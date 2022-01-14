import  socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
while True:
    s.connect((host, 3001))
    message = input('Input message to send to server:' )
    data = message.encode('ascii')
    s.send(data)
    data = s.recv(MAX_SIZE_BYTES) 
    text = data.decode('ascii')
    print('The server replied with {!r}'.format(text))


