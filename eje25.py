#!/usr/bin/python
import getopt, sys, multiprocessing


def option_reading():

    # Inicializamos las 3 variables como none...
    cantidad_procesos = num_min = num_max = None
    # Usamos getopt para tomar los 3 argumentos que necesitamos
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:m:n:')

    # Si, el numero de opciones ingresados, es diferente de 3, entonces...
    if len(opt) != 3:
        print("Error: Expected at least 3 options [-p] [-m] [-n]", len(opt), "received")
        sys.exit(0)

    # Si no, un for para almacenar en las variables "cantidad_procesos", "num_min", "num_max"
    for (opt, arg) in opt:
        if opt == '-p':
            cantidad_procesos = int(arg)
        elif opt == '-m':
            num_min = int(arg)
        elif opt == '-n':
            num_max = int(arg)

    # En caso de no ser none las 3 variables
    assert (cantidad_procesos, num_min, num_max) is not None

    # Error en caso de que hayan pas procesos que numeros o que el numero minimo sea mayor al maximo...
    if (cantidad_procesos > num_max - num_min) or (num_min > num_max):
        raise getopt.GetoptError('The num_min must be less than num_max, or it may have more processes than numbers.')
    
    # Sino, retornamos los valores.
    return cantidad_procesos, num_min, num_max


def sublist_squared(sublist):
    # Con un for, recorremos numero por numero de la sublista
    for numero in sublist:
        # Declaramos el nombre del proceso
        MultiProcssName = multiprocessing.current_process().name
        # y printeamos el process name y el cuadrado del numero...
        print(f'{MultiProcssName} --> {numero}^2')


def separate_list(aimList, parts):
    # En la variable 'length' almacenamos la longitud de la cadena 'aimList'
    length = len(aimList)
    # Retornamos la cadena aimList, partimos la lista de elementos en sublistas.
    return [aimList[part * length // parts:(part + 1) * length // parts] for part in range(parts)]


def main():
    # En las 3 variables, alojamos los valores que obtuvimos de los argumentos en la funcion option_reading()
    cantidad_procesos, min_num, max_num = option_reading()

    # Usamos la funcion list() para convertir los numeros a tipo lista.. y hacemos un range desde el min num al max.
    aim_list = list(range(min_num, max_num))

    # Definimos que la variable process_list va a ser una lista a la que luego se le adjuntaran procesos
    process_list = []

    # Un for para recorer la lista separada
    for sublist in separate_list(aim_list, cantidad_procesos):
        # En la variable 'proces' vamos a ir cargando los procesos usando multiprocessing para varios procesos.
        proces = multiprocessing.Process(target=sublist_squared, args=(sublist,))
        # Iniciamos el proceso
        proces.start()
        # Adjunatamos a la lista previamente definida, el proceso
        process_list.append(proces)

    # En un for decimos que si el proc esta en la lista de procesos
    for proc in process_list:
        # Unimos el proc...
        proc.join()

main()
