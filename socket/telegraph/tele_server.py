import socket
import threading

import time

from morse import *

"""
Program: Morse Communications Server
Author: RickyG3
Date: 08/09/2021
"""


# Variables
HEADER = 30
FORMAT = 'utf-8'
DISCONNECT_MSG = '!BYE'


HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


# Functions

def send(raw_msg, conn):
    encoded_msg = raw_msg.encode(FORMAT)
    msg_length = len(encoded_msg)
    processed_length = str(msg_length).encode(FORMAT)
    processed_length += b' ' * (HEADER - len(processed_length))

    conn.sendall(processed_length)
    conn.sendall(encoded_msg)


def receive(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                connected = False
                print("[DISCONNECTED]")
                continue

            print(f"[{addr}] {msg}")  # convert_morse(msg)

        time.sleep(.5)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # msg_length = conn.recv(HEADER).decode(FORMAT)
        #
        # if msg_length:
        #     msg_length = int(msg_length)
        #     msg = conn.recv(msg_length).decode(FORMAT)
        #
        #     if msg == DISCONNECT_MSG:
        #         connected = False
        #         print("[DISCONNECTED]")
        #         continue
        #
        #     print(f"[{addr}] {msg}")  # convert_morse(msg)
        ping = threading.Thread(target=receive, args=(conn, addr))
        ping.start()

        response = input(">>> ")
        if response != "":
            send(response, conn)

    conn.close()


def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    print("[STARTING] server is starting...")
    start_server()
