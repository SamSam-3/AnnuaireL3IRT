##Importations library
import threading
import time
import socket

## Constante Server
host = "127.0.0.1" ## A Changer vers un server défini 
port = 64030

class ThreadReception(threading.Thread):
    def __init__(self, stop, server):
        threading.Thread.__init__(self)
        self.stop = stop
        self.server = server

    def run(self):
        while(self.stop != b'fin'):
            time.sleep(0.08) ## Facilite la lecture d'affichage
            data = repr(self.server.recv(1024).decode('utf-8'))
            print('\nRecu :', data)

def connexion(premiere):
    if(premiere):
        creationCompte()
    else:
        id = input("Entrez votre id ou email : ")
        mdp = input("Entrez votre mot de passe : ")



def creationCompte():
    a=0