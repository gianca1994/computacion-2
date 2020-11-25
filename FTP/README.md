Cliente y servidor FTP - Computacion 2 - 2020

09/11/2020 - Se crearon los 2 archivos .py (ServidorFTP.py y ClienteFTP.py)


ClienteFTP.py - Implementaciones:

09/11/2020 - Se definio la funcion "option_reading" para leer la ip y puerto con los cuales, el cliente se conecta al servidor.

09/11/2020 - Se definio el "main" para realizar todas las acciones.

09/11/2020 - Se creo todo lo relacionado al socket.

10/11/2020 - Se definio el bucle while dentro del (main), para enviarle al servidorFTP todos los comandos que el cliente quiera ejecutar.

19/11/2020 - Comando "lls" para listar todos los archivos del directorio del cliente.

20/11/2020 - Comando "lls" y "lpwd" Funcionando.

21/11/2020 - Comando "cd" no funcional.

23/11/2020 - Comando "lcd" Funcionando.

24/11/2020 - Se cambio la toma de comandos ahora se hace un split para recibir mas de 1 parametro y si son mas parametros se almacenan en 2 variables.

24/11/2020 - Se agregaron la toma de todos los comandos, para trabajarlos unitariamente 

24/11/2020 - Comandos: lss, lpwd, lcd, exit funcionales.

24/11/2020 - Comando put no funcional.



ServidorFTP.py - Implementaciones:

09/11/2020 - Se definio la funcion "option_reading" para leer el puerto sobre el cual, corre el servidor.

09/11/2020 - Se definio la funcion "ClosedServer" para cerrar el servidor.

09/11/2020 - Se creo la funcion main con todo las funcionalidades (Cargar la ip local y el puerto del option_reading, crear el socket TCP, quedarse esperando online hasta que un cliente se conecte y un while para aceptar las conexiones de los clientes usando multiprocessing para atender multiples clientes al mismo tiempo).

10/11/2020 - Se definio la funcion "clientint" para recibir los comandos del cliente y enviarle la respuesta a su peticion.

14/11/2020 - Funcion "ls" para listar los archivos y directorios de una ruta en el servidor.

16/11/2020 - Correcciones y emprolijamiento del codigo.

21/11/2020 - Comando "ls" y "pwd" Funcionando (Ahora envia las listas empaquetadas al cliente y las muestra en el).

22/11/2020 - Comando "cd" no funcional.

24/11/2020 - Comandos: ls, pwd, help y exit funcionales.

24/11/2020 - Comando cd funcional y correccion de posibles bug y errores como, el envio de un comando vacio o una ruta que no existe..

24/11/2020 - Comando put no funcional.
