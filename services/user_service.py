from models.user_model import User
import random
import sqlite3
import models.security_model as sec
import os


def new_user():
    u = User()
    u.set_id(random.randint(1, 999))
    u.set_username(input("Nutzername: "))
    u.set_password_encrypt(input("Passwort: "))
    u.set_mail(input("Mail: "))
    for i in range(len(sec.secs)):
        print(str(i + 1) + " | " + sec.secs[i].name)
    which = int(input("Wählen sie eine Sicherheitsstufe: "))
    u.set_security(sec.secs[which - 1])
    save_user(u)
    print("Nutzer erstellt.")
    return u


def save_user(user):
    params = (user.get_id(), user.get_username(), user.get_password(), user.get_mail(), user.get_security().name)
    conn = sqlite3.connect("db.db")
    c = conn.cursor()
    c.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?)", params)
    conn.commit()
    conn.close()


def delete_user(id):
    params = (id, )
    conn = sqlite3.connect("db.db")
    c = conn.cursor()
    c.execute("DELETE FROM user WHERE id=?", params)
    conn.commit()
    conn.close()


def modify_user(user):
    print("1 | Nutzername \n"
          "2 | Passwort \n"
          "3 | Mail \n"
          "4 | Security")
    choice = input("Was möchten sie bearbeiten?")
    if choice == "1":
        print("Aktueller Nutzername: " + user.get_username())
        new = input("Neuer Nutzername: ")
        user.set_username(new)
    elif choice == "2":
        print("Aktuelles Password: " + user.get_password())
        new = input("Neues Password: ")
        user.set_password(new)
    elif choice == "3":
        print("Aktuelle Mail: " + user.get_mail())
        new = input("Neue Mail: ")
        user.set_mail(new)
    elif choice == "4":
        print("Aktuelle Sicherheitsstufe: " + user.get_security().name)
        for i in range(len(sec.secs)):
            print(str(i + 1) + " | " + sec.secs[i].name)
        which = int(input("Wählen sie eine Sicherheitsstufe: "))
        user.set_security(sec.secs[which - 1].name)
    if input("Wollen sie noch etwas bearbeiten? (j | n) ").lower() == "j":
        modify_user(user)
    else:
        delete_user(user.get_id())
        save_user(user)
        print("Bearbeitung abgeschlossen.")


def print_ids():
    users = get_all()
    for user in users:
        print(str(user.get_id()) + " | " + user.get_username())


def get_single(id):
    params = (id,)
    conn = sqlite3.connect("db.db")
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE id=?", params)
    user = c.fetchone()
    user = list_to_user(user)
    conn.close()
    return user


def get_all():
    conn = sqlite3.connect("db.db")
    c = conn.cursor()
    c.execute("SELECT * FROM user")
    users = c.fetchall()
    for i in range(0, len(users)):
        users[i] = list_to_user(users[i])
    return users


def list_to_user(user_list):
    u = User()
    u.set_id(user_list[0])
    u.set_username(user_list[1])
    u.set_password(user_list[2])
    u.set_mail(user_list[3])
    u.set_security(sec.get_by_name(user_list[4]))
    return u
