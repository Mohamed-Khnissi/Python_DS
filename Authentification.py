import hashlib

# Fonction pour vérifier les informations d'authentification
def authentification(email, pwd):
    with open("Enregistrement.txt", "r") as fichier:
        for ligne in fichier:
            if f"Ind. Email: {email}, Pwd: {pwd}" in ligne:
                return True
    return False

# Fonction pour enregistrer un nouveau compte
def enregistrer_compte(email, pwd):
    with open("Enregistrement.txt", "a") as fichier:
        fichier.write(f"Ind. Email: {email}, Pwd: {pwd}\n")

# Fonction pour hacher un mot en utilisant SHA-256
def hacher_mot(mot):
    hashed = hashlib.sha256(mot.encode()).hexdigest()
    return hashed

# Fonction pour le chiffrement César
def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    for caractere in message:
        if caractere.isalpha():
            majuscule = caractere.isupper()
            caractere = chr(((ord(caractere) - 65 + decalage) % 26) + 65 if majuscule else ((ord(caractere) - 97 + decalage) % 26) + 97)
        message_chiffre += caractere
    return message_chiffre

# Fonction pour collecter une dataset fictive
def collecter_dataset():
    # Ajoutez ici le code pour collecter votre dataset fictive
    pass

# Menu principal
while True:
    print("Menu principal:")
    print("1. Authentification")
    print("2. Enregistrement")
    choix = input("Choisissez une option (1/2) : ")

    if choix == "1":
        email = input("Email : ")
        pwd = input("Mot de passe : ")

        if authentification(email, pwd):
            print("Authentification réussie. Accès au menu.")

            while True:
                print("Menu:")
                print("A. Donnez un mot à hacher")
                print("B. Décalage par César")
                print("C. Collecter une Dataset de votre choix")
                print("Q. Quitter")

                sous_choix = input("Choisissez une option (A/B/C/Q) : ")

                if sous_choix == "A":
                    mot = input("Entrez le mot à hacher : ")
                    hashed = hacher_mot(mot)
                    print(f"Mot haché (SHA256) : {hashed}")

                elif sous_choix == "B":
                    mot = input("Entrez le mot à chiffrer : ")
                    decalage = int(input("Entrez le décalage : "))
                    message_chiffre = chiffrement_cesar(mot, decalage)
                    print(f"Message chiffré : {message_chiffre}")

                elif sous_choix == "C":
                    collecter_dataset()
                    print("Dataset collectée et prête à être utilisée.")

                elif sous_choix == "Q":
                    break

        else:
            print("L'authentification a échoué. Veuillez vous enregistrer.")

    elif choix == "2":
        email = input("Email : ")
        pwd = input("Mot de passe : ")
        enregistrer_compte(email, pwd)
        print("Compte enregistré avec succès.")

    else:
        print("Option non valide. Choisissez 1 pour authentification ou 2 pour enregistrement.")
