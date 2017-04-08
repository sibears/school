from time import strftime
from prettytable import PrettyTable

WELCOME = """\
Hello in the SImple StOrage System!
Please select what you wanted to do:
1. Sign IN
2. Sign UP
3. Exit
"""

USER_WELCOME = """\
Hello {}! What you wanted to do?
0. Logout
1. List your records
2. Get secret by ID
3. Add new secret
4. List registered users
"""

PROMPT = "> "


def stringify_secrets(secrets):
    t = PrettyTable(['ID', 'Owner', 'Secret'])
    for s in secrets:
        t.add_row([
            s.id,
            s.owner.name,
            s.secret,
        ])
    return str(t)


def stringify_users(users):
    t = PrettyTable(['Name', 'Joined at'])
    for u in users:
        t.add_row([
            u.name,
            strftime("%a, %d %b %Y %H:%M:%S", u.register_time),
        ])
    return str(t)

