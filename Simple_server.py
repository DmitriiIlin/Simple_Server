from socketserver import BaseRequestHandler, TCPServer
from socket import socket, AF_INET, SOCK_STREAM

class TestTCPHandler(BaseRequestHandler):

    def handle(self):
        print("handle activated", self.client_address)
        self.data = self.request.recv(1024).strip()
        print(self.data)
        self.request.send(b'privet, hello')



def server_active():
    #Активация сервера
    server = TCPServer(('localhost', 12345), TestTCPHandler)
    server.serve_forever()
    
def client():
    #Создание клиента сервера
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 12345))
    s.send(b'Hello')
    print(s.recv(1024).strip())

server_active()
client()