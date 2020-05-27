# !/usr/bin/python3
import socket
import getopt
import sys

def comm (connect, msg):
    connect.send(msg.encode('ascii'))
    resp = connect.recv(1024).decode('ascii')
    print('Respuesta del server:', resp)

socket1 = socket.socket()

def main():

    host = ''
    port = ''

    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:')

    for (op, ar) in opt:
            if (op == '-h'):
                print("host =", ar)
                host = (ar)
            elif (op == '-p'):
                print("port =", ar)
                port = int(ar)

    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    assert host,port is not none

    socket1.connect((host,port))

    name = 'hello |' + input ('Ingrese su nombre: ').replace('','')
    comm(socket1, name)
    email = 'email |' + input('Ingrese su email: ')
    comm(socket1, email)
    key = 'key |' + input('Ingrese la clave: ')
    comm(socket1, key)

    print('cerrando conexion...')
    comm(socket1, 'exit')

if __name__ == '__main__':
    main()
