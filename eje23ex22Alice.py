#!/usr/bin/python

import socket, sys , threading
from datetime import dtime

def attend(Csocket, n, bloq):

    # En la variable Datime alojamos, la fecha y la hora
    Datime = dtime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Abrimos el archivo "eje23ex19_LOG.txt" en el directorio "etc_23"
    with open("etc_23/eje23ex22Alice_LOG.txt", "a") as file_LOG:
        bloq.acquire()
        # Alojamos el nombre del hilo en la variabl
        Threading = threading.current_thread().name
        # Escribimos en el archivo los logs, tanto de la fecha y hora que se ejecuto, y el nombre del hilo que atendio a bob
        file_LOG.write(f"[{Datime}] Bob was taken care of by the thread: {Threading}\n")
        # Arrancamos el bloqueo
        bloq.release()

    # Un while para:
    while True:
        # Escuchar
        hear(Csocket, n)
        # Decir
        tell(Csocket, n)


def hear(Csocket, n):

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
        print("Bob says ", {n}, ":", MsgClient)


def tell(Csocket, n):

    while True:
        # Alojamos en la variable MsgServer el mensaje encodeado que va a enviar "ALICE"
        MsgServer = input(f"Bob {n}:").encode()
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
    # n = cantidad de bobs o cliente que se conectan
    n = 1; port = 7666

    # Creamos el socket con protocolo TCP
    Ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Asociamos el socket con la ip y el puerto
    Ssocket.bind(('', port))
    # Definimos la ip local sobre el cual vamos a correr el servidor, o Alice
    IpLocalServer = socket.gethostbyname(socket.getfqdn())
    bloq = threading.Lock()
    print("Alice is online with ip: ", IpLocalServer, " and port: ", port)
    # El socket del servidor, queda esperando una conexion
    Ssocket.listen(16)

    while True:
        # Aceptamos la conexion
        Csocket, IpClient = Ssocket.accept()
        print(IpClient, " conected...")

        # Creamos la variable threading targeteando la funcion attend
        threading = threading.Thread(target=attend, args=(Csocket, n, bloq))
        threading.start()
        # Informamos que se arranco un nuevo hilo
        print(f"Start a new thread: {threading.name} for bob {n}")
        n += 1

main()