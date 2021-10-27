##Importations library
import threading
import time
import socket

## Constante Server
host = "127.0.0.1" ## A Changer vers un server défini 
port = 64030

class ThreadReception(threading.Thread):

    def __init__(self, server):
        threading.Thread.__init__(self)
        self.running = True
        self.server = server

    def run(self): ## C'est encore un peu buggué, je corrigerai ca plus tard
        while(self.running):
            time.sleep(0.08) ## Facilite la lecture d'affichage
            data = repr(self.server.recv(1024).decode('utf-8'))
            print('\nRecu :', data)
            if(data == "'fin'"):
                self.running = False
        return 0

def connexion(premiere):
    if(premiere):
        creationCompte()
    else:
        id = input("Entrez votre id ou email : ")
        mdp = input("Entrez votre mot de passe : ")



def creationCompte():
    a=0