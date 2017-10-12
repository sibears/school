import asyncio
from noteshop.network import ShopProtocol
from noteshop.commandhandler import CommandHandler
from noteshop.applogic import AppLogic

def protocol_factory(): 
    return ShopProtocol(CommandHandler(AppLogic()))

loop = asyncio.get_event_loop()

# Each client connection will create a new protocol instance
coro = loop.create_server(protocol_factory, '0.0.0.0', 2505)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
