import secret
import users


class SecretService:
    def __init__(self):
        self.storage = secret.SecretStorage()
        self.user_manager = users.UserManager()

    def login(self, username, password):
        user = self.user_manager.get_by_name(username)
        if user is None:
            return None
        if not user.check_password(password):
            return None
        return SecretClient(self, user)

    def register_student(self, username, password):
        user = users.User(username, password)
        self.user_manager.add_user(user)
        return user


class SecretClient:
    def __init__(self, service, logged_user):
        self.service = service
        self.user = logged_user

    def add_secret(self, secret):
        self.service.storage.add_secret(self.user, secret)

    def get_secret(self, id):
        return self.service.storage.secret_by_id(id)

    def list_users(self, limit=10, offset=0):
        all_users = self.service.user_manager.list_users()
        return sorted(all_users, reverse=True)[offset:offset+limit]

    def list_records(self, limit=10, offset=0):
        all_records = self.service.storage.get_secrets_for(self.user)
        return sorted(all_records, reverse=True)[offset:offset + limit]
