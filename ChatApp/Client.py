import socket


MAX_SIZE_BYTES = 65535
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_address = '127.0.0.1'
port = 3000
while True:
    s.connect((host_address,port))
    #hosts.append((host_address,port))
    message = input('Enter a message: ')
    data = message.encode('ascii')
    s.send(data)
    data = s.recv(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    print('The client replied with {!r}'.format(text))    