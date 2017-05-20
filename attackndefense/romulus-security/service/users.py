import time
from base64 import b85encode as hashpwd


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if self.get_by_name(user.name) is not None:
            raise Exception("User exists!")
        user.register_time = time.gmtime()
        if user.name.strip().startswith('Centurion'):
            user.is_centurion = True
        else:
            user.is_centurion = False
        self.users.append(user)

    def list_users(self):
        return self.users

    def get_by_name(self, user_name):
        for u in self.users[::-1]:
            if u.name == user_name:
                return u
        return None


class User(object):
    def __init__(self, name, passwd):
        self.name = name
        self.password = hashpwd(passwd.encode()).decode()
        self.register_time = time.gmtime()

    def check_password(self, passwd):
        return hashpwd(passwd.encode()).decode() == self.password

    def __lt__(self, other):
        return self.register_time.__lt__(other.register_time)
