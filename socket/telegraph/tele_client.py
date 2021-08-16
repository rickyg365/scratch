import socket
import threading
import time

from morse import *

"""
Program: Morse Communications Client
Author: RickyG3
Date: 08/09/2021
"""


# Variables
HEADER = 30
FORMAT = 'utf-8'
DISCONNECT_MSG = '!BYE'

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


# Functions
def send(raw_msg):
    encoded_msg = raw_msg.encode(FORMAT)
    msg_length = len(encoded_msg)
    processed_length = str(msg_length).encode(FORMAT)
    processed_length += b' ' * (HEADER - len(processed_length))

    client.sendall(processed_length)
    client.sendall(encoded_msg)


def receive():
    connected = True
    while connected:
        new_msg_length = int(client.recv(HEADER).decode(FORMAT))
        raw_received = client.recv(new_msg_length).decode(FORMAT)
        received = raw_received  # convert_morse(raw_received)

        print(f"Received: {received}")

        time.sleep(.5)


if __name__ == "__main__":
    msg = ""

    ping = threading.Thread(target=receive)
    ping.start()

    while msg != DISCONNECT_MSG:
        msg = input()

        send(msg)
