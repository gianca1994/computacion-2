# !/usr/bin/python3

import getopt, sys, socket, signal, multiprocessing, os, time

ErrorCode = '500 Error\n\n'
OkCode = '200 OK\n\n'
 # Aca lo que hacemos es traer la IPV4, que seria la ip local del servidor usando el metodo "gethostbyname"
ipv4 = socket.gethostbyname(socket.getfqdn())

# Definimos option_reading para leer el puerto sobre el cual, el servidor FTP correra.
def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['port='])

    # Si, el numero de modificadores ingresados, es diferente de 1, entonces...
    if len(opt) != 1:
        print("Error: expected 1 option [-p] or [--port] ", len (opt)," received")
        sys.exit(0)

    # Un for para recorrer las optiones
    for (op, arg) in opt:
        if (op in ['-p', '--port']):
            # Si el argumento pasado como puerto es diferente a todos los puertos de la lista
            if int(arg) > 1000:
                port = int(arg)
            # Si no, mostramos el error y la lista de puertos que no pueden ser ingresados
            else:
                print(f'\nThe port entered is reserved, enter another port...')
                sys.exit(0)    
        else:
            # Printeamos en caso de que el modificador no sean ni (-p o --port)
            print('Only the -p or --port commands are allowed')
            sys.exit(0)

    # En caso de no ser none la variable
    assert port is not None
    # Sino, retornamos los valores.
    return port
    
# Definimos la funcion clientint para recibir los comandos del cliente, un Handler
def clientint(Csocket, host):
    # El bucle while para que te deje ingresar diferentes comandos hasta que ingreses "exit"
    while True:
        # Desencodeamos el mensaje del cliente y entramos a la cadena de ifs.
        command = Csocket.recv(2048).decode()

        # Listamos los archivos del directorio actual y le enviamos el listado al cliente
        if command == 'ls':
            msg = "\n".join(os.listdir())
            Csocket.send((OkCode + msg).encode())

        # Guardamos en la variabl msg, el mensaje OK, el codigo y la ruta actual del servidor y se la enviamos al cliente
        elif command == 'pwd':
            msg = OkCode + os.getcwd()
            Csocket.send(msg.encode())
        
    #    elif command == 'cd':
    #        msg = OkCode + os.getcwd()
    #        os.chdir(msg)
    #        sleep(1)
    #        Csocket.send(msg.encode())
            
        # Lista de comandos posibles a realizar en el serverFTP
        elif command == 'help':
            Csocket.send(('Comandos disponibles:\n'
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

        # PREGUNTAR AL PROFE, PORQUE ESTA EJECUCION LA HAGO EN EL CLIENTE...
        # Si ingresa el comando exit, le enviamos al cliente el mensaje bye y cerramos la conexion.
        elif command == 'exit':
            print(OkCode)
            Csocket.send(('connection closed!').encode())
            break

        else:
            Csocket.send('It is not a valid command, to know the list of possible commands, type "help" and press enter'.encode())

    # Si el while deja de ser true, se cierra el socket (close conections)
    print('Client', host, 'disconnected')
    Csocket.close()

# Definimos la funcion para cerrar el servidor
def ClosedServer():
    # Mostramos por consola del ServidorFTP que el servidor se ha cerrado.
    print("Server connection lost")
    # Cerramos el servidor
    sys.exit(0)
   
def main():

    # Declaramos el "Manejador de señales" para el cierre del servidor
    signal.signal(signal.SIGINT, ClosedServer)
    # Cargamos a la variables, los numeros leidos en el option reading
    port = option_reading()

    # Creamos el socket (AF_INET: Una conexion a una red y SOCK_STREAM: Por ser protocolo TCP)
    Ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectamos el socket al servidor, atravez de la ip y el puerto
    Ssocket.bind(('', port))
    # Imprimimos en la consola del servidor, la IP local y el puerto que designamos en el argumento de -p o --port
    print("Server turned on with ip ", ipv4, " and the port ", port, " (waiting for interaction)")


    while True:
        Ssocket.listen(16)
        # Aceptamos el socket y le informamos al servidor que se conecto un cliente con la ip "host"
        Csocket, host = Ssocket.accept()
        print('\nGot a connection from', host)

        # Declaramos la variable y le decimos que targetee la funcion clientint y traiga las IPV4 de los clientes...
        multiproces = multiprocessing.Process(target=clientint, args=(Csocket, host))
        # Iniciamos el multi-proceso
        multiproces.start()


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