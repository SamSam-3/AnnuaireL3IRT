#! /usr/bin/env bash

from Annuaire import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(2)
    
    while(True):
        conn, addr = s.accept()
        print(conn.getpeername())

        if(conn.getpeername() not in utilisateurs):
            utilisateurs.append([conn.getpeername()])
            c = ThreadConnexion(conn)
            c.start()