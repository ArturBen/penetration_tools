#!/usr/bin/env python3

import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.0.105", 4444))
connection.send("\n[+] Connection established.\n")
connection.close()
