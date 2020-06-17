#!/usr/bin/python

import sys, getopt, socket

def read_options():

    # Declaramos las variables
    port = protocol = file_path = None

    # Aplicamos el getopt para tomar los 3 argumentos que necesitamos: p(puerto),t(tipo de protocolo) y f(archivo de texto blanco)
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:t:f:')

    # En caso de recibir mas o menos de 3 argumentos..
    if len(opt) != 3:
        # Se cancela la conexion y sale.
        sys.exit(0)

    # Con el array tomamos los 3 argumentos que ingresamos por teclado
    for (option, argument) in opt:
        # El argumento -p para designar el puerto
        if option == '-p':
            port = int(argument)
        # El argumento -t para elegir el tipo de protocolo
        elif option == '-t':
            protocol = argument
        # El argumento -f para el nombre y la ubicacion del archivo
        elif option == '-f':
            file_path = argument
    assert port is not None and file_path is not None
    assert protocol.upper() in ['TCP', 'UDP']

    # Nos retorna los 3 argumentos que ingresamos
    return port, protocol, file_path

# Definimos "main" para realizar las funciones que se realizaran en base a si se eligio el protocolo TCD o UDP
def main():

    port, protocol, file_path = read_options()
    data = ''

    # Si el protocolo es "TCP":
    if protocol.upper() == 'TCP':
        # Creamos el socket (AF_INET: Una conexion a una red y SOCK_STREAM: Por ser protocolo TCP)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conectamos el socket al servidor, atravez de la ip y el puerto
        server_socket.bind(('', port))
        # Ponemos el socket en modo escucha (3) escucha 3 clientes...
        server_socket.listen(3)
        # Aceptamos al cliente
        client_socket = server_socket.accept()
        # Aplicamos el metodo ".recvfrom" vamos a recibir la informacion y con el (1024 caracteres que puede recibir), maximo 1 socket
        data, client_address = client_socket[0].recv(1024), client_socket[1]
        # Cerramos la coneccion con el cliente
        client_socket[0].close()

    # Si es "UDP" entonces:
    elif protocol.upper() == 'UDP':
        # Creamos el socket (AF_INET: Una conexion a una red y SOCK_DGRAM: Por ser protocolo UDP)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Conectamos el socket al servidor, atravez de la ip y el puerto
        server_socket.bind(('', port))
        # Aplicamos el metodo ".recvfrom" vamos a recibir la informacion y con el (1024 la cantidad de caracteres que puede recibir)
        data, client_address = server_socket.recvfrom(1024)
        # Cerramos la coneccion con el servidor
        server_socket.close()

    # Abrimos el archivo en el cual escribiremos...
    with open(file_path, 'w') as file:
        # Escribimos el archivo y lo decodificamos con el metodo "ascii"
        file.write(data.decode('ascii'))
        # Imprimimos la informacion que fue recibida por: "cliente" y almacenada en: "ruta donde se almacena el archivo + nombre del archivo"
        print('Information received by', client_address, 'and stored in', file_path)
main()