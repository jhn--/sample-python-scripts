#!/usr/bin/env python3.4

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#MESSAGE = 'Hello, world!'.encode()
MESSAGE = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean porttitor consectetur metus, vitae condimentum nisi porttitor vel. Ut lacinia dui ut tincidunt placerat. Mauris quis urna justo. Vestibulum dictum neque in justo porta ultrices. Sed maximus sit amet lorem et suscipit. Duis purus libero, ullamcorper quis eleifend at, euismod non purus. In congue lectus nec quam facilisis volutpat. Pellentesque at enim odio. Proin non sollicitudin elit, non ultrices urna. Mauris scelerisque et felis eu congue. Aliquam ac lacus ac urna consequat convallis vitae sed leo. Etiam vitae diam at orci congue bibendum et fringilla arcu. Aenean in turpis a tortor feugiat venenatis ut a tortor. Aenean urna purus, vulputate eu commodo eu, tempor eu nisl. Aenean posuere luctus libero, sed venenatis justo venenatis et.'.encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
print(MESSAGE)
data = s.recv(BUFFER_SIZE)
print("received: data: {0}".format(data))
#print(BUFFER_SIZE)
#s.recv(BUFFER_SIZE)
#print(s.recv(BUFFER_SIZE))
#print("data = {0}".format(data))
s.close()

