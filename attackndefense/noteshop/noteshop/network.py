import asyncio

class ShopProtocol(asyncio.Protocol):
    def __init__(self, commandhandler):
        self.commandhandler = commandhandler

    def connection_made(self, transport):
        self.commandhandler.transport = transport
        self.commandhandler.exec_command("welcome_message")

    def data_received(self, data):
        message = data.decode()
        self.commandhandler.exec_command(message)
