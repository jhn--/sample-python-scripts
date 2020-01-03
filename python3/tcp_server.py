#!/usr/bin/env python3.4

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20 # normally 1024, but we want fast response
#BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print("conn = {0}".format(conn))
print("addr = {0}".format(addr))
print("Connection address: {0}".format(addr))
while 1:
    data = conn.recv(BUFFER_SIZE)
    conn.send(data) #echo
    data_1 = conn.recv(BUFFER_SIZE).decode()
    if not data:
        break
    print("received data: {0}".format(data.decode()))
    #print("received data: {0}".format(data_1))
    #conn.send(data) #echo
conn.close()