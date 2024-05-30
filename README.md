# C2 Server

The C2 Server is a comprehensive Remote Administration Tool (RAT) implemented in Python. Designed for ethical hacking and educational purposes, this tool facilitates control and management of remote systems through a command-and-control server. It supports generating payloads for different platforms, managing multiple sessions, and executing commands on remote targets.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Main Menu Commands](#main-menu-commands)
  - [Session Commands](#session-commands)
- [Functions](#functions)
  - [Communication Functions](#communication-functions)
  - [Listener Functions](#listener-functions)
  - [Payload Functions](#payload-functions)
  - [Helper Functions](#helper-functions)
- [Contributing](#contributing)
- [License](#license)

## Features

- Start a listener to accept connections from clients.
- Generate payloads for Windows and Linux.
- Generate executable payloads for Windows.
- List and manage active sessions.
- Send commands to remote targets.
- Maintain persistence on remote targets.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/C2-Server.git
    ```
2. Navigate to the project directory:
    ```sh
    cd C2-Server
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script:

```sh
python server.py
```

## Main Menu Commands

- `help`: Display help information.
- `listen -g`: Generate a new listener.
- `windows`: Generate a Windows compatible Python payload.
- `linux`: Generate a Linux compatible Python payload.
- `executable`: Generate an executable payload for Windows.
- `sessions -l`: List active sessions.
- `sessions -i <val>`: Enter a specific session by its ID.
- `kill <val>`: Kill an active session by its ID.
- `pshell_shell`: Generate a PowerShell payload.
- `exit`: Exit the program.

## Session Commands

- `background`: Background the current session.
- `exit`: Terminate the current session.

## Functions

### Communication Functions

- `comm_in(targ_id_input)`: Receives and decodes a message from the target.
- `comm_out(targ_id_input, message)`: Encodes and sends a message to the target.
- `kill_sig(targ_id_input, message)`: Sends a termination signal to the target.

### Listener Functions

- `listener_handler()`: Starts the listener and waits for connections.
- `comm_handler()`: Handles communication with connected targets.

### Payload Functions

- `winplant()`: Generates a Windows-compatible Python payload.
- `linplant()`: Generates a Linux-compatible Python payload.
- `exeplant()`: Generates an executable payload for Windows.
- `pshell_cradle()`: Generates a PowerShell payload.

### Helper Functions

- `help_desk()`: Displays the help menu.
- `target_comm(targ_id_input, target_input, num_targets)`: Manages communication with a specific target session.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Disclaimer:** This tool is intended for educational purposes only. Use it at your own risk and ensure you have permission before using it on any target system. I am not responsible for any misuse or damage caused by this tool.
