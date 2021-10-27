from Annuaire import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    r = ThreadReception("",conn)
    r.start()
    with conn:
        print("Connecté à", addr)

        while True:
            msg = bytes(input("Envoyer un message : ").encode(encoding='utf-8'))
            conn.send(msg)