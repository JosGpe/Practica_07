import threading
import time
import random
from random import choice

estacionamiento = []
max_autos = 12
nuevos_autos_frecuencia = choice([0.5, 1, 2]) # segundos
quitar_autos_frecuencia = choice([0.5, 1, 2]) # segundos

# función para añadir nuevos autos al estacionamiento
def añadir_auto():
    global estacionamiento
    while True:
        if len(estacionamiento) < max_autos:
            auto = {"marca": "Toyota", "modelo": "Corolla"}
            estacionamiento.append(auto)
            print(f"Nuevo auto añadido al estacionamiento ({len(estacionamiento)} de {max_autos} ocupados).")
        else:
            print("El estacionamiento está lleno")
        time.sleep(random.uniform(0, nuevos_autos_frecuencia))

# función para quitar autos del estacionamiento
def quitar_auto():
    global estacionamiento
    while True:
        if len(estacionamiento) > 0:
            auto = estacionamiento.pop(0)
            print(f"Auto {auto} retirado del estacionamiento ({len(estacionamiento)} de {max_autos} ocupados).")
        else:
            print("El estacionamiento está vacío")
        time.sleep(random.uniform(0, quitar_autos_frecuencia))

# función para imprimir el estado actual del estacionamiento
def imprimir_estado():
    global estacionamiento
    while True:
        print(f"Estado actual del estacionamiento: {len(estacionamiento)} de {max_autos} ocupados.")
        time.sleep(5)

# función para cambiar la frecuencia de añadir nuevos autos
def cambiar_frecuencia_nuevos_autos():
    global nuevos_autos_frecuencia
    while True:
        print(f"Frecuencia actual de añadir nuevos autos: {nuevos_autos_frecuencia} segundos.")
        nuevos_autos_frecuencia = float(input("Introduce la nueva frecuencia en segundos: \n"))
        print(f"Frecuencia actualizada a {nuevos_autos_frecuencia} segundos.")
    
# función para cambiar la frecuencia de quitar autos
def cambiar_frecuencia_quitar_autos():
    global quitar_autos_frecuencia
    while True:
        print(f"Frecuencia actual de quitar autos: {quitar_autos_frecuencia} segundos.")
        quitar_autos_frecuencia = float(input("Introduce la nueva frecuencia en segundos: \n"))
        print(f"Frecuencia actualizada a {quitar_autos_frecuencia} segundos.")

# creamos los hilos para ejecutar las funciones
hilo_añadir_auto = threading.Thread(target=añadir_auto)
hilo_quitar_auto = threading.Thread(target=quitar_auto)
hilo_imprimir_estado = threading.Thread(target=imprimir_estado)
hilo_cambiar_frecuencia_nuevos_autos = threading.Thread(target=cambiar_frecuencia_nuevos_autos)
hilo_cambiar_frecuencia_quitar_autos = threading.Thread(target=cambiar_frecuencia_quitar_autos)

# iniciamos los hilos
hilo_añadir_auto.start()
hilo_quitar_auto.start()
hilo_imprimir_estado.start()
hilo_cambiar_frecuencia_nuevos_autos.start()
hilo_cambiar_frecuencia_quitar_autos.start()

# esperamos a que los hilos terminen
hilo_añadir_auto.join()
hilo_quitar_auto.join()
hilo_imprimir_estado.join()
hilo_cambiar_frecuencia_nuevos_autos.join()
hilo_cambiar_frecuencia_quitar_autos.join()
