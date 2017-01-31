#!/usr/bin/env python3
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input("Input message\n")
clientSocket.send(message.encode('utf-8'))
response = clientSocket.recv(1024)
print(response.decode('utf-8'))
clientSocket.close()
