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
    u.set_security(sec.secs[which - 1].name)
    save_user(u)
    return u


def save_user(user):
    params = (user.get_id(), user.get_username(), user.get_password(), user.get_mail(), user.get_security())
    conn = sqlite3.connect("db.db")
    c = conn.cursor()
    c.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?)", params)
    conn.commit()
    conn.close()


def get_single(id):
    params = (id,)
    conn = sqlite3.connect("db.db")
    c = conn.cursor()
    c.execute("SELECT FROM user WHERE id=?", params)
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
