from Annuaire import *

host = "127.0.0.1"
port = 64030

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    r = ThreadReception("",s)
    r.start()

    while True:
        msg = bytes(input("Envoyer un message : ").encode(encoding='utf-8'))
        s.send(msg)