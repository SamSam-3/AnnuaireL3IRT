import socket

host = "127.0.0.1"
port = 65535

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.send(b'Hello World')
    data = s.recv(1024)

print('Recu :', repr(data))