"""
    Ejemplo del manejo de hilos
"""

import requests
import time
import csv
import threading
# librería de python que permite ejecutar comandos
import subprocess

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for lineaObtenida in lineas:
            print("Linea obtenida de archivo data: ",lineaObtenida)
            # pass
            # lista.append((numero, pagina))
            valoresAux = lineaObtenida[0].split('|')
            lista.append((valoresAux[0], valoresAux[1]))
    # se retorna la lista con la información que se necesita
    return lista

def worker(numero, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    # pass
    resultado = requests.get(url)
    print("Se va a crear el archivo %s.txt" % numero)
    resultado.encoding = 'utf-8'
    archivo = open("salida/%s.txt" % numero,"w", encoding='utf-8')
    archivo.writelines(resultado.text)
    archivo.close()
    print("Archivo creado %s.txt" % numero)
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    # Se crea los hilos
    # en la función
    numero = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='navegando...',
                            target=worker,
                            args=(numero, url))
    hilo1.start()