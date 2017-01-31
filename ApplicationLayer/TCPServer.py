#!/usr/bin/env python3
from socket import *
import time

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    print("Receive: "+message.decode('utf-8'))
    response = time.ctime().encode('utf-8')
    connectionSocket.send(response)
    connectionSocket.close()
