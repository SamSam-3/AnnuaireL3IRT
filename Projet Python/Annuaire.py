##Importations library
from os import name
import threading
import time
import socket


## IDEES:
## Faire une GUI (Tkinter très probablement)
## ???
## ???

## Constante Server
host = "192.168.1.33" ## A Changer vers un server défini 
port = 64030
utilisateursConnectes=[]

class ThreadReception(threading.Thread):

    def __init__(self, server,name):
        threading.Thread.__init__(self)
        self.running = True
        self.server = server
        self.name = name

    def run(self): ## C'est encore un peu buggué, je corrigerai ca plus tard
        while(self.running):

            time.sleep(0.08) ## Facilite la lecture d'affichage
            data = self.server.recv(2048).decode()

            if(data == 'fin'):
                self.running = False
                self.server.close()
                print(self.name +" déconnecté")
                utilisateursConnectes.remove(self.name)
                return 0
            
            print('\nRecu par {}: {}'.format(self.name,data))

            ##Commandes Server

            ## Affiche les utilisateurs connectés
            if(data == 'ut'):
                print(utilisateursConnectes)

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

class ThreadConnexion(threading.Thread):

    def __init__(self, server):
        threading.Thread.__init__(self)
        self.running = True
        self.server = server
        self.name = "name"

    def run(self):

        resp = self.server.recv(1024).decode() ## Attend la réponse de connexion d'un client
        
        if(resp not in utilisateursConnectes):
            self.name = resp
            utilisateursConnectes.append(resp)
            self.startServer()

    def startServer(self):
        with self.server:
            r = ThreadReception(self.server, self.name)
            r.start()
            print("Connecté à", self.name)

            while(r.running):
                msg = bytes(input("Envoyer un message : "), 'UTF-8')
                self.server.send(msg) 
                ##Erreur --> Le server envoi le message à l'un puis à l'autre machine connecté
                ## Pour l'instant peut être pas une erreur si le server répond rapidement aux demandes
                if(msg.decode() == 'fin'):
                    r.running = False
                    break

            self.server.close()


## Fonctions commande Annuaire

def connexion(premiere):
    verif = True
    if(premiere):
        db = open("dbUtilisateurs.txt",'a')
        id = input("Entrez une id utilisateur : ")
        mdp = input("Entrez un mot de passe : ")
        email = input("Entrez votre email : ")
        champs=[id,mdp,email]

        for i in champs:
            db.write(i+";")
        db.write("\n")

        print("Vous possédez maintenant un compte !\n")
        db.close()
        connexion(False)
    else:
        while(verif):
            print("-------------| CONNEXION |---------------\n")
            id = input("Entrez votre id ou email : ")
            mdp = input("Entrez votre mot de passe : ")

            with open("dbUtilisateurs.txt",'r') as db:
                for i in db.readlines():
                    if(i.split(";")[0]==id and i.split(";")[1]==mdp and id not in utilisateursConnectes):
                        verif = not verif
                        db.close()
                if(verif):
                    print("Mauvaises informations !")
                    print("Veuillez réessayer :")

        print("Connecté")
        return id
         
#Pour actualiser : git fetch && git pull