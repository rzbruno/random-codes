import thread
from socket import *

HOST = "0.0.0.0"
PORT = 1234

def f(clientsock, addr):
   clientsock.settimeout(3)
   clientsock.send("Hi there!")
   clientsock.close()

if __name__ == '__main__':
   ADDR = (HOST, PORT)
   serversock = socket(AF_INET, SOCK_STREAM)
   serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
   serversock.bind(ADDR)
   serversock.listen(1)

   while 1:
      clientsock, addr = serversock.accept()
      thread.start_new_thread(f, (clientsock, addr))
