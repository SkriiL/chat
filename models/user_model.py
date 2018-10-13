import functions.encryption as encrypt
import functions.decryption as decrypt

class User:
    def __init__(self):
        self.id = 0
        self.username = ""
        self.password = ""
        self.mail = ""
        self.security = object

    def set_id(self, id):
        self.id = id

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_password_encrypt(self, password):
        self.password = encrypt.full_encrypt(password)

    def set_mail(self, mail):
        self.mail = mail

    def set_security(self, security):
        self.security = security

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_password_decrypted(self):
        return decrypt.full_decrypt(self.password)

    def get_mail(self):
        return self.mail

    def get_security(self):
        return self.security