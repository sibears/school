from time import strftime
from prettytable import PrettyTable

LOGO = """\
       .---.        .-----------
      /     \  __  /    ------ S
     / /     \(  )/    -----   P
    //////   ' \/ `   ---      Q
   //// / // :    : ---        R
  // /   /  /`    '--
 //          //..\\
            '//||\\`
              ''``
"""

WELCOME = """\
Welcome here, legionary! What does yoy annoy me for?
0. Run away
1. I want to join the LEGION!
2. Hey, did you forget me, corporal?
3. Show me how safe are your secrets.
"""

USER_WELCOME = LOGO + """\
Hello {}! What you wanted to do?
0. Disguise yourself
1. List your military reports
2. Report new information
3. Decrypt report
"""

CENTURION_WELCOME = LOGO + """\
Ave {}! Can we do something for you?
0. Disguise yourself
1. Show me the LEGION, corporal!
"""

PROMPT = "> "


def stringify_reports(secrets):
    t = PrettyTable(['Owner', 'Protected Report', 'Delivered At'])
    for s in secrets:
        t.add_row([
            s.owner.name,
            s.secret,
            strftime("%a, %d %b %Y %H:%M:%S", s.timestamp),
        ])
    return str(t)


def stringify_users(users):
    t = PrettyTable(['Name', 'Password Hash', 'Joined At'])
    for u in users:
        t.add_row([
            u.name,
            u.password,
            strftime("%a, %d %b %Y %H:%M:%S", u.register_time),
        ])
    return str(t)

