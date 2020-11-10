# !/usr/bin/python3

import getopt, sys

# Definimos option_reading para leer el puerto sobre el cual, el servidor FTP correra.
def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['port='])

    # Si, el numero de modificadores ingresados, es diferente de 1, entonces...
    if len(opt) != 1:
        print("Error: expected 1 option [-p] or [--port] ", len (opt)," received")
        sys.exit(0)

    # Un for para recorrer las optiones
    for (op, arg) in opt:
        if (op in ['-p', '--port']):
            port = int(arg)
        else:
            # Printeamos en caso de que el modificador no sean ni (-p o --port)
            print('Only the -p or --port commands are allowed')
            sys.exit(0)

    # En caso de no ser none la variable
    assert port is not None
    # Sino, retornamos los valores.
    return port

   
def main():

    # Cargamos a las 3 variables, los numeros leidos en el option reading
    port = option_reading()

    print ("El puerto es: ", port)
main()