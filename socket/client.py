import os
import sys
import socket

"""
Program: Simple Client
"""

'''
argv:
    0 - filename
    1 - first arg
    2 - second arg
    .
    .
    .
    -1 - last arg

'''
#
# for _, arg in enumerate(sys.argv):
#     print(_, arg)

#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     for i, arg in enumerate(sys.argv):
#         if i == 0:
#             s.sendall(f"Filename:{arg.split('.')[0]}, ".encode())
#             continue
#         new_string = f"A{i}:{arg}, "
#         s.sendall(new_string.encode())
#     data = s.recv(1024)
#
# print('Received', repr(data))


if __name__ == "__main__":

    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!BYE"

    HOST = socket.gethostbyname(socket.gethostname())  # Get local machine
    PORT = 12345  # Reserve a port for service

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))

        client.send(send_length)
        client.send(message)


    # send("Hello Fro yo")
    # send("Hello yo yo")
    # send(DISCONNECT_MESSAGE)

    msg = ""

    while msg != DISCONNECT_MESSAGE:
        msg = input(">>> ")

        send(msg)


