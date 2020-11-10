# !/usr/bin/python3

import getopt, sys, socket

# Definimos option_reading para leer el puerto sobre el cual, el servidor FTP correra.
def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:', ['host=', 'port='])

    # Si, el numero de modificadores ingresados, es diferente de 1, entonces...
    if len(opt) != 2:
        print("Error: expected at least 2 options: ([-h] or [--host] and [-p] or [--port]) ", len (opt)," received")
        sys.exit(0)

    # Un for para recorrer las optiones
    for (op, arg) in opt:
        if (op in ['-h', '--host']):
            host = arg
        elif (op in ['-p', '--port']):
            port = int(arg)  
        else:
            # Printeamos en caso de que el modificador no sean ni (-p o --port) para el puerto, ni (-h o --hots) para la ip
            print('Only the commands "-h" or "--host" are allowed for the ip and "-p" or "--port" for the port')
            sys.exit(0)

    # En caso de no ser none la variable
    assert (host, port) is not None
    # Sino, retornamos los valores.
    return host, port


def main():

    # Cargamos a las 2 variables, los numeros leidos en el option reading
    host, port = option_reading()
    # Creamos el socket que usaremos para comunicar el cliente con el servidor
    Csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectamos el cliente al servidor FTP y le printeamos la ip el puerto al cual fue conectado.
    Csocket.connect((host, port))
    print('Connected to remote shell at', host, 'on port', port)

    # Inicializamos la variable vacia
    command = ''

    # Este bucle se va a repetir siempre y cuando el mensaje no sea "exit"
    while command != 'exit':
        command = str(input('Msg>>> '))
        # Enviamos el mensaje del cliente al servidor
        Csocket.send(command.encode())
        # Desencodeamos la respuesta y la printeamos..
        answer = Csocket.recv(4096).decode()
        print(answer)
    else:
        # Cerramos la conexion
        sys.exit(0)

main()