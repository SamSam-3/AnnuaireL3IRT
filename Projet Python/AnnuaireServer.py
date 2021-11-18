import socket
import threading
import time

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

            time.sleep(0.08) ## Facilite la lecture d'affichage
            data = self.server.recv(2048).decode() ## Recoit le retour du

            if(data == 'fin'):
                self.running = False
                self.server.close()
                print(self.name +" déconnecté")
                server.connectedUsers.remove(self.name) ## Si le server recoit un code, il supprime l'utilisateur de ses ut connectés 

            else:
                print('\nRecu par {}: {}'.format(self.name,data))

                ##Commandes Server
                
                ## Affiche les utilisateurs connectés
                if(data == 'ut'):
                    print(server.connectedUsers)

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
        name = connServer(self.server,resp)

        if(name not in server.connectedUsers):
            self.name = name
            server.connectedUsers.append(name)
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

server = Server(64030,"10.188.14.206")

def connServer(client,data):
    verif = 0
    data = strToArray(data)

    if(data[0]=="0"):
        db = open("dbUtilisateurs.txt",'a')

        for i in data[1:]:
            db.write(i+";")
        db.write("\n")

    else:
        with open("dbUtilisateurs.txt",'r') as db:
            for i in db.readlines():
                id = i.split(";")[0]
                mdp = i.split(";")[1]

                idUt = data[1][1:(len(data[1])-1)]
                mdpUt = data[2][1:(len(data[2])-1)]

                if(id==idUt and mdp==mdpUt and idUt not in server.connectedUsers):
                    time.sleep(0.08)
                    client.send(bytes("0".encode())) ##Confirme que les informations sont correctes
                    verif = 1
                    db.close()
                    return id ## Renvoi le nom de l'utilisateur
                    
            if(verif == 0):
                time.sleep(0.08)
                client.send(bytes("1".encode()))
                client.send(bytes("Mauvaises informations !\n Veuillez réessayer :".encode()))


def strToArray(string):
    data = string[1:len(string)-1].replace(",","").split()
    return data