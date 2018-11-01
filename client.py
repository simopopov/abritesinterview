import socket

class Client:
    def __init__(self, host_name, port_number):
        self.host_name = host_name
        self.port_number = port_number
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host_port_pair = (self.host_name, self.port_number)

    def start(self):
        self.sock.connect(self.host_port_pair)
        while True:
            try:
                print ("TYPE A MESSAGE FOR SERVER ==> ")
                msg_for_server = input()
                if not msg_for_server:
                    break
                self.sock.send(msg_for_server.encode())
                
                msg_from_server = self.sock.recv(2048)
                if not msg_from_server:
                    print ("<...No Reply from Server...>")
                else:
                    print ("From Server ==> ", msg_from_server)
            except KeyboardInterrupt:
                print("Bye bye from me")
                self.close()
                break

        self.close()


    def close(self):
        self.sock.close()


if __name__ == '__main__':
    client = Client('127.0.0.1', 1234)
    client.start()