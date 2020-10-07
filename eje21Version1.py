#!/usr/bin/python

import sys, getopt, time, random, multiprocessing


def incoming_pac(consulting_rooms, med_times):

    # Actualizamos la variable y mostramos cuantos consultorios hay disponibles...
    room = consulting_rooms.get_value()
    print("A patient arrived, now there is", room, "consulting rooms")

    consulting_rooms.acquire()

    # Actualizamos la variable y mostramos cuantos consultorios hay disponibles...
    room = consulting_rooms.get_value()
    print("A patient is being treated, there is", room, "consulting rooms")

    # El timesleep, lo hacemos con un random number entre medico y medico.
    time.sleep(random.uniform(med_times[0], med_times[1]))
    consulting_rooms.release()

    # Actualizamos la variable y mostramos cuantos consultorios hay disponibles...
    room = consulting_rooms.get_value()
    print("A patient retired, now there is", room, "consulting rooms")

def attended_pac(pac_times, med_times, consulting_rooms):
    i = 1
    while True:
        # El timesleep, lo hacemos con un random number entre paciente y paciente.
        time.sleep(random.uniform(pac_times[0], pac_times[1]))
        # Targeteamos la funcion "incoming_pac" y le pasamos como argumentos: "consulting_rooms, med_times, i" e iniciamos el proceso
        multiprocessing.Process(target=incoming_pac, args=(consulting_rooms, med_times, i)).start()
        i += 1

def main():
    # Declaramos las variables pac_times y med_times con los rangos correspondientes..
    pac_times = (1, 3)
    med_times = (5, 7)
    # A la variable consulting_rooms
    consulting_rooms = multiprocessing.Semaphore(5)
    # Llamamos y ejecutamos la funcion attended_pac y le parametrizamos los valores previamentes definidos...
    attended_pac(pac_times, med_times, consulting_rooms)

main()