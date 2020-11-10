# !/usr/bin/python3

import getopt, sys

# Agregado, lista de los principales puertos TCP reservados
PortsTCP_Reserved = [
    21, 22, 23, 25, 53, 80, 101, 110, 143, 443, 445, 587, 591,  853, 990, 993, 995, 1194, 1723,
    1812, 1813, 2049, 2082, 2083, 3074, 3306, 3389, 4662, 4672, 4899, 5000,
    5400, 5500, 5600, 5700, 5800, 5900, 6881, 6969, 8080, 51400, 25565]

# Definimos option_reading para leer el puerto sobre el cual, el servidor FTP correra.
def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:', ['host=', 'port='])

    # Si, el numero de modificadores ingresados, es diferente de 1, entonces...
    if len(opt) != 2:
        print("Error: expected at least 2 options: ([-h] or [--host] and [-p] or [--port]) ", len (opt)," received")
        sys.exit(0)

    # Un for para recorrer las optiones
    for (op, arg) in opt:
        if (op in ['-h', '--host']):
            host = arg
        elif (op in ['-p', '--port']):
            # Un for para recorrer la lista de puertos reservados...
            for portReserved in PortsTCP_Reserved:
                # Si el argumento pasado como puerto es diferente a todos los puertos de la lista
                if int(arg) != portReserved:
                    port = int(arg)
                # Si no, mostramos el error y la lista de puertos que no pueden ser ingresados
                else:
                    print(f'\nThe port entered is reserved, enter another that is not in this list:\n{PortsTCP_Reserved}\n')
                    sys.exit(0)    
        else:
            # Printeamos en caso de que el modificador no sean ni (-p o --port) para el puerto, ni (-h o --hots) para la ip
            print('Only the commands "-h" or "--host" are allowed for the ip and "-p" or "--port" for the port')
            sys.exit(0)

    # En caso de no ser none la variable
    assert (host, port) is not None
    # Sino, retornamos los valores.
    return host, port

def main():

    # Cargamos a las 3 variables, los numeros leidos en el option reading
    host, port = option_reading()

    print(f'La ip es: {host} y el puerto es: {port}')
main()