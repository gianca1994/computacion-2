#!/usr/bin/python

import sys, getopt, socket, signal

# Definimos la funcion "port", encargada de leer  el puerto que ingresamos al abrir el servidor
def portarg():
    # Le decimos que con la opcion "-p" el siguiente argumento, sera el puerto por el cual correra el servidor.
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:')
    port = int(opt[0][1])
    return port

# Definimos la funcion "clientint" para realizar las interacciones con el cliente, los pedidos
def clientint(clientsock, address):
    while True:
        # Aplicamos el metodo ".recvfrom" vamos a recibir la informacion y con el (1024 caracteres que puede recibir)
        com = clientsock.recv(1024)

        # Con el if lo que hacemos es desencodear el mensaje enviado por el cliente
        if com.decode('ascii') == 'disconect':
            break
    # Y se cierra el socket del cliente..
    clientsock.close()

# Definimos la funcion para cerrar el servidor
def exitserv(s, frame):
    # Mostramos por consola que el servidor se ha cerrado.
    print("Server connection lost")
    # Cerramos el servidor
    sys.exit(0)

# Definimos "main" para realizar la funcion
def main():
    # Declaramos el "Manejador de señales" para el cierre del servidor
    signal.signal(signal.SIGINT, exitserv)

    # Aca lo que hacemos es traer la IPV4, que seria la ip local del servidor usando el metodo "gethostbyname"
    ipv4 = socket.gethostbyname(socket.getfqdn())
    # En la variable port, alojamos el port ingresado en el argumento
    port = portarg()
    # Creamos el socket (AF_INET: Una conexion a una red y SOCK_STREAM: Por ser protocolo TCP)
    sockserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectamos el socket al servidor, atravez de la ip y el puerto
    sockserv.bind(('', port))
    # Imprimimos en la consola del servidor, la IP local y el puerto que designamos en el argumento de -p
    print("server turned on with ip ", ipv4, " and the port ", port, " (waiting for interaction)")

    # El bucle while esta para poder realizar multiples insercciones de comandos
    while True:
        sockserv.listen(16)
        clientsock, address = sockserv.accept()
        # Nos imprime por consola la IP, del cliente que se conecto
        print("A client connected with the ip: ", address)

main()