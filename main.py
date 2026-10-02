from SortingFunctions.bubbleSort import bubble_sort
from SortingFunctions.insertionSort import insertion_sort
from SortingFunctions.mergeSort import merge_sort
from SortingFunctions.quickSort import quick_sort
from SortingFunctions.selectionSort import selection_sort
from generateFile import resetFile, benchMethods, readFile
from itertools import combinations
import csv
import matplotlib.pyplot as plt
import pandas as pd
import random

def generateRandoms(length, minRand, maxRand):
  numbers = random.sample(range(minRand, maxRand + 1), length)
  return numbers

def main():
    numbers = generateRandoms(10000, 0, 10000)

    algorithms = {
        "bubbleSort": lambda values: bubble_sort(values),
        "insertionSort": lambda values: insertion_sort(values),
        "mergeSort": lambda values: merge_sort(values, 0, len(values) - 1),
        "quickSort": lambda values: quick_sort(values, 0, len(values) - 1),
        "selectionSort": lambda values: selection_sort(values, len(values)),
    }

    # for name, sort in algorithms.items():
    #     resetFile(f"generatedLists/{name}.csv")
    #     benchMethods(sort, name, 10000, 100, numbers)

    datasheet = {}

    for name, sort in algorithms.items():
        data = pd.read_csv(f"generatedLists/{name}.csv", sep=";")

        if datasheet.get("x") is None:
            datasheet["x"] = data.N

        key = name
        datasheet[key] = data.Tiempo

    metodos = [key for key in datasheet.keys() if key != "x"]

    for metodo1, metodo2 in combinations(metodos, 2):
        plt.figure(figsize=(8, 5))

        plt.plot(datasheet["x"], datasheet[metodo1], label=metodo1, marker="o")
        plt.plot(datasheet["x"], datasheet[metodo2], label=metodo2, marker="s")

        plt.xlabel("N (Tamaño de la lista)")
        plt.ylabel("Tiempo (s)")
        plt.title(f"Comparativa: {metodo1} vs {metodo2}")
        plt.legend()
        plt.grid(True)

        plt.show()



if __name__ == "__main__":
  main()
