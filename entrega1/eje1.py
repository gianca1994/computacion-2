# Crear una calculadora, donde se pase como argumentos luego de la opción -o el operador que se va a
# ejecutar (+,-,*,/), luego de -n el primer número de la operación, y de -m el segundo número.
# Ejemplo: "./calc -o + -n 5 -m 6"
# 5 + 6 = 11
# Considerar que el usuario puede ingresar los argumentos en cualquier orden. El programa deberá verificar
# que los argumentos sean válidos (no repetidos, números enteros, y operaciones válidas.

#------------------------------------------------------------------------------------------------------#
#---------------------------------------COMIENZA EL EJERCICIO------------------------------------------#
#------------------------------------------------------------------------------------------------------#

# !/usr/bin/python3

import getopt
import sys

(opt, arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')

print("(opciones,argumentos)", opt)

operator = ''
num1 = ''
num2 = ''

for (op, ar) in opt:
	if (op == '-n'):
		print("number 1 =", ar)
		num1 = int(ar)
	elif (op == '-m'):
		print("number 2 =", ar)
		num2 = int(ar)
	elif (op == '-o'):
		print("operator =", ar)
		operator = ar

		if (operator == '+'):
			print('El resultado nos da: %d + %d = %d' % (num2, num1, num2 + num1))
		elif (operator == '-'):
			print('El resultado nos da: %d - %d = %d' % (num2, num1, num2 - num1))
		elif (operator == '*'):
			print('El resultado nos da: %d * %d = %d' % (num2, num1, num2 * num1))
		elif (operator == '/'):
			print('El resultado nos da: %d / %d = %d' % (num2, num1, num2 / num1))

	else:
		print("Opcion invalida")
