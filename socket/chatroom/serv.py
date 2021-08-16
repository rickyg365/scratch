import os
import sys
import socket
import threading


"""
Program: Chatroom
"""

HEADER = 1024
FORMAT = 'utf-8'
DISCONNECT = "!QUIT"

PORT = 12345
HOST = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Listening for connections...")

clients = []
nicknames = []

"""

[) | Joe || newt || toot || rewt | (]

"""

def chat_status():
    chat_stat = ""

    for name in nicknames:
        chat_stat += f"| {name} |"

    return f"[ {chat_stat} ]"


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(a_client, a_nickname):
    while True:
        try:
            message = a_client.recv(HEADER)
            # if message.decode(FORMAT).split(':')[1] == DISCONNECT:
            #     index = nicknames.index(a_nickname)
            #     clients.pop(index)
            #     a_client.close()
            #     nicknames.remove(a_nickname)
            #     broadcast(f"{a_nickname} left!".encode(FORMAT))
            broadcast(message)
        except Exception as e:
            # print(nicknames)
            # print(clients)
            ind = nicknames.index(a_nickname)
            clients.pop(ind)
            a_client.close()
            nicknames.remove(a_nickname)
            broadcast(f"{a_nickname} left!".encode(FORMAT))
            print(f"{a_nickname} left!")
            print(f"active chat => {chat_status()}")
            break


def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print(f"[Connected] {address}")

        # Request and save Nickname
        client.send("NICK".encode(FORMAT))
        nickname = client.recv(HEADER).decode(FORMAT)
        nicknames.append(nickname)
        # print(nicknames)
        clients.append(client)

        # print and broadcast names
        print(f"Nickname => {nickname}")  # Print is output for server, broadcast for clients

        broadcast(chat_status().encode(FORMAT))
        broadcast(f"{nickname} joined!".encode(FORMAT))

        # Thread
        client_thread = threading.Thread(target=handle, args=(client, nickname))
        client_thread.start()


if __name__ == "__main__":
    receive()
