import socket
import threading
import time

host = "127.0.0.1"
port = 65535

class ThreadReception(threading.Thread):
    def __init__(self, stop, server):
        threading.Thread.__init__(self)
        self.stop = stop
        self.server = server

    def run(self):
        while(self.stop != b'fin'):
            data = repr(s.recv(1024).decode(encoding='utf-8'))
            time.sleep(0.08) ## Facilite la lecture d'affichage
            print('\nRecu :', data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    r = ThreadReception("",s)
    r.start()

    while True:
        msg = bytes(input("Envoyer un message : ").encode(encoding='utf-8'))
        s.send(msg)