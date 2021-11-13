#! /usr/bin/env bash

from Annuaire import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: ## Server principal
    s.bind((host, port))
    s.listen(2) ## recoit 2 personnes maximum

    while(True): ## Attend à l'infini
        conn, addr = s.accept() ## Attend une connexion client
        time.sleep(0.08) ## Evite la coupure de connexion
        c = ThreadConnexion(conn)
        c.start()

print("GIT ON TENCULE")