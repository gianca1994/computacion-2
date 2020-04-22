# Escribir un programa que en ejecución genere dos procesos, uno padre y otro hijo.
# El hijo debe escribir "Soy el hijo, PID YYYY" 5 veces (YYYY es el pid del hijo).
# El padre debe escribir "Soy el padre, PID XXXX, mi hijo es YYYY" 2 veces (XXXX es el pid del padre).
# El padre debe esperar a que termine el hijo y mostrar el mensaje "Mi proceso hijo, PID YYYY, terminó".
# El hijo al terminar debe mostrar "PID YYYY terminando".

#------------------------------------------------------------------------------------------------------#
#---------------------------------------COMIENZA EL EJERCICIO------------------------------------------#
#------------------------------------------------------------------------------------------------------#

# !/usr/bin/python3

import os


def child():
    # Con el "range(5)" le decimos que ejecute el print 5 veces.
    for x in range(5):
        print("Soy el hijo, PID %d" % (os.getpid()))
    os._exit(0)


def parent():
    childProc = os.fork()
    if childProc == 0:
        child()
    else:
        childExit = os.wait()
        print("PID %d terminando" %(childExit[0]))
        print("Mi proceso hijo, PID %d, terminó" % (childExit[0]))
        for x in range(2):
            print("Soy el padre, PID %d, mi hijo es" % (os.getpid()), "%d" % (childExit[0]))
parent()
