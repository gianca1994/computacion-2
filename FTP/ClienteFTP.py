# !/usr/bin/python3

import getopt, sys, socket, os

from time import sleep

ErrorCode = '500 Error\n\n'
OkCode = '200 OK\n\n'

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
    print('Connected to the FTP server at ip ', host,' and at port ', port)

    # Inicializamos las variables vacias
    command = ''
    comando = ''
    argumento = ''

    # Este bucle se va a repetir siempre hasta que el usuario tipee "exit"
    while True:
        # Spliteo el command con un maximo de 1 split para poder pasar argumentos y comandos
        command = str(input('Message >>> ')).split(maxsplit=1)
        
        # El primer valor del input va a ser el comando
        comando = (command[0])
        # Y en caso de tener mas de 1 valor, entonces tomo como que el segundo valor es el argumento.
        if len(command) > 1: argumento = (command[1])


    # COMANDOS PARA TRABAJAR DE MANERA LOCAL

        # Listamos los archivos en el directorio actual del cliente
        if (comando == 'lss'):
            msg = "\n".join(os.listdir())
            print(f"{OkCode}{msg}")

        # Vemos en que ruta nos encontramos actualmente del cliente
        elif (comando == 'lpwd'):
            print(f'{OkCode}{os.getcwd()}')

        # Nos movemos por las rutas del cliente
        elif (comando == 'lcd'):
            os.chdir(argumento)
            print(f'{OkCode}Ruta actual: "{os.getcwd()}"')


    # COMANDOS PARA TRABAJAR DE MANERA REMOTA CON EL SERVIDOR
       
        # Listamos los archivos en el directorio actual del servidor
        elif command == 'ls':
            Csocket.send(comando.encode())
        
        # Vemos en que ruta nos encontramos actualmente del servidor
        elif command == 'pwd':
            Csocket.send(comando.encode())
        
        # Nos movemos por las rutas del Servidor
        elif (comando == 'cd'):
            comyruta = comando + ' ' + argumento
            print (comyruta)
            #Csocket.send(commandyruta.encode())
        
        # Si el mensaje tipeado es exit, le envio el comando al servidor
        elif (comando == 'exit'):
            Csocket.send(comando.encode())
            answer = Csocket.recv(4096).decode()
            print(answer)
            sys.exit(0)

        else:
            # Enviamos el mensaje del cliente al servidor
            Csocket.send(comando.encode())

            # Desencodeamos la respuesta y la printeamos..
            answer = Csocket.recv(4096).decode()
            print(answer)
    else:
        # Cerramos la conexion
        sys.exit(0)

main()
