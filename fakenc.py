import argparse
import socket
import sys
import threading
import random


def handle_client(client_socket):
    with client_socket as sock:
        client_address = sock.getpeername()  # Get client's IP and port
        while True:
            try:
                request = sock.recv(1024)
                if len(request) != 0:
                    print(f'[*] Received from {client_address[0]}:{client_address[1]}: {request.decode("utf-8")}')
                    sock.send(b'ACK')
            except BaseException:
                break



parser = argparse.ArgumentParser(description="This is a fake netcat")
parser.add_argument("-v", "--verbose", help="Don't need this yet", action="store_true")
parser.add_argument("-l", "--listen", help="Listen for incoming traffics", action='store_true')
parser.add_argument("-p", "--port", help="Specify port number", type=int, default=random.randint(2000, 60000))
args = parser.parse_args()
if args.verbose:
    print("Developing")

if args.listen:
    print(f"Listening on port {args.port}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', args.port))
    server.listen(5)

    while True:
        try:
            client, address = server.accept()
            print(f'[*] Accepted connection from {address[0]}:{address[1]}')
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()
        except KeyboardInterrupt:
            sys.exit()
