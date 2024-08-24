# CyberLink

## Overview

*CyberLink** is a cutting-edge screen-sharing application that allows users to create and join real-time screen-sharing sessions with ease. Built with Flask and Socket.IO, it provides seamless, high-quality screen sharing with a focus on security and user experience.

## Features

- **Create and Join Rooms**: Easily create new rooms or join existing ones using a unique Room ID.
- **Screen Sharing**: Share your screen in real-time with other participants.
- **Secure Access**: Integration with OTP for secure room creation and joining.
- **Responsive Design**: Optimized for various screen sizes and devices.
- **Status Updates**: Real-time status updates on connection and sharing state.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- Flask-SocketIO
- pyotp

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Place your SSL certificates in the root directory of the project as `cert.pem` and `key.pem`.

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and navigate to `https://localhost:5001` to start using the application.

## Usage

1. **Create a Room**: Click on "Create Room" to generate a new room. Copy the Room ID for sharing.
2. **Join a Room**: Enter a Room ID and click "Join Room" to participate in an existing session.
3. **Start Sharing**: Once in a room, click "Start Sharing" to begin sharing your screen.
4. **Stop Sharing**: Click "Stop Sharing" to end your screen-sharing session.

## Screenshots

![Screenshot 1](path/to/screenshot1.png)
![Screenshot 2](path/to/screenshot2.png)
![Screenshot 3](path/to/screenshot3.png)

## Contributing

1. Fork the repository.
2. Create a feature branch 
3. Commit your changes 
4. Push to the branch 
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


