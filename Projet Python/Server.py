from AnnuaireServer import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: ## Server principal    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.socket = s

    s.bind((server.host, server.port))
    s.listen(2) ## recoit 2 personnes maximum
    print("En attente d'une connection ...")

    while(True): ## Attend à l'infini
        conn, addr = s.accept() ## Attend une connexion client
        time.sleep(0.08) ## Evite la coupure de connexion
        c = ThreadConnexion(conn)
        c.start()