import socket

hosts = []
MAX_SIZE_BYTES = 65535
port = 3001
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

while True:
    host = input('Inout Host Address: ')
    hosts.append((host,port))
    
    message = input('Input lower Scentence: ')
    data = message.encode('ascii')
    s.sendto(data, (host,port))
    print('The OS assigned the address {} to me'.format(s.getsockname()))
    data , address = s.recvfrom(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    if(address in hosts):
        print('The server {} replied with {!r}'.format (address,text))
        hosts.remove(address)
    else:
        print('Message {!r} from unexpected host{}'.format(text,address))