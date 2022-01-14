import  socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = '127.0.0.1'
    s.bind((hostname, port))
    print('Listening at {}'.format(s.getsockname()))
    while True:
        data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
        message = data.decode('ascii')
        print('The client at {} says {!r}'.format(clientAddress, message))
        msg_to_send = input('Input message to send to client:' )
        data = msg_to_send.encode('ascii')
        s.sendto(data, clientAddress)

server(3001)