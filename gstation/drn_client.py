# Echo client program
import socket
import time

HOST = '192.168.0.10'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1.0)
s.connect((HOST, PORT))
s.sendall('Hello, world')
s.sendall('Another message')
s.sendall('Yet something else')
for x in range(1, 50):
    time.sleep(0.1)
    s.sendall(str(x) + '\n')

s.close
