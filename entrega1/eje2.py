#Escribir un programa que reciba dos nombres de archivos por línea de órdenes utilizando los parámetros “-i”
#y “-o” procesados con getopt().

#El programa debe verificar que el archivo pasado a “-i” exista en el disco. De ser así, lo abrirá en modo
#de solo lectura, leerá su contenido, y copiará dicho contenido en un archivo nuevo cuyo nombre será el
#pasado a “-o”. Si el archivo nuevo ya existe, deberá sobreescribirlo.

#------------------------------------------------------------------------------------------------------#
#---------------------------------------COMIENZA EL EJERCICIO------------------------------------------#
#------------------------------------------------------------------------------------------------------#

# !/usr/bin/python3

import getopt
import os.path
import sys

(opt, arg) = getopt.getopt(sys.argv[1:], 'i:o:', ['test1=', 'test2='])

print('(Opciones ; Argumentos)', opt)

for (op, ar) in opt:
    if op == '-i':
        file1 = str(ar)
        print("archivo 1 =", ar)
    elif op == '-o':
        file2 = str(ar)
        print("archivo 2 =", ar)

if os.path.isfile(file1):
    file1 = open(file1, 'r')
    file2 = open(file2, '+w')
    linea = file1.readline()
    while linea:
        file2.write(linea)
        linea = file1.readline()
