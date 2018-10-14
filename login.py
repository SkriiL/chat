from models.user_model import User
from services.user_service import get_all
import os


def login():
    username = input("Nutzername: ")
    all_users = get_all()
    picked_user = User()
    for user in all_users:
        if user.get_username() == username:
            picked_user = user
    if picked_user == 0:
        print("Nutzer existiert nicht, bitte erneut versuchen!")
        login()
    for i in range(0, 3):
        password = input("Passwort: ")
        if picked_user.get_password_decrypted() == password:
            os.system("cls")
            print("Login erfolgreich! \n")
            return picked_user
        else:
            print("Falsches Passwort, bitte erneut versuchen")
    exit()