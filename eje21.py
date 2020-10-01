#!/usr/bin/python

import sys, getopt


def option_reading():

    # Aplicamos el getopt para tomar los argumentos que necesitamos
    (opt, arg) = getopt.getopt(sys.argv[1:], 's:', ['pac1=', 'pac2=', 'med1=', 'med2='])

    # Valores por defecto...
    pactiemp_min, pactiemp_max = (1,3)
    medtiemp_min, medtiemp_max = (5,7)
    consulting_rooms = 5

    # Si, el numero de opciones ingresados, es menor que 3, entonces...
    if len(opt) < 5:
        print("Error: Expected at least 5 options 's:', ['pac1=', 'pac2=', 'med1=', 'med2='] ")
        sys.exit(0)

    if int(arg) > 0
        # Si no, un for para almacenar en las variables "cant_process", "cant_iterations"  y el "name_file"
        for (opt, arg) in opt:
            if opt == '--pac1':
                pactiemp_min = int(arg)
            elif opt == '--pac2':
                pactiemp_max = int(arg)
            elif opt == '--med1':
                medtiemp_min = int(arg)
            elif opt == '--med1':
                medtiemp_max = int(arg)
            elif opt == '-s':
                consulting_rooms = int(arg)

        return (pactiemp_min, pactiemp_max), (medtiemp_min, medtiemp_max), consulting_rooms

    else
        print("Error: Arguments must be whole numbers, positive greater than 0")
        sys.exit(0)