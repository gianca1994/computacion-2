import getopt
import multiprocessing
import signal
import socket
import sys

from commands import Commands
from constants import ResponseCode
from printer import Printer

printer = Printer()
commands = Commands()
ipv4 = socket.gethostbyname(socket.getfqdn())


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['port='])

    if len(opt) != 1:
        printer.bad_options_input(opt)
        sys.exit(0)

    for (op, arg) in opt:
        if op in ['-p', '--port']:
            if int(arg) > 1000:
                port = int(arg)
            else:
                printer.reserved_port()
                sys.exit(0)
        else:
            printer.allowed_commands()
            sys.exit(0)

    assert port is not None
    return port


def clientint(client_socket, client_address):
    while True:

        argument = ''

        request = client_socket.recv(2048).decode().split()
        command = (request[0])

        if len(request) > 1: argument = (request[1])

        if command == 'ls':
            client_socket.send(commands.ls().encode())

        elif command == 'pwd':
            client_socket.send(commands.pwd().encode())

        elif command == 'cd':
            client_socket.send(commands.cd(argument).encode())

        elif command == 'put':

            archive = open(argument, 'wb')
            content = client_socket.recv(1024)

            while content:
                print("Receiving...")
                archive.write(content)
                content = client_socket.recv(1024)

            archive.close()
            print("Done Receiving")
            client_socket.send('Thank you for connecting')

        #            msg = OkCode + os.getcwd()
        #            client_socket.send(msg.encode())

        elif command == 'help':
            client_socket.send(('Comandos disponibles:\n'
                                'pwd                Retorna el directorio actual del servidor (comando remoto)\n'
                                'lpwd               Retorna el directorio actual del cliente (comando local)\n'
                                'cd /ruta/          Cambia la ruta actual en el servidor (comando remoto)\n'
                                'lcd /ruta/         Cambia la ruta actual en el cliente (comando local)\n'
                                'ls                 Lista el contenido del directorio en el servidor.\n'
                                'Lls                Lista el contenido del directorio en el cliente.\n'
                                'get filename       Permite descargar un archivo remoto desde el servidor al cliente.\n'
                                'put filename       Permite subir un archivo local desde el cliente al servidor.\n'
                                'exit               Cierra la conexión con el servidor y termina el cliente.\n'
                                'help               Muestra esta ayuda.'
                                ).encode())

        elif command == 'exit':
            client_socket.send('connection closed!'.encode())
            break

        else:
            client_socket.send(ResponseCode.COMMAND_FAIL.encode())

    printer.client_disconect(client_address)
    client_socket.close()


def ClosedServer(client_socket):
    printer.finished_server()
    client_socket.close()
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, ClosedServer)

    port = option_reading()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))

    printer.server_running(ipv4, port)

    while True:
        server_socket.listen(16)
        client_socket, client_address = server_socket.accept()

        multiprocessing.Process(target=clientint, args=(client_socket, client_address)).start()
        printer.connection_of(client_address)


if __name__ == '__main__':
    try:
        main()
    except getopt.GetoptError as e:
        print(e)
    except ConnectionRefusedError:
        print('Error: Connection refused')
    except socket.error:
        print('Failed to create a socket')
    except Exception as e:
        print(e)
