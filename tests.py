import socket
import unittest

from expressionParser import Parser

class TestServer(unittest.TestCase):

    def setUp(self):
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host_port_pair = ('127.0.0.1', 1234) 
        self.client_socket.connect(host_port_pair) 

    def tearDown(self):
        self.client_socket.close()

    def test_successful_1(self):
        self.client_socket.send('1+2'.encode())
        self.assertEqual(self.client_socket.recv(1024).decode(), 'The answer is: 3.0')

    def test_successful_2(self):
        self.client_socket.send('(4*(2+3))/5'.encode())
        self.assertEqual(self.client_socket.recv(1024).decode(), 'The answer is: 4.0')

    def test_successful_3(self):
        self.client_socket.send('((1 + 3) / 3.14) * 4 - 5.1'.encode())
        self.assertEqual(self.client_socket.recv(1024).decode(), 'The answer is: -0.004458598726114538')

    def test_wrong_expression(self):
        self.client_socket.send('alabala'.encode())
        self.assertEqual(self.client_socket.recv(1024).decode(), 'The answer is: Something is wrong with the expression')

class TestParser(unittest.TestCase):

    def test_successful_calculation(self):
        parser = Parser("1+2")
        self.assertEqual(parser.getValue(), 3.0)

    def test_exception_handling(self):
        parser = Parser("Wrong expression")
        self.assertRaises(TypeError, parser.getValue)

if __name__ == '__main__':
    unittest.main()