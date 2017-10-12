from noteshop.helpers import Singleton
from prettytable import PrettyTable

CURRENCY = "bearcoins"  # We accept only our cool currency. Because we can!

HELP = """
register <login> <password> - Register a new user
login <login> <password> - Login with given credentials

(if logged in)
list - List all notes (without secrets, ofc)
list self - List my own notes (with secrets)
add <text> <price> <secret> - Add note to shop
buy <id> - Buy note with given id
balance - View current balance

If you want to pass argument with spaces or special symbols, escape it or quote with " or '
""".strip()

WELCOME="""
Welcome to Note Shop! That shop was developed for easy note trading. 
You can buy a lot of secret information here and sell your own secrets.
""".strip()

DEBUG_KEY = 288 ^ 576 + 666


class AppLogic:
    def __init__(self):
        self.user = None
        self.db = CoolDB()  # best practice ever!

    def welcome_message(self):
        return WELCOME + "\n\nAvailable commands:\n" + self.help()  # bad practice ever :(

    def help(self):
        return HELP

    def register(self, login, password):
        if login not in self.db.users:
            self.db.users[login] = {"login": login, 
                                     "password": password, 
                                     "balance": 0}
            return "OK, now you can log in via 'login <login> <password>'"
        else:
            return "Error: User already exists"

    def login(self, login, password):
        if login not in self.db.users:
            return "User doesn't exists, can't log in"
        elif password in self.db.users[login]["password"]:  # TODO: improve security of comparer
            self.setUser(self.db.users[login])
            return "Successfully logged in, type 'help' for help (cap?)"
        else:
            return "Invalid password"

    def add(self, text, price, secret):
        if not self.user:
            return "Please log in"
        else:
            CoolDB().notes[len(self.db.notes)] = {
                "id": len(CoolDB().notes),
                "author": self.user["login"], 
                "text": text, 
                "price": int(price), 
                "secret": secret
            }
            return "Success"

    def buy(self, id):
        note = self.db.notes[int(id)]
        if self.user["balance"] < note['price']:
            return "Not enough money"
        else:
            self.user["balance"] -= note['price']
            self.db.users[note["author"]]["balance"] += note['price']
            return "Thank you, note secret is: %s" % note["secret"]

    def balance(self):
        return "Your balance: %s %s" % (self.user["balance"], CURRENCY)

    def list(self, filter=""):
        if not self.user:
            return "Please log in"
        else:
            display_notes = {}
            if filter == "self":
                # display only user notes with secrets
                for id, note in self.db.notes.items():
                    if note["author"] == self.user['login']:
                        display_notes[id] = note
                return self.prettify_notes(display_notes, show_secrets=True)
            elif filter == "":
                # display all notes without secrets
                return self.prettify_notes(self.db.notes, show_secrets=False)
            else:
                return "Unknown filter %s!" % filter

    # That's not a command, just helper!
    def prettify_notes(self, notes, show_secrets=False):
        if self.user.get("god", False):
            show_secrets = True
        t = PrettyTable([
            'ID', 
            'Author', 
            'Text', 
            'Price', 
            'Secret (if provided)'
        ])
        for _, note in notes.items():
            t.add_row([
                note["id"],
                note["author"],
                note["text"],
                "%d %s" % (note["price"], CURRENCY),
                note["secret"] if show_secrets else "-"
            ])
        return str(t)

    # Another cool login helper
    def setUser(self, user):
        self.user = user

    # For tests only! Please don't use in production!
    def godmode(self, activate):
        if not self.user:
            return "Please log in"
        if int(activate)^123456 == DEBUG_KEY:
            self.user['god'] = True
            return "[god_mode]=on"
        else:
            self.user['god'] = False
            return "[god_mode]=off"

# High available in-memory database with native python api and pretty easy schema migration (SIGKILL)
class CoolDB(metaclass=Singleton):
    users = {
        "admin": {  # The only database which provide you in-code examples!
            "login": "admin", 
            "password": "changeme", 
            "balance": 10000
        }
    }
    notes = {}

    def __str__(self):  # Very cool and simple database serializator
        return str(self.users) + str(self.notes)
