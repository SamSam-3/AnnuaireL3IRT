from AnnuaireClient import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((client.host, client.port))

    name = conn(False,s)

    r = ReceptionClient(s,name)
    r.start()
    
    while(r.running):
        
        msg = bytes(input("Envoyer un message : "), 'UTF-8')
        s.send(msg)
        if(msg.decode() == 'fin'):
            r.running = False
            s.close()
            break