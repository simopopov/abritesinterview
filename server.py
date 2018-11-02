import socketserver
from solver import Solver

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip().decode()
            if not self.data:
                break
            try:
                p = Solver(self.data)
                value = "{} = {}".format(self.data, p.getValue())
            except:
                value = "Error in parsing your expression"
            self.request.sendall(value.encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 1234

    # Create the server, binding to localhost on port 9999
    server = ThreadedTCPServer((HOST, PORT), Server)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("The server is stopped")
        server.server_close()