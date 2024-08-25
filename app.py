from flask import Flask, render_template, request, jsonify, session
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import timedelta
import uuid
import pyotp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['SESSION_REFRESH_EACH_REQUEST'] = True

socketio = SocketIO(app, cors_allowed_origins="*")

CERT = 'cert.pem'
CERT_KEY = 'key.pem'
rooms = {}

# OTP setup
otp_secret = pyotp.random_base32()  #  generating OTPs
print(otp_secret)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_room', methods=['POST'])

def create_room():
    otp_provided = request.json.get('otp')
    totp = pyotp.TOTP(otp_secret)

    if not otp_provided or not totp.verify(otp_provided):
        return jsonify({'error': 'Invalid OTP'}), 403

    room_id = str(uuid.uuid4())
    rooms[room_id] = {'host': None, 'viewers': []}
    print(f"Room created: {room_id}")
    return jsonify({'room_id': room_id})


@socketio.on('join')
def on_join(data):
    room_id = data['room_id']

    if room_id not in rooms:
        emit('error', {'message': 'Room not found'})
        return

    join_room(room_id)
    if not rooms[room_id]['host']:
        rooms[room_id]['host'] = request.sid
        emit('host_joined', {'room_id': room_id})
    else:
        rooms[room_id]['viewers'].append(request.sid)
        emit('viewer_joined', {'room_id': room_id})

    print(f"Current room state: {rooms[room_id]}")




if __name__ == '__main__':
    context = ('cert.pem', 'key.pem')
    socketio.run(app, debug=True, host='0.0.0.0', port=5001, certfile=CERT, keyfile=CERT_KEY)
