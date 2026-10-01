import os
import copy
from time import time

from numpy.random.mtrand import f

def createFile(name, content):
    directory = os.path.dirname(name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    with open(name, "a", encoding="utf-8") as file:
        file.write(str(content))

def resetFile(name):
    with open(name, "w", encoding="utf-8") as file:
        file.write("")

def readFile(name):
    lines = []
    with open(name, "r", encoding="utf-8") as file:
        for line in file:
            rawLine = line.strip()
            lines.append(rawLine)
    return lines

def benchMethods(method, fileName, maxCount=10000, steps=100, unorderedList=[]):
    if os.path.exists(fileName):
        os.remove(fileName)

    createFile(f"generatedLists/{fileName}.csv", "N;Tiempo" + "\n")

    for x in range(steps, maxCount + steps, steps):
        lista_nueva = copy.deepcopy(unorderedList[:x])

        inicio_tiempo = time()
        method(lista_nueva)  # Ejecutamos la función pasada como parámetro
        transcurrido = time() - inicio_tiempo

        createFile(f"generatedLists/{fileName}.csv", str(x)+";"+format(transcurrido,'.5f') + "\n")
