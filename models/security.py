class Security:
    def __init__(self, name, can_recv=False, can_send=False, can_create=False, can_modify=False, can_encrypt=False, can_decrypt=False):
        self.name = name
        self.can_recv = can_recv
        self.can_send = can_send
        self.can_create = can_create
        self.can_modify = can_modify
        self.can_encrypt = can_encrypt
        self.can_decrypt = can_decrypt


admin = Security("Admin", True, True, True, True, True, True)
member = Security("Member", True, True, False, False, True, True)
secs = [admin, member]


def get_by_name(name):
    if admin.name == name:
        return admin
    elif member.name == name:
        return member