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


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',3000))
print('The client has been assigned to sockett: ', s.getsockname())
s.sendall(b'Greetings server')
reply = recvall(s,16)
print('server', repr(reply))
s.close()






