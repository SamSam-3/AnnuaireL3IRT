from Annuaire import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    r = ThreadReception(s)
    r.start()

    while r.running:
        msg = bytes(input("Envoyer un message : ").encode(encoding='utf-8'))
        s.send(msg)
    print("Communication coupée !")