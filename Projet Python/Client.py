from AnnuaireClient import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.connect((client.host, client.port)) ##Connexion au serveur

    name = conn(True,s) ##Se connecte et récupère le nom du client

    r = ReceptionClient(s,name) ##Recoit les données asynchroniquement
    r.start()
    
    while(r.running):
        
        msg = bytes(input("Envoyer un message : "), 'UTF-8')
        entree = msg.decode()

        if(entree == 'fin'):
            s.send(msg)
            r.running = False
            s.close()
            exit(0)

        elif(entree == 'help'): ## Récupère la liste des commandes disponibles
            for commande in commandes:
                print("\t- {}".format(commande))

        elif(entree in commandes):
            s.send(msg)
            
        else:
            s.send(msg)