""" 
BYU DRAGN Lab Server's Client
By: Nathan Tibbetts
July 2020
"""

import socket
import json
import struct
from sys import argv

# KEYWORDS   = ["PRINT", "RETURN", "EXCEPTION", "SHUTDOWN", "RESTART", "LIST", "PING", "DOCS", "CONSTANTS"]
DEFAULT_PORT = 40404
DEFAULT_IP   = u"0.0.0.0" # or "localhost"
DEFAULT_URL  = u"{}.cs.byu.edu"
DEFAULT_HOST = u"deckard"

# Ensure some extra string backwards compatibility for Python 2
# NOTE: Even if the client is run in Python 2, we're always communicating
#   with the server via unicode.
try:
    # Python 2: "unicode" is built-in
    unicode
except NameError:
    unicode = str



# --------------------------------------------------------------------------
# The Client, and user relevant functions

def run(module_name, function_name=None, *args, **kwargs):
    return Client().run(module_name, function_name, *args, **kwargs)

def run_on(server_name, module_name, function_name=None, *args, **kwargs):
    return Client(server_name).run(module_name, function_name, *args, **kwargs)

class Client:
    """ A client program for DRAGNServer, the DRAGN Lab Server."""

    def __init__(self, host_name=DEFAULT_HOST, address=None, port=DEFAULT_PORT):
        """ NOTE: Server and client switch dynamically between the given port
            and a secondary, +1 incremented port number, in case of restarting."""
        # Initialization
        if address is None: address = DEFAULT_URL.format(host_name)
        self.server_address = (address, port)
        self.backup_address = (address, port+1)
        self.use_backup_address = False
        print(u"Connecting to server at: {}".format(self.server_address))

        # See if server is available
        try:
            self.run(u"PING")
        except:
            pass


    def run(self, module_name, function_name=None, *args, **kwargs):
        if '.' in module_name:
            if function_name is not None:
                args = [function_name] + list(args)
            module_name, function_name = module_name.split('.')
            # The above should allow "anaphora", "coref" or "anaphora.coref"

        # Set up the socket to be the same type as the server
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = self.backup_address if self.use_backup_address else self.server_address
        try:
            client_sock.connect(address)    # Attempt to connect to the server.
        except:
            address = self.server_address if self.use_backup_address else self.backup_address
            print(u"Trying other port, {}".format(address[1]))
            try:
                client_sock.connect(address)
                self.use_backup_address = not self.use_backup_address
            except Exception as e:
                print(u"Server unavailable")
                raise e # TODO: maybe remove later

        # Print server info if not ping
        if module_name != u"PING":
            print(u"Sending request to DRAGN Lab Server on: {}".format(
                socket.gethostbyaddr(address[0])[0]))

        # Send data from the client to the server
        _send_msg(client_sock, [module_name, function_name, args, kwargs])

        if module_name != u"PING":
            print(u"Awaiting responses from server:")
        while True:
            # Wait to receive a response back from the server.
            tag, value = _recv_msg(client_sock)

            if tag == u"SHUTDOWN" or tag == u"RESTART": print(tag)
            elif module_name != u"PING": print(value)
            if tag != u"PRINT": break

        # Close the client socket
        client_sock.close()

        # Return Value (Means task was successfully completed)
        if tag == u"RETURN":
            return value

    def shutdown_server(self):
        """ Command to shut down the server. """
        self.run(u"SHUTDOWN")

    def restart_server(self):
        """ Command to restart the server. """
        self.run(u"RESTART")

    def list_modules(self):
        """ Command to list the server's available modules. """
        self.run(u"LIST")

    def list_functions(self, module_name):
        """ Command to list the functions found in the server's given module."""
        self.run(u"LIST", module_name)

    def list_constants(self, module_name):
        """ Command to list the constants defined in the server's given module."""
        self.run(u"LIST", module_name, u"CONSTANTS")

    def get_docs(self, module_name, function_name=None):
        """ Command to retrieve docs for a given server module or function."""
        if function_name is None: self.run(u"DOCS", module_name)
        else: self.run(u"DOCS", module_name, function_name)

    def pull_server(self):
        """ Command for the server to do a Git pull to update the local modules."""
        self.run(u"PULL")

    def ping(self):
        """ Command to ping the server for connectivity."""
        self.run(u"PING")


# --------------------------------------------------------------------------
# These functions allow us to send and receive variable sized messages
#   in various formats

class Encoder(json.JSONEncoder):
    def default(self, o):
        try:
            return o.tolist()
        except:
            try:
                return list(iter(o))
            except:
                return unicode(o)

def _send_msg(sock, obj):
    # JSON pack it
    # try:
    msg = json.dumps(obj, cls=Encoder).encode()
    # except:
    #     msg = json.dumps([obj[0], unicode(obj[1])]).encode()

    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def _recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = _recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]

    # Read the message data
    msg = _recvall(sock, msglen)

    # Un-JSON pack it
    return json.loads(msg.decode(encoding='UTF-8'))

def _recvall(sock, n):
    # Helper function to recv n bytes or return None if nothing to receive
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
# --------------------------------------------------------------------------


# Script Behavior, for testing if a server is running:
if __name__ == "__main__":
    c = Client(*argv[1:]) if len(argv) > 1 else Client()
    c.ping() # This should error out if no server, process returning nonzero.