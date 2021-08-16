import os
import socket
import threading

"""
Program: Simple Server
"""
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     print("Waiting...")
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)


if __name__ == "__main__":
    # Variables
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!BYE"

    HOST = socket.gethostbyname(socket.gethostname())  # Get local machine
    PORT = 12345  # Reserve a port for service

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))

    def handle_client(conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    print("[Disconnected]")
                    continue
                print(f"[{addr}] {msg}")

        conn.close()

    def start_server():
        server.listen()
        print(f"[LISTENING] Server is listening on {HOST}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    print("[STARTING] server is starting...")
    start_server()


