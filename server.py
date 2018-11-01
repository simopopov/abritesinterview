import socket
import threading

from worker import Worker

class Server:

    def __init__(self, host_name, port_number):
        self.host_name = host_name
        self.port_number = port_number
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host_port_pair = (self.host_name, self.port_number)

    def start(self):
        
            self.sock.bind(self.host_port_pair)
            self.sock.listen(10)
            while True:
                try:
                    client_sock = None
                    client_sock, address = self.sock.accept()
                    worker = Worker(client_sock)
                    worker.start()
                except KeyboardInterrupt:
                    if client_sock:
                        client_sock.close()
                    self.sock.close()
                    return
                    
        


if __name__ == '__main__':
    client = Server('127.0.0.1', 1234)
    client.start()