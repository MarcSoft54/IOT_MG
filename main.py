import socket

adressIP = "175.0.0.1"
adressPort = 32000
try:
    s = socket.socket()
    s.connect((adressIP, adressPort))
    print("conexion reussi ...")
except:
    print("echec de connexion ...")



