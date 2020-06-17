#!/usr/bin/python3

import getopt, sys, socket

def read_options():

    # Declaramos las variables
    address = port = file = None
    # Aplicamos el getopt para tomar los 3 argumentos que necesitamos: p(puerto),t(tipo de protocolo) y f(archivo de texto blanco)
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:t:')

    # En caso de recibir mas o menos de 3 argumentos..
    if len(opt) < 2:
        # Se cancela la conexion y sale.
        sys.exit(0)

    # Definimos el array para tomar los 3 argumentos que ingresamos por teclado
    for (option, argument) in opt:

        # El argumento -a para designar a la ip que nos conectaremos
        if option == '-a':
            address = argument
        # El argumento -p para designar el puerto
        elif option == '-p':
            port = int(argument)
        # El argumento -t para la ruta del archivo
        elif option == '-t':
            file = argument
            assert port is not None and address is not None
    # Nos retorna los 3 argumentos que ingresamos
    return address, port, file

def main():
    address, port, file = read_options()

    # Creamos el socket (AF_INET: Una conexion a una red y SOCK_STREAM: Por ser protocolo TCP)
    clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectamos el socket a la ip y el puerto del servidor
    clientsock.connect((address, port))

    # Nos imprime por pantalla la ip y el puerto al que se conecto (servidor)
    print("Successful shell connection with ip", address,"and the port",port)
    # Nos da el mensaje, de que debemos tipear para cortar la conexion con el servidor...
    print("type (disconnect) to end the connection")
    # Declaramos la variable
    com = ""

    # Declaramos la variable disconect
    disconect = None
    # Si, lo ingresado anteriormente es "disconect", then
    if com != disconect:
        # Tomamos el comando ingresado luego de ">>>" y lo almacenamos en la variable.
        com = str(input(">>>"))
        # Encodeamos el comando y lo enviamos al servidor
        clientsock.send(com.encode("ascii"))
        # Recibimos la respuesta del servidor y lo desencodeamos
        fast_answer = clientsock.recv(2048).decode("ascii")
        # Dicha respuesta la mostramos por pantalla
        print(fast_answer)
    # Si no:
    else:
        # Cerramos la conexion
        sys.exit(0)
main()