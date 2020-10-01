# !/usr/bin/python3

import getopt, socket, sys

# Definimos option_oeading para que el cliente ingrese la ip y el puerto para conectarse con el servidor..
def option_reading():

    # Primero, inicializamos las variables que usaremos para la ip y puerto como "none", osea ningun valor asignado.
    ip_server = port_server = None

    # Aplicamos el getopt para tomar los 2 argumentos que necesitamos: h(ip),p(puerto)
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:')

    # Si, el numero de opciones ingresados, es menor que 2, entonces...
    if len(opt) < 2:
        print("Error: Expected at least 2 options [-h] [-p]", len(opt), "received")
        sys.exit(0)

    # Si no, un for para almacenar en las variables "port" y "host" los valores ingresados como argumentos de (-p y -h)
    for (opt, arg) in opt:
        if opt == '-h':
            ip_server = arg
        elif opt == '-p':
            port_server = int(arg)

    # Si, se comprueba que el host y el puerto no son "None", entonces, nos retorna los mismos
    assert ip_server is not None and port_server is not None
    return ip_server, port_server


def main():
    # Alojamos en las variables ip y port, los valores de la funcion "option_reading"
    ip, port = option_reading()

    # Creamos un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectamos el socket con la ip y el puerto argumentado en la funcion "option_reading"
    sock.connect((ip, port))
    print('Connection with the server, established !!, To end the connection, type the command "exit".')
    msg = ''

    # En un while, si el msg escrito es diferente de "exit"
    while msg != 'exit':
        # Entonces...
        msg = str(input('>> '))
        # Enviamos el mensaje encodeado
        sock.send(msg.encode())
        # Desencodeamos la respuesta y la imprimimos en consola..
        answer = sock.recv(4096).decode()
        print(answer)

main()