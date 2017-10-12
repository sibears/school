from service import secret
from service import users


class LegionService:
    def __init__(self):
        self.storage = secret.SecretStorage()
        self.user_manager = users.UserManager()

    def look_for_legionary(self, username, password):
        user = self.user_manager.get_by_name(username)
        if user is None:
            return None
        if not user.check_password(password):
            return None
        return Legionary(self, user)

    def join_legion(self, username, password):
        user = users.User(username, password)
        self.user_manager.add_user(user)
        return user

    def list_latest_reports(self):
        return self.storage.get_last_secrets(10)


class Legionary:
    def __init__(self, service, logged_user):
        self.service = service
        self.user = logged_user

    def save_report(self, secret):
        self.service.storage.add_secret(self.user, secret)

    def decrypt_report(self, message):
        return self.service.storage.decrypt_message(self.user, message)

    def list_legionaries(self):
        all_users = self.service.user_manager.list_users()
        return list(sorted(all_users))

    def list_reports(self, limit=10, offset=0):
        all_records = self.service.storage.get_secrets_for(self.user)
        return sorted(all_records, reverse=True)[offset:offset + limit]
