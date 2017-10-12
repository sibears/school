import logging
import socket
import threading

import interface
import service


class Server:
    def __init__(self, host="0.0.0.0", port=31337):
        logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)-15s %(message)s')

        self.service = service.SecretService()
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(50)
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
        ans = self.sock.recv(100500)
        if len(ans) > 1:
            return ans[0]
        return ans

    def get_answer(self, prompt=interface.PROMPT):
        if prompt:
            self.print_message(prompt)
        ans = self.sock.recv(100500)
        return ans.strip()

    def print_message(self, msg):
        self.sock.send(msg)

    def println_message(self, msg):
        self.sock.send(msg + "\n")

    def process_command(self, cmd):
        if self.client_ctx is None:
            self._process_unprivileged(cmd)
        else:
            self._process_privileged(cmd)

    def _process_unprivileged(self, cmd):
        if cmd == '1':
            self._login()
        elif cmd == '2':
            self._register()
        elif cmd == '3':
            raise Exception("exit")
        elif cmd == '?':
            self.print_message(self.welcome)
        elif cmd == '':
            raise Exception("exit")
        else:
            self.println_message("Unknown command! Type '?' for help")

    def _login(self):
        name = self.get_answer("Enter your name: ")
        password = self.get_answer("Enter your password: ")
        ctx = self.service.login(name, password)
        if ctx is None:
            self.println_message("Wrong name and/or password!")
            return
        self.welcome = interface.USER_WELCOME.format(ctx.user.name)
        self.print_message(self.welcome)
        self.client_ctx = ctx

    def _register(self):
        name = self.get_answer("Enter your name: ")
        password = self.get_answer("Enter your password: ")
        try:
            self.service.register_student(name, password)
        except Exception as e:
            print e
            self.println_message("User already exists!")
            return
        self.println_message("User successfully registered! Now you can login.")

    def _process_privileged(self, cmd):
        if cmd == '1':
            self._list_records()
        elif cmd == '2':
            self._get_record()
        elif cmd == '3':
            self._add_record()
        elif cmd == '4':
            self._list_users()
        elif cmd == '0':
            self.println_message("You successfully logged out")
            self.welcome = interface.WELCOME
            self.client_ctx = None
        elif cmd == '?':
            self.print_message(self.welcome)
        else:
            self.println_message("Unknown command! Type '?' for help")

    def _list_records(self):
        records = self.client_ctx.list_records()
        self.println_message(interface.stringify_secrets(records))

    def _get_record(self):
        id = self.get_answer("Enter secret ID: ")
        secret = self.client_ctx.get_secret(int(id))
        if secret is None:
            self.println_message("No such secret!")
        else:
            self.println_message(interface.stringify_secrets([secret]))

    def _add_record(self):
        secret = self.get_answer("Enter your secret: ")
        self.client_ctx.add_secret(secret)
        self.println_message("Success!")

    def _list_users(self):
        users = self.client_ctx.list_users()
        self.println_message(interface.stringify_users(users))
