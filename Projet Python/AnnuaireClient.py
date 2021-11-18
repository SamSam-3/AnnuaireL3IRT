import socket
import threading
import time

class ReceptionClient(threading.Thread):

    def __init__(self, server,name):
        threading.Thread.__init__(self)
        self.running = True
        self.server = server
        self.name = name

    def run(self): ## C'est encore un peu buggué, je corrigerai ca plus tard
        while(self.running):

            time.sleep(0.08) ## Facilite la lecture d'affichage
            data = self.server.recv(2048).decode() ## Recoit le retour du

            if(data == 'fin'):
                self.running = False
                self.server.close()
                print(self.name +" déconnecté")

            else:
                print('\nRecu par {}: {}'.format(self.name,data))

                ##Commandes Server
                
                ## Affiche les utilisateurs connectés
                if(data == 'ut'):
                    a=0

            ## Fonctions utiles (A faire): 

            ## admin :
            ## - Creer/Supprimer/Modifier un compte

            ## utilisateur :

            ## - importer un/des contact(s)
            ## - exporter un/des contacts(s)
            ## - creer/supprimer/modifier un contact
            ## - afficher les infos d'un contact
            ## - Partager son annuaire à un compte
            ## - Bonus ??


        print("Communication coupée !")
        return 0

class Client():
    def __init__(self,port,host):
        self.connected = False
        self.port = port
        self.host = host

def conn(premiere,server):
    verif = True
    if(premiere):
        id = input("Entrez une id utilisateur : ")
        mdp = input("Entrez un mot de passe : ")
        email = input("Entrez votre email : ")
        champs=[0,id,mdp,email]

        server.send(bytes(str(champs).encode())) ## Envoie les champs nécessaire à la création de compte

        print(server.recv(1024).decode())
        print("Vous possédez maintenant un compte !\n")
        
        conn(False,server)
    else:
        while(verif):
            print("-------------| CONNEXION |---------------\n")
            id = input("Entrez votre id ou email : ")
            mdp = input("Entrez votre mot de passe : ")
            champs=[1,id,mdp]
    
            server.send(bytes(str(champs).encode()))
            
            time.sleep(0.08)
            data = server.recv(2048).decode()

            if(data[0]=="0"):        
                verif = False
                client.connected = True
                print("Connecté")
                return id


client = Client(64030,"192.168.43.26")