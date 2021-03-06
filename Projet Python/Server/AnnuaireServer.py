import socket
import threading
import time
import os


class Server():
    def __init__(self,port,host):
        self.connectedUsers = []
        self.port = port
        self.host = host
        self.socket = ""

class ReceptionServer(threading.Thread):

    def __init__(self, server,name):
        threading.Thread.__init__(self)
        self.running = True
        self.server = server
        self.name = name

    def run(self): ## C'est encore un peu buggué, je corrigerai ca plus tard
        while(self.running):
            with open("{}/Annuaire.txt".format(self.name),'r+') as annuaire:
                
                time.sleep(0.08) ## Facilite la lecture d'affichage
                data = self.server.recv(2048).decode() ## Recoit le retour du client

                ##Si le client coupe la connexion
                if(data == 'fin'): 
                    self.running = False
                    annuaire.close()
                    self.server.close()
                    print(self.name +" déconnecté")
                    server.connectedUsers.remove(self.name) ## Si le server recoit un code, il supprime l'utilisateur de ses ut connectés 

                else:
                    print('\nRecu par {}: {}'.format(self.name,data))

                    ##Commandes Server

                    ## Affiche les utilisateurs connectés
                    if(data == 'ut'):
                        self.server.send(objecttobytes(server.connectedUsers)) ##Envoie la liste des utilisateurs connectés

                    elif(data == 'ajouter'):
                        a=0 ## A faire

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
        code = connServer(self.server,resp) ##Récupère son 

        if(code == 200): ## Si la création du code est correct
            resp = self.server.recv(1024).decode() ##
            code = connServer(self.server,resp)

        if(code not in server.connectedUsers):
            self.name = code
            server.connectedUsers.append(self.name)
            self.startServer()

    def startServer(self):
        with self.server:
            r = ReceptionServer(self.server, self.name)
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
            exit(0)

def connServer(client,data):
    verif = 0
    data = strToArray(data)

    if(data[0]=="0"):
        db = open("dbUtilisateurs.txt",'a')
        
        if(not alreadyExist(data[1])):
            for i in data[1:]:
                db.write(i+";")
            db.write("\n")

            os.system("mkdir {}".format(data[1])) ## Crée le dossier du client
            os.system("touch {}/Annuaire.txt".format(data[1])) ## Lui construit un annuaire
            client.send(bytes("Vous possédez maintenant un compte !\n".encode()))
        else:
            client.send(bytes("Vous possédez déjà un compte !".encode()))
        
        return 200

    else:
        with open("dbUtilisateurs.txt",'r') as db:
            for i in db.readlines():
                id = i.split(";")[0]
                mdp = i.split(";")[1]

                idUt = data[1]
                mdpUt = data[2]

                if(id==idUt and mdp==mdpUt and idUt not in server.connectedUsers):
                    time.sleep(0.08)
                    client.send(objecttobytes(0)) ##Confirme que les informations sont correctes
                    verif = 1
                    return id ## Renvoi le nom de l'utilisateur
                    
            if(verif == 0):
                time.sleep(0.08)
                client.send(objecttobytes(1))
                client.send(objecttobytes("Mauvaises informations ! Veuillez réessayer :"))
            db.close()






##Transforme un objet en bytes encodé pour l'envoie au client
def objecttobytes(object):
    return bytes(str(object).encode())

## Transforme une string en tableau
def strToArray(string):
    data = string[1:len(string)-1].replace(",","").split()
    array=[data[0]]
    for i in data[1:]:
        array.append(i[1:(len(i)-1)])

    return array

## Verifie si l'utilisateur existe déjà dans la db
def alreadyExist(id):
    db = open("dbUtilisateurs.txt",'r')

    for i in db.readlines():
        if(id in i):
            return True
    return False

server = Server(64030,"127.0.0.1")
