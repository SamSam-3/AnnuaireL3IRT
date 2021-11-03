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

        resp= self.server.recv(1024).decode() ## Attend la réponse de connexion d'un client
        if(resp == 'ConnexionOk'):
            self.startServer()

    def startServer(self):
        with self.server:
            r = ThreadReception(self.server)
            r.start()
            print("Connecté à", self.server.getpeername())

            while(r.running):
                msg = bytes(input("Envoyer un message : "), 'UTF-8')
                self.server.send(msg) 
                ##Erreur --> Le server envoi le message à l'un puis à l'autre machine connecté
                ## Pour l'instant peut être pas une erreur si le server répond rapidement aux demandes
                if(msg.decode() == 'fin'):
                    r.running = False
                    break
            self.server.close()



def connexion(premiere):
    if(premiere):
        with open("dbUtilisateurs.txt",'w') as db:
            id = input("Entrez une id utilisateur : ")
            mdp = input("Entrez un mot de passe : ")
            email = input("Entrez votre email : ")
            champs=[id,mdp,email]

            for i in champs:
                db.write(i+";")

            print("Vous possédez maintenant un compte !\n")
            connexion(False)
    else:
        while(True):
            print("-------------| CONNEXION |---------------\n")
            id = input("Entrez votre id ou email : ")
            mdp = input("Entrez votre mot de passe : ")

            with open("dbUtilisateurs.txt",'r+') as db:
                for i in db.readlines():
                    if(i.split(";")[0]==id or i.split(";")[1]==mdp):
                        print("Connecté")
                        return 0
