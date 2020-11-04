#!/usr/bin/python
import getopt, sys, socket, hashlib

# El módulo hashlib pertenece a la librería estándar y permite realizar cifrados directamente desde Python 
# con los algoritmos BLAKE, SHAKE, SHA1, SHA224, SHA256, SHA384, SHA512 y MD5.

Hashes ={
    'sha1':hashlib.sha1,
    'sha224':hashlib.sha224,
    'sha256':hashlib.sha256,
    'sha384':hashlib.sha384,
    'sha512':hashlib.sha512,
    'sha3-224':hashlib.sha3-224,
    'sha3-256':hashlib.sha3-256,
    'sha3-384':hashlib.sha3-384,
    'sha3-512':hashlib.sha3-512,
}

def option_reading():

    # Inicializamos las 2 variables como none...
    port, enable_use_threads = None

    # Usamos getopt para tomar los 2 argumentos que necesitamos
    (opt, arg) = getopt.getopt(sys.argv[1:], 'pmt:')

    # Si, el numero de opciones ingresados, es diferente de 2, entonces...
    if len(opt) != 2:
        raise getopt.GetoptError("Error: Expected at least 2 options [-p] and ([-m] or [-t]).")
        sys.exit(0)

    # Si no, un for para almacenar en las variables "port", "enable_use_threads(booleana) en -m y -t"
    for (opt, arg) in opt:
        if opt == '-p':
            port = int(arg)
        elif opt == '-m':
            enable_use_threads = False
        elif opt == '-t':
            enable_use_threads = True

    # Si, se comprueba que port y enable_use_threads no son "None", entonces, nos retorna los mismos
    assert (port, enable_use_threads) is not None
    return port, enable_use_threads

# Funcion para atender el socket enviado por el cliente
def read_client(Csocket):

    # Desencodeamos el hash que viene del cliente en el socket
    ClientHash = Csocket.recv(64).decode()
    # Y decimos, si el hash no esta en la lista de hashes permitidos
    if ClientHash not in Hashes:
        # Error - 404
        Csocket.send('404'.encode())
        return
    else:
        # OK - 200
        Csocket.send('200'.encode())

    # Desencodeamos el socket del cliente y lo almacenamos en la variable
    cTexto = Csocket.recv(1024).decode()
    # En la variable hashed almacenamos, de los Hashes(El hash del cliente)
    hashed = Hashes[ClientHash]
    hashed.update(cTexto.encode())
    Csocket.send(hashed.hexdigest().encode())

def main():
    # Almacenamos en IPV4 la ip local del servidor
    IPV4 = socket.gethostbyname(socket.getfqdn())
    # Alamacenamos en las 2 variables, los argumentos ingresados en la funcion option_reading()
    port, enable_use_threads = option_reading()
    # Creamos el socket del servidor con protocolo TCP
    Ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enlazamos el socket con la ip local y el puerto ingresado como argumento
    Ssocket.bind(('', port))
    # Avisamos, que el servidor esta online en la ip y puerto y si esta usando hilos o procesos
    print(f"online server (IPV4 and PORT): {IPV4}:{port},using {'Threads' if enable_use_threads else 'Processes'}")

    # En caso de enable_use_threads sea 'TRUE' importamos 'Thread', sino 'Process'
    if enable_use_threads:
        from threading import Thread as Thread_Or_Process
    else:
        from multiprocessing import Process as Thread_Or_Process
    # Se use Procesos o Hilos, ambas se almacenan en, de esta forma no tendremos problemas en el siguiente while.

    while True:
        # El socket del sv queda escuchando...
        Ssocket.listen(16)
        # Aceptamos la conexion...
        Csocket, address = Ssocket.accept()
        print(f'{address}, has connected...')

        # Creamos un nuevo proceso o hilo, variable T_Or_P ("Thread Or Process") para atender las peticiones del cliente.
        T_Or_P = Thread_Or_Process(target=read_client, args=(Csocket))
        # Inicializamos el proceso o hilo
        T_Or_P.start()

main()
