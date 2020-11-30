import socket



def recvall(sock,length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more

    return data


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('127.0.0.1',3000))

s.listen(1)

print('listening at {}'.format(s.getsockname()))

while True:
    sc, sockname = s.accept()
    print('connection from: ',sockname)
    print('socket name: ', sc.getsockname())
    print('socket peer: ', sc.getpeername())
    message = recvall(sc, 16)
    print('Message from the client: ',repr(message))
    sc.sendall(b'good bye client!')
    sc.close()
    print('Closing socket')


