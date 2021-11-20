import socket
import threading
import time

commandes = ["ut","ajouterContact"]
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
                print('\nRecu par le serveur : {}'.format(data))

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
    if(premiere): ## Si c'est la 1ere connexion
        id = input("Entrez une id utilisateur : ") ## Champs nécessaire à renseigner
        mdp = input("Entrez un mot de passe : ")
        email = input("Entrez votre email : ")
        champs=[0,id,mdp,email]

        server.send(objecttobytes(champs)) ## Envoie les champs nécessaire à la création de compte

        print(server.recv(1024).decode()) ## Attend le retour du serveur à la création du compte

        premiere = False

    if(not premiere): 

        while(verif): ##Tant que le client ne renseigne pas de bonnes informations
            print("-------------| CONNEXION |---------------\n")
            id = input("Entrez votre id ou email : ")
            mdp = input("Entrez votre mot de passe : ")
            champs=[1,id,mdp]
    
            server.send(objecttobytes(champs)) ##Envois les champs nécessaire à la connexion
            
            time.sleep(0.08)
            data = server.recv(2048).decode() ##Attent le retour du serveur à la connexion

            if(data[0]=="0"): ## Si la réponse est correct
                verif = False ## Sort de la boucle de connexion
                client.connected = True ## Etat du client --> Connecté
                print("Connecté")
                return id ## Renvoie le nom du client


## Transforme un objet en bytes encodé pour l'envoie de données
def objecttobytes(object):
    return bytes(str(object).encode())


## Permet de transformer une string en tableau pour le transfert client/server
def strToArray(string):
    data = string[1:len(string)-1].replace(",","").split()
    return data

client = Client(64030,"127.0.0.1")
