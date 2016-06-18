from socket import *
import threading

BUFF = 1024
HOST = '127.0.0.1'
PORT = 9999

def gen_response():
    return 'this_is_the_return_from_the_server'

def handler(clientsock,addr):
    while 1:
        data = clientsock.recv(BUFF)
        print('data:' + repr(data))
        if not data: break
        clientsock.send(gen_response())
        print('sent:' + repr(gen_response()))
        clientsock.close()

if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print('waiting for connection...')
        clientsock, addr = serversock.accept()
        print('...connected from:' + str(addr))
        threading.Thread(target=handler, args=(clientsock, addr)).start()
