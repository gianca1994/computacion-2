#!/usr/bin/python

import socket, sys, getopt

def hear(Csocket):

    while True:
        # Alojamos en la variable MsgServer el mensaje desencodeado que se envio desde "BOB"
        MsgServer = Csocket.recv(1024).decode()

        # Si el mensaje es "Cambio" entonces, se deja de repetir el bucle y ALICE escucha desde el proceso de BOB.
        if MsgServer == "CAMBIO":
            break
        # MsgClient == "EXIT", good bye BOB and ALICE
        elif MsgServer == "EXIT":
            sys.exit(0)
        # Printeamos el mensaje de ALICE
        print("Alice says: ", MsgServer)


def tell(Csocket):

    while True:
        # Alojamos en la variable MsgClient el mensaje encodeado que va a enviar "BOB"
        MsgClient = input("").encode()
        # Le enviamos el socket del cliente, con el mensaje de BOB
        Csocket.send(MsgClient)

        # Si el mensaje es "Cambio" entonces, se invierte nuevamente la secuencia.
        if MsgClient.decode() == "CAMBIO":
            break
        # MsgClient == "EXIT", good bye BOB and ALICE
        elif MsgClient.decode() == "EXIT":
            sys.exit(0)

# Definimos AcceptConnection para realizar la conexion entre BOB y ALICE
def AcceptConnection():

    # GetOpt para que bob ingrese la ip de Alice, solo ip, porque el puerto es una variable constante
    opt, arg = getopt.getopt(sys.argv[1:], "m:")

    # Declaramos la ip y puerto del servidor
    IpLocalServer = opt[0][1]
    port = 7666

    # Creamos el socket con protocolo TCP
    Csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectamos el socket de Bob con la ip y el puerto del servidor
    Csocket.connect((IpLocalServer, port))
    return Csocket


def main():
    # Establecemos conexion entre los 2 socket, tanto cliente como servidor.
    Csocket = AcceptConnection()

    while True:
        hear(Csocket)
        tell(Csocket)

main()