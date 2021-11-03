##Importations library
import threading
import time
import socket

## Constante Server
host = "127.0.0.1" ## A Changer vers un server défini 
port = 64030
utilisateurs=[]

class ThreadReception(threading.Thread):

    def __init__(self, server):
        threading.Thread.__init__(self)
        self.running = True
        self.server = server

    def run(self): ## C'est encore un peu buggué, je corrigerai ca plus tard
        while(self.running):

            time.sleep(0.08) ## Facilite la lecture d'affichage
            data = self.server.recv(2048).decode()

            if(data == 'fin'):
                self.running = False
                self.server.close()
                return 0

            print('\nRecu :', data)

        print("Communication coupée !")
        return 0

class ThreadConnexion(threading.Thread):

    def __init__(self, server):
        threading.Thread.__init__(self)
        self.running = True
        self.server = server

    def run(self):
        with self.server:
            r = ThreadReception(self.server)
            r.start()
            print("Connecté à", self.server.getpeername())

            while(r.running):
                msg = bytes(input("Envoyer un message : "), 'UTF-8')
                self.server.send(msg)
                if(msg.decode() == 'fin'):
                    r.running = False
                    break
            self.server.close()



def connexion(premiere):
    if(premiere):
        creationCompte()
    else:
        id = input("Entrez votre id ou email : ")
        mdp = input("Entrez votre mot de passe : ")



def creationCompte():
    a=0