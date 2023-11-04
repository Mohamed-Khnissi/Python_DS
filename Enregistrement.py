
import re

def est_email_valide(email):
    # Utilisation d'une expression régulière pour vérifier la validité de l'email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def est_pwd_valide(pwd):
    # Vérifier si le mot de passe respecte les critères donnés
    return re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$', pwd)

def enregistrer_infos(email, pwd):
    # Vérifier la validité de l'email et du mot de passe
    if not est_email_valide(email):
        print("L'email n'est pas valide.")
        return
    if not est_pwd_valide(pwd):
        print("Le mot de passe ne respecte pas les critères requis.")
        return

    # Enregistrer l'email et le mot de passe dans le fichier
    with open("Enregistrement.txt", "a") as fichier:
        fichier.write(f"Ind. Email: {email}, Pwd: {pwd}\n")
        print("Enregistrement réussi.")

# Demander à l'utilisateur de saisir l'email et le mot de passe
email = input("Entrez l'adresse email : ")
pwd = input("Entrez le mot de passe : ")

# Appeler la fonction d'enregistrement
enregistrer_infos(email, pwd)
