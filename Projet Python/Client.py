from Annuaire import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    name = connexion(False)

    r = ThreadReception(s,name)
    r.start()
    
    s.send(bytes(name.encode()))
    while(r.running):
        
        msg = bytes(input("Envoyer un message : "), 'UTF-8')
        s.send(msg)
        if(msg.decode() == 'fin'):
            r.running = False
            break