import time
from copy import copy

from service.crypto import CryptoEngine


class Secret(object):
    def __init__(self, owner, secret, password):
        self.owner = owner
        self.secret = CryptoEngine.encrypt(secret, password)
        self.timestamp = time.gmtime()

    def __lt__(self, other):
        return self.timestamp.__lt__(other.timestamp)

    def decrypt(self, password):
        cp = copy(self)
        cp.secret = CryptoEngine.decrypt(self.secret, password)
        return cp


class SecretStorage(object):
    def __init__(self):
        self.secrets = []

    def get_secrets_for(self, user):
        res = []
        for s in self.secrets:
            if s.owner.name == user.name:
                res.append(s)
        return res

    def add_secret(self, user, secret):
        s = Secret(user, secret, user.password)
        self.secrets.append(s)

    def get_last_secrets(self, n=10):
        return list(sorted(self.secrets[-n:]))

    def decrypt_message(self, owner, message):
        return CryptoEngine.decrypt(message, owner.password)