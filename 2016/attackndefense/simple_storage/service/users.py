import time


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        user.register_time = time.gmtime()
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
        self.password = passwd
        self.register_time = time.gmtime()

    def check_password(self, passwd):
        # inner bruteforce protection
        for given, expected in zip(passwd, self.password):
            if given != expected:
                return False
            time.sleep(0.1)
        return True

    def __cmp__(self, other):
        return cmp(self.register_time, other.register_time)
