
class Secret(object):
    def __init__(self, owner, secret):
        self.owner = owner
        self.secret = secret
        self.id = None

    def __cmp__(self, other):
        return cmp(self.id, other.id)


class SecretStorage(object):
    def __init__(self):
        self.last_id = 1
        self.secrets = {}

    def get_secrets_for(self, user):
        res = []
        for s in self.secrets.itervalues():
            if s.owner.name == user.name:
                res.append(s)
        return res

    def secret_by_id(self, id):
        if id in self.secrets:
            return self.secrets[id]
        return None

    def add_secret(self, user, secret):
        s = Secret(user, secret)
        s.id = self.last_id
        self.secrets[s.id] = s
        self.last_id += 1
