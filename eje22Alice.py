#!/usr/bin/python

import socket, sys

# Primero definimos 2 funciones 1 para escuchar y otra para decir, luego una funcion para entablecer la conexion y un main

def hear(Csocket):

    while True:
        # Alojamos en la variable MsgClient el mensaje desencodeado que se envio desde "ALICE"
        MsgClient = Csocket.recv(1024).decode()

        # Si el mensaje es "Cambio" entonces, se deja de repetir el bucle y BOB escucha desde el proceso ALICE.
        if MsgClient == "CAMBIO":
            break
        # MsgClient == "EXIT", good bye BOB and ALICE
        elif MsgClient == "EXIT":
            sys.exit(0)
        # Printeamos el mensaje de Bob
        print("Bob says: ", MsgClient)


def tell(Csocket):

    while True:
        # Alojamos en la variable MsgServer el mensaje encodeado que va a enviar "ALICE"
        MsgServer = input("").encode()
        # Le enviamos al socket del cliente, el mensaje de ALICE
        Csocket.send(MsgServer)

        # Si el mensaje es "Cambio" entonces, se invierte nuevamente la secuencia.
        if MsgServer.decode() == "CAMBIO":
            break
        # MsgServer == "EXIT", good bye ALICE y BOB
        elif MsgServer.decode() == "EXIT":
            sys.exit(0)

# Definimos AcceptConnection para realizar la conexion entre BOB y ALICE
def AcceptConnection():

    port = 7666

    # Creamos el socket con protocolo TCP
    Ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Ssocket.bind(("", port))
    # Definimos la ip local sobre el cual vamos a correr el servidor, o Alice
    IpLocalServer = socket.gethostbyname(socket.getfqdn())

    print("alice is online with ip: ", IpLocalServer, " and port: ", port)

    # Dejamos el socket de Alice escuchando
    Ssocket.listen(1)
    # Aceptamos la conexion entre bob y alice
    Csocket, IPclient = Ssocket.accept()
    # Retornamos los 2 sockets
    return Ssocket, Csocket


def main():
    # Establecemos conexion entre los 2 socket, tanto cliente como servidor.
    Ssocket, Csocket = AcceptConnection()

    while True:
        hear(Csocket)
        tell(Csocket)

main()