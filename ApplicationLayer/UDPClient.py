#!/usr/bin/env python3
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input message\n")
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
response, serverAddress = clientSocket.recvfrom(2048)
print(response)
clientSocket.close()
