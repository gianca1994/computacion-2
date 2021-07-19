class Printer:

    @staticmethod
    def server_running(ipv4, port):
        print(f"Server turned on with ip {ipv4} and the port {port} (waiting for interaction)")

    @staticmethod
    def connection_of(client_address):
        print(f'\nGot a connection from {client_address}')

    @staticmethod
    def client_disconect(client_address):
        print(f'Client {client_address} disconnected')

    @staticmethod
    def finished_server():
        print("Server connection lost")

    @staticmethod
    def reserved_port():
        print('The port entered is reserved, enter a port greater than 1000.')

    @staticmethod
    def bad_options_input(options):
        print(f"Error: expected 1 option [-p] or [--port] {len(options)} received")

    @staticmethod
    def allowed_commands():
        print('Only the -p or --port commands are allowed')
