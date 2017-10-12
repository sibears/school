import shlex
from noteshop.helpers import log


class CommandHandler:
    transport = None  # connection with user

    def __init__(self, applogic):
        self.applogic = applogic  # Application logic

    def exec_command(self, s):
        s = s.replace(".", "")  # Very secure filtering

        # Split "login user pass" into ["login", "user", "pass"]
        command = shlex.split(s)

        # Make "login('user', 'pass')" from ["login", "user", "pass"]
        pyfunc = "self.applogic.{name}({args})".format(name=command[0], args=str(command[1:])[1:-1])

        # log(pyfunc)

        try:
            result = eval(pyfunc)  # Try to exec command
        except Exception as e:
            result = str(e)  # Exception if fails
        finally:
            self.answer(str(result))  # Send result to user as string

    def answer(self, s, end="\n> "):
        self.transport.write((s + end).encode())
