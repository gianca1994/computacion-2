#!/usr/bin/python

import sys, getopt, socket

def read_options():

    # Declaramos las variables
    address = port = protocol = None
    # Aplicamos el getopt para tomar los 3 argumentos que necesitamos: p(puerto),t(tipo de protocolo) y f(archivo de texto blanco)
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:t:')

    # En caso de recibir mas o menos de 3 argumentos..
    if len(opt) != 3:
        # Se cancela la conexion y sale.
        sys.exit(0)

    # Definimos el array para tomar los 3 argumentos que ingresamos por teclado
    for (option, argument) in opt:
        # El argumento -p para designar el puerto
        if option == '-p':
            port = int(argument)
        # El argumento -t para elegir el tipo de protocolo
        elif option == '-t':
            protocol = argument
        # El argumento -a para designar a la ip que nos conectaremos
        elif option == '-a':
            address = argument
        assert port is not None and address is not None
        assert protocol.upper() in ['TCP', 'UDP']

        # Nos retorna los 3 argumentos que ingresamos
        return address, port, protocol

# Definimos la funcion "read_stdin" para asignar el mensaje que enviara el cliente al servidor
def read_stdin():
    data = ''
    for line in sys.stdin:
        # Guardamos la informacion ingresada en la variable "data" declarada anteriormente
        data = line
    return data

def main():

    address, port, protocol = read_options()

    # Si el protocolo es "TCP":
    if protocol.upper() == 'TCP':
        # Creamos el socket (AF_INET: Una conexion a una red y SOCK_STREAM: Por ser protocolo TCP)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conectamos el socket a la ip y el puerto del servidor
        client_socket.connect((address, port))
        # Nos imprime por pantalla la ip y el puerto al que se conecto (servidor)
        print('Connected to', address, 'on port', port)
        data = read_stdin()
        # Enviamos la infromacion dentro de la variable data y la encodeamos con el metodo "ascii"
        client_socket.send(data.encode('ascii'))

    # Si el protocolo es "UDP":
    elif protocol.upper() == 'UDP':
        # Creamos el socket (AF_INET: Una conexion a una red y SOCK_STREAM: Por ser protocolo UDP)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = read_stdin()
        # Enviamos la infromacion dentro de la variable data y la encodeamos con el metodo "ascii"
        client_socket.sendto(data.encode('ascii'), (address, port))
        # Imprimimos la informacion enviada por el cliente y a la ip que se le envia
        print('Information sent to', address)

main()