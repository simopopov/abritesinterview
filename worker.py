import threading
from expressionParser import Parser

class Worker(threading.Thread):

    def __init__(self, client_socket, *args, **kwargs):
        self.client_socket = client_socket
        super(Worker, self).__init__(*args, **kwargs)

    def handle_client_connection(self):
        while True:
            try:
                try:
                    msg_from_client = self.client_socket.recv(2048)
                except:
                    return
                if not msg_from_client:
                    return
                elif msg_from_client.decode() == "exit":
                    return
                else:
                    try:
                        print("MESSAGE")
                        print(msg_from_client.decode())
                        p = Parser(msg_from_client.decode())
                        value = p.getValue()
                    except Exception as e:
                        print(str(e))
                        value = "Something is wrong with the expression"
                    self.client_socket.send("The answer is: {}".format(value).encode())
            except KeyboardInterrupt:
                print("Worker KeyboardInterrupt")
                return

    def run(self):
        self.handle_client_connection()
        self.client_socket.close()
        return