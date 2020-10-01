#!/usr/bin/python

import getopt, sys, socket, multiprocessing

Commands = ["ABRIR", "CERRAR", "AGREGAR", "y LEER"]

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
        print("Client", connect[0], "connected")
        # Creamos un nuevo proceso targeteando la funcion que se encargara de atender las peticiones del cliente y como arg, el sock(client), bloc, connect
        proc = multiprocessing.Process(target="Falta crear la funcion para atender al cliente con la lista de Commands jeje", args=(csock, bloc, connect[0]))
        # Inicializamos el proceso
        proc.start()

main()
