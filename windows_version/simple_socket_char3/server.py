import socketserver

# Global variables
PORT = 50000     # Port No
BUFSIZE = 4096   # Buffer size

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def setup(self):
        pass

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(BUFSIZE)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data)

    def finish(self):
        pass

if __name__ == '__main__':
    # not a local environment, the IP address of the server.
    HOST = 'localhost' # HOST = 'IP address of the server'

    # Allow the port to be reused
    socketserver.TCPServer.allow_reuse_address = True

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('Keyboard Interrupt')
        pass
