import os
import sys
import threading
import socket


"""
Program: Chatroom Client
"""


nickname = input("Nickname?: ")

HEADER = 1024
FORMAT = 'utf-8'
DISCONNECT = "!QUIT"

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def clear_screen():
    platforms = {
        'linux1': 'clear',
        'linux2': 'clear',
        'darwin': 'clear',
        'win32': 'cls'
    }
    if sys.platform not in platforms:
        print(f"{sys.platform}")

    os.system(platforms[sys.platform])


def receive():
    while True:
        try:
            message = client.recv(HEADER).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
            else:
                name = message.split(':')[0][1:-1]
                if name != nickname:
                    print(message)
        except Exception as e:
            # print(e)
            client.close()
            break


def send_msg():
    while True:
        message = f"[{nickname}]: {input('')}"
        if message == f"[{nickname}]: !QUIT":
            # client.send(DISCONNECT.encode(FORMAT))
            client.close()
            break
        client.send(message.encode(FORMAT))


if __name__ == "__main__":
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=send_msg)
    write_thread.start()
