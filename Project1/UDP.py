'''Purpose of the program
    The client will send a line of text to the server.
    The server will receive the data and convert each character to uppercase.
    The server will send the uppercase characters to the client.
    The client will receive and display them on its screen.
'''
#Importing a Socket library
import socket

MAX_SIZE_BYTES = 65535
#creating a object 's' with syntax 'socket.socket(family,type,proto,fileno'
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#AF_INET = IPV4 ;  SOCK_DGRAM = for UDP ; SOCK_STREAM = TCP

port = 3001  # port number
hostname =  '127.0.0.1' #local host
s.bind((hostname,port))

print('listening at {}'.format(s.getsockname()))

while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    upperCaseMessage = message.upper()
    print('The client at {} says {!r}'.format(clientAddress, message))
    data = upperCaseMessage.encode('ascii')
    s.sendto(data , clientAddress)