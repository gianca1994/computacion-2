#!/usr/bin/python

import socket, getopt, sys

# Definimos option_oeading para que el cliente ingrese la ip, el puerto, el tipo de hash y el texto.
def option_reading():

    # Inicializamos las 4 variables como none...
    host = port = texto = hash_function = None

    # Usamos getopt para tomar los 4 argumentos que necesitamos
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:c:h:p:')

    # Si, el numero de opciones ingresados, es menor que 4, entonces...
    if len(opt) < 4:
        print("Error: Expected at least 4 options [-a] [-p] [-c] [-h]", len(opt), "received")
        sys.exit(0)

    # Si no, un for para almacenar en las variables "port", "host", "text" y "hash_function"
    for (opt, arg) in opt:
        if opt == '-a':
            host = arg
        elif opt == '-p':
            port = int(arg)
        elif opt == '-c':
            texto = arg
        elif opt == '-h':
            hash_function = arg

    # Si, se comprueba que host, port, texto, hash_function no son "None", entonces, nos retorna los mismos
    assert (host, port, texto, hash_function) is not None
    return host, port, texto, hash_function


def main():
    # Cargamos los argumentos de cada variable, tomados en el option_reading()
    host, port, texto, hash_function = option_reading()
    # Creamos el socket con protocolo TCP
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectamos el socket con la ip y el puerto ingresados
    socket.connect((host, port))
    # Enviamos el socket con encodeado con el hash que definimos como argumento
    socket.send(hash_function.encode())

    # Almacenamos en la variable la respuesta
    SCode = socket.recv(1024)

    # En caso de que la respuesta del servidor, sea un error 404 entonces: sys.exit...
    if int(SCode.decode()) == 404:
        sys.exit(0)
    # Si no..
    else:
        # Enviamos al servidor, el texto encodeado.
        socket.send(texto.encode())
        hashed = socket.recv(1024).decode()
        print('Valor:', hashed)
main()
