import logging
import socket
import threading
from hashlib import md5

from service import interface
from service import service


class Server:
    def __init__(self, host="0.0.0.0", port=1453):
        logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)-15s %(message)s')

        self.service = service.LegionService()
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(50)
        logging.info('[Server] Started on %s:%s', self.host, self.port)
        while True:
            clientsock, addr = self.sock.accept()
            logging.info('[Server] Accepted connection from %s', addr)
            cthread = Client((clientsock, addr), self.service)
            cthread.start()


class Client(threading.Thread):
    def __init__(self, client, service):
        threading.Thread.__init__(self)
        self.sock, self.addr = client
        self.service = service
        self.welcome = interface.WELCOME
        self.client_ctx = None

    def run(self):
        try:
            self.print_message(self.welcome)
            while True:
                cmd = self.get_command()
                self.process_command(cmd)
        except Exception as e:
            if str(e) != 'exit':
                logging.error('[CLIENT %s] Got exception "%s"', self.addr, e)
        finally:
            logging.info('[CLIENT %s] Has gone', self.addr)
            self.sock.close()

    def get_command(self, prompt=interface.PROMPT):
        if prompt:
            self.print_message(prompt)
        ans = self.sock.recv(100500).decode()
        if len(ans) > 1:
            return ans[0]
        return ans

    def get_answer(self, prompt=interface.PROMPT):
        if prompt:
            self.print_message(prompt)
        ans = self.sock.recv(100500).decode()
        return ans.rstrip()

    def print_message(self, msg):
        self.sock.send(msg.encode())

    def println_message(self, msg):
        self.print_message(msg + "\n")

    def process_command(self, cmd):
        if self.client_ctx is None:
            self._process_unprivileged(cmd)
        else:
            self._process_privileged(cmd)

    def _process_unprivileged(self, cmd):
        if cmd == '0':
            raise Exception("exit")
        elif cmd == '1':
            self._register()
        elif cmd == '2':
            self._login()
        elif cmd == '3':
            self._last_secrets()
        elif cmd == '?':
            self.print_message(self.welcome)
        elif cmd == '':
            raise Exception("exit")
        else:
            self.println_message("Unknown command! Type '?' for help")

    def _login(self):
        name = self.get_answer("Say your name, private: ")
        password = self.get_answer("Now say your secret legion name: ")
        ctx = self.service.look_for_legionary(name, password)
        if ctx is None:
            self.println_message("Are you trying to fool me?!")
            return
        if ctx.user.is_centurion:
            self.welcome = interface.CENTURION_WELCOME.format(ctx.user.name)
        else:
            self.welcome = interface.USER_WELCOME.format(ctx.user.name)
        self.print_message(self.welcome)
        self.client_ctx = ctx

    def _register(self):
        name = self.get_answer("Say your name, private: ")
        password = self.get_answer("Now say your secret legion name: ")
        try:
            if name.startswith('Centurion'):
                self._register_centurion(name, password)
                return
            self.service.join_legion(name, password)
        except Exception as e:
            logging.error('[CLIENT %s] Got exception "%s"', self.addr, e)
            self.println_message("You aren't looking like {}".format(name))
            return
        self.println_message("Huh! Welcome to the LEGION, private!")

    def _register_centurion(self, name, password):
        self.println_message("Can't recognize you, sir! Can you tell me the secret word?")
        secret = self.get_answer("Secret word: ").encode()
        if md5(secret).hexdigest() != 'bc5cb2d611ee8956b9daeb2beebc7544':
            raise Exception("Traitor!")
        self.service.join_legion(name, password)
        self.println_message("Oh! My lord! How could I not recognize you?! Ave LEGION!")

    def _last_secrets(self):
        self.println_message("LEGION use the most modern ciphers " +
                             "so all our military reports are absolutely safe!")
        self.println_message("Ensure it by yourself:")
        secrets = self.service.list_latest_reports()
        self.println_message(interface.stringify_reports(secrets))

    def _process_privileged(self, cmd):
        if cmd == '?':
            self.print_message(self.welcome)
        elif cmd == '0':
            self.println_message("You successfully ran away")
            self.welcome = interface.WELCOME
            self.client_ctx = None
        elif self.client_ctx.user.is_centurion:
            self._process_centurion(cmd)
        elif cmd == '1':
            self._list_records()
        elif cmd == '2':
            self._add_record()
        elif cmd == '3':
            self._get_record()
        else:
            self.println_message("Unknown command! Type '?' for help")

    def _list_records(self):
        records = self.client_ctx.list_reports()
        self.println_message(interface.stringify_reports(records))

    def _get_record(self):
        message = self.get_answer("Enter encrypted message: ")
        message = self.client_ctx.decrypt_report(message)
        self.println_message("That's what we can read: {}".format(message))

    def _add_record(self):
        secret = self.get_answer("Enter your secret: ")
        self.client_ctx.save_report(secret)
        self.println_message("Success!")

    def _list_users(self):
        users = self.client_ctx.list_legionaries()
        self.println_message(interface.stringify_users(users))

    def _process_centurion(self, cmd):
        if cmd == '1':
            self._list_users()
        else:
            self.println_message("Unknown command! Type '?' for help")
