Cliente y servidor FTP - Computacion 2 - 2020

09/11/2020 - Se crearon los 2 archivos .py (ServidorFTP.py y ClienteFTP.py)

ClienteFTP.py - Implementaciones:

09/11/2020 - Se definio la funcion "option_reading" para leer la ip y puerto con los cuales, el cliente se conecta al servidor.

09/11/2020 - Se definio el "main" para realizar todas las acciones.

09/11/2020 - Se creo todo lo relacionado al socket.

10/11/2020 - Se definio el bucle while dentro del (main), para enviarle al servidorFTP todos los comandos que el cliente quiera ejecutar.

ServidorFTP.py - Implementaciones:

09/11/2020 - Se definio la funcion "option_reading" para leer el puerto sobre el cual, corre el servidor.
09/11/2020 - Se definio la funcion "ClosedServer" para cerrar el servidor.
09/11/2020 - Se creo la funcion main con todo las funcionalidades (Cargar la ip local y el puerto del option_reading, crear el socket TCP, quedarse esperando online hasta que un cliente se conecte y un while para aceptar las conexiones de los clientes usando multiprocessing para atender multiples clientes al mismo tiempo). 
10/11/2020 - Se definio la funcion "clientint" para recibir los comandos del cliente y enviarle la respuesta a su peticion.