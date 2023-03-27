def verificationAdressIp(Adress):  # une adresse IP est sous la forme 170.0.0.1
    newAdress = Adress.split(".")
    if len(newAdress) < 4 or len(newAdress) > 4:  # verifions d'abord si elle est longue genre de 4 nombre au max et min
        return False
    for i in newAdress:  # ici verifions si se sont les chiffres
        try:
            IP = int(i)
            if len(i) > 3:
                return False
        except:
            return False  # au cas contraire sa nous renvoie un False
    return True  # si tout se passe bien alors on n'as un True



def portDeConnexion(port):  # verification du port
    try:
        p = int(port)
        return True
    except:
        return False
