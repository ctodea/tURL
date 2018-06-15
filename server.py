#!/usr/bin/env python3
from url import Url
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 15000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(16)
            if data:
                x = Url()
                connection.sendall(x.newUrl(data.decode('ascii')))
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
