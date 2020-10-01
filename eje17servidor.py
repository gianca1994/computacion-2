# !/usr/bin/python3

import multiprocessing, sys, getopt, socket, signal

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


def inverted_chain(string: str) -> str:
    return string[::-1]

# Definimos la funcion para atender las peticiones del cliente y le pasamos como parametros el sock del cliente y la ip.
def read_client(csock):
    while True:
        # Desencodeamos el mensaje proveniente del cliente
        msg = csock.recv(2048).decode()

        # En caso de que el mensaje que tipeo el cliente sea "exit"
        if msg == 'exit':
            # Le enviamos al cliente el mensaje
            csock.send('-> see you later!'.encode())
            break

        # Le enviamos al cliente la respuesta encodeada..
        csock.send(('-> ' + inverted_chain(msg)).encode())

    # Cerramos el socket del cliente y cortamos la conexion con el.
    csock.close()


# Definimos serverexit para cortar la coneccion del servidor
def closed_sv(s, frame):
    print('\nConnection finished...')
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, closed_sv)

    # Alojamos en la variable port, el puerto leido en la funcion "reading_port"
    port = reading_port()

    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.bind(('', port))
    print('Server online: ', socket.gethostbyname(socket.getfqdn()), ' port: ', port)

    while True:
        ssock.listen(16)

        #Aceptamos el socket
        csock, address = ssock.accept()
        # Le informamos que se recibio la conexion desde la ip "adress"
        print('\nConnection of ', address, "Approved!!")

        # Creamos un nuevo proceso, targeteando a la funcion read_client y traemos como argumentos, el socket del cliente y su ip.
        new_process = multiprocessing.Process(target=read_client, args=(csock, address))
        # Corremos el nuevo proceso
        new_process.start()

main()