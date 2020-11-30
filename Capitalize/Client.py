import socket


MAX_SIZE_BYTES = 65535
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hosts = []
host_address = '127.0.0.1'
port = 3000
print(hosts)
while True:
    s.connect((host_address,port))
    #hosts.append((host_address,port))
    message = input('Enter a lowercase sentence: ')
    data = message.encode('ascii')
    s.sendto(data,(host_address,port))
    print('The OS assigned the address {} to me'.format(s.getsockname()))
    data, address = s.recvfrom(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    if address in hosts:
        print('The server at {} replied with {!r}'.format(address,text))
        hosts.remove(address)
    else:
        print('message {!r} from unexpected host {}!'.format(text, address))