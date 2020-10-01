#!/usr/bin/python

import getopt, sys, socket, multiprocessing

Commands = ["ABRIR", "CERRAR", "AGREGAR", "LEER"]

def reading_port():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:')

    # En caso de que la opcion sea diferente de 1, imprimos el mensaje...
    if len(opt) != 1:
        raise getopt.GetoptError("You are required to enter (-p) and then as an argument, the port.")

    # Sino, le asignamos a la variable port, el argumento proporcionado
    port = int(opt[0][1])

    # En caso de ser un puerto menor a 1, retornamos error.
    if port < 1:
        raise ValueError
    return port

def read_client(csock, bloq, ip_client):
    # Inicializamos las variables como none, para luego ser redimencionadas
    name_file = None
    open_file = None
    # Le enviamos al cliente en el socket, el mensaje con los comandos que puede ejecutar.
    csock.send(('Enter any of the following commands: "ABRIR", "CERRAR", "AGREGAR", "LEER", to perform the operation you want\n').encode())

    while True:
        # Desencodeamos el socket y lo almacenamos en la variable commands para luego ser comparado en los if/elif..
        commands = csock.recv(256).decode()
        commands = commands.upper().strip()

        if commands == 'ABRIR':
            # Le enviamos al cliente el mensaje.
            csock.send('Enter the name of the file you want to open:'.encode())
            # Recibimos la respuesta con el nombre del archivo, la desencodeamos y la almacenamos en la variable.
            name_file = csock.recv(256).decode()
            # Abrimos un nuevo archivo para escribir. "a" == Agrega datos al final del archivo.
            open_file = open(name_file, 'a')

        elif commands == 'CERRAR':
            # Si el comando ingresado es CERRAR, entonces, enviamos el mensaje encodeado en el socket y cerramos el archivo..
            csock.send('Connection closed, see you later!\n'.encode())
            open_file.close()

        elif commands == 'AGREGAR':
            # Enviamos el socket con el mensaje
            csock.send('Enter the message you want to ADD to the file:\n'.encode())
            # Desencodeamos la respuesta del usuario
            user_string = csock.recv(256).decode()
            bloq.acquire()
            # Escribimos el archivo
            open_file.writelines(user_string)
            # Y flusheamos el archivo.
            open_file.flush()
            bloq.release()

        elif commands == 'LEER':
            # Lo que hacemos es abrir el archivo con open y 'r' para indicar que es read, es decir, que lo vamos a leer solamente..
            with open(name_file, 'r') as read_file:
                # En la variable file_content, adjuntamos todas las lineas que tenga el archivo
                file_content = str(read_file.read()) + '\n'
                # Enviamos el contenido del archivo encodeado en el socket..
                csock.send(file_content.encode())
        else:
            # Si el comando ingresado no es ninguno de los anteriores aceptados...
            csock.send(('Command not allowed, you must use "OPEN", "CLOSE", "ADD" or "READ"\n').encode())

        # Cerramos la conexion con el cliente..
        csock.close()

def main():
    # Le seteamos a la variable port, el puerto ingresado en la funcion reading_port
    port = reading_port()
    # Creamos el socket en TCP "SOCK_STREAM" y establecemos conexion al servidor, usando la ip y el puerto
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Asocia el socket con el puerto indicado
    ssock.bind(('', port))
    # Iniciamos el servidor con la ip correspondiente al servidor (gethostbyname)
    ip_server = socket.gethostbyname(socket.getfqdn())
    print('Server online: ', ip_server, ' port: ', port)
    bloc = multiprocessing.Lock()

    while True:
        # El socket del sv queda escuchando...
        ssock.listen(32)
        # El socket del servidor es aceptado cuando un cliente se conecta...
        csock, connect = ssock.accept()
        print(connect[0], " connected")
        # Creamos un nuevo proceso targeteando la funcion que se encargara de atender las peticiones del cliente y como arg, el sock(client), bloc, connect
        proc = multiprocessing.Process(target=read_client, args=(csock, bloc, connect[0]))
        # Inicializamos el proceso
        proc.start()

main()
