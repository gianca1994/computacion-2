# **Cliente y servidor FTP - Computacion 2 - 2020**

**Guia de uso:**

-En el directorio "/FTP/Servidor" iniciar consola y tipear:

-Python3 ServidorFTP.py -p 'Puerto deseado (debe ser mayor a 1000, para evitar puertos reservados)' - Ya tendremos el servidor ONLINE

-En el directorio "/FTP/Cliente" iniciar consola y tipear:

-Python3 ClienteFTP.py -h 'Ip del servidor' -p 'Puerto del servidor' - Ya tendremos el cliente conectado con el servidor.


-Luego de esto, ya podremos ejecutar todos los comandos, para ver la lista de comandos tipear: 'Help (en el cliente)'


**Especificaciones y mejoras:**

- Se utilizo multiprocessing para poder atender a mas de 1 cliente al mismo tiempo.

- Se puede mejorar utilizando encriptacion al enviar los paquetes para mayor seguridad

- Trabajar con base de datos utilizando un login y permisos

- Optimizar el rendimiento utilizando mapeo para evitar repeticion si el proyecto se extiende



**Cambios realizados:**

09/11/2020 - Se crearon los 2 archivos .py (ServidorFTP.py y ClienteFTP.py)