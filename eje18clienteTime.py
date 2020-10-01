#!/usr/bin/python

import socket, getopt, sys

# Definimos option_oeading para que el cliente ingrese la ip, el puerto y el tipo de protocolo que va a usar.
def option_reading():

    # Aplicamos el getopt para tomar los 3 argumentos que necesitamos: h(host_servidor_time),p(puerto), t(tcp/udp)
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:t:')

    # Valores por defecto...
    port_svORclient = 37
    protocol_svORclient = 'TCP'
    ip_svORclient = None

    # Si, el numero de opciones ingresados, es menor que 3, entonces...
    if len(opt) < 3:
        print("Error: Expected at least 32 options [-h] [-p] [-t]", len(opt), "received")
        sys.exit(0)

    # Si no, un for para almacenar en las variables "port", "host"  y el "protocolo(tcp o udp)"
    for (opt, arg) in opt:
        if opt == '-h':
            ip_svORclient = arg
        elif opt == '-p':
            port_svORclient = int(arg)
        elif opt == '-t':
            protocol_svORclient = argument.upper() if argument.upper() in ['UDP', 'TCP'] else 'TCP'

    # Si, se comprueba que el host y el puerto no son "None", entonces, nos retorna los mismos
    assert ip_svORclient is not None
    return ip_svORclient, port_svORclient, protocol_svORclient

def outgoing_format(dtime: str) -> str:
    # Creamos la variable msg para almacenar el mensaje que vamos a mandar cuando sea requerido en el main
    msg = 'Fecha y hora actual (UTC): '
    # A las variables date y time, se le almacenara en formato de string, la fecha y hora
    date, time = dtime.split(' ')[1], dtime.split(' ')[2]
    # Le agregamos a la variable msg los valores de date y time y los enviamos.
    msg += date + ' ' + time
    return msg

def main():
    ip_server, port_server, protocol_svORclient = read_options()

    # Si el protocolo es UDP, trabaja sin envios de paquetes, es decir sin conexion, si es TCP, establece conexion con el servidor

    if protocol_svORclient == "UDP":
        # Creamos el socket en UDP "SOCK_DGRAM" enviamos el mensaje encodeado, usando la ip y el puerto
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(''.encode(), (ip_svORclient, port_svORclient))
        # Almacenamos en la variable dtime la fecha y hora actual del servidor y la printeamos...
        dtime = sock.recvfrom(1024)[0].decode()
        # Printeamos el resultado de la funcion, y como parametro, el valor de dtime.
        print(outgoing_format(dtime))

    elif protocol_svORclient == 'TCP':
        # Creamos el socket en TCP "SOCK_STREAM" y establecemos conexion al servidor, usando la ip y el puerto
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_svORclient, port_svORclient))
        # Almacenamos en la variable dtime la fecha y hora actual del servidor y la printeamos...
        dtime = sock.recv(1024).decode()
        # Printeamos el resultado de la funcion, y como parametro, el valor de dtime.
        print(outgoing_format(dtime))

main()
