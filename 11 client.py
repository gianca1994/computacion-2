# !/usr/bin/python3
import socket
import getopt
import sys

cod_Resp = {200: 'OK', 400: 'Comando válido, pero fuera de secuencia', 500: 'Comando inválido', 404: 'Clave errónea', 405: 'Cadena nula'}

def comm (connect, msg):
    connect.send(msg.encode('ascii'))
    resp = connect.recv(1024).decode('ascii')
    print('Respuesta del server:', resp, '-', cod_Resp.get(resp))

    return int(resp)

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


    checkN = false
    checkE = false
    checkK = false

    while not checkN
        name = 'hello ' + input('Ingrese su nombre: ').replace('', '')
        comm(socket1, name)
        checkN = int(communicate(s, name)) == 200
    while not checkE:
        email = 'email ' + input('Ingrese su email: ')
        comm(socket1, email)
        checkE = int(communicate(s, email)) == 200
    while not checkK:
        key = 'key ' + input('Ingrese la clave: ')
        comm(socket1, key)
        checkK = int(communicate(s, key)) == 200

    print('cerrando conexion...')
    comm(socket1, 'exit')

if __name__ == '__main__':
    main()
