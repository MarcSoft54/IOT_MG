# Coter Client

import socket
import time
import PartirFonction

while True:
    adressIP = input("Veuillez entre une adresse IP ...\n")  # La c'est l'adress IP
    adressPort = input("veuillez entrer le port ...\n")  # La c'est le port de connexion
    while PartirFonction.verificationAdressIp(adressIP) and PartirFonction.portDeConnexion(adressPort):
        print(f"En attente de connexion a l'adresse {adressIP} ....")
        try:
            s = socket.socket()
            s.connect((adressIP, adressPort))
        except:
            print("tentative de connexion echouer ...")
            time.sleep(9)
        else:
            print("conexion reussi ...")
            break
    else:
        print("*****\tVeuillez verifier l'adress de l'un de composants ... \n*****\tEt reassayer ....\n")
