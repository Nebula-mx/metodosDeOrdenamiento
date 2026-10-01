from SortingFunctions.bubbleSort import bubble_sort
from SortingFunctions.insertionSort import insertion_sort
from SortingFunctions.mergeSort import merge_sort
from SortingFunctions.quickSort import quick_sort
from SortingFunctions.selectionSort import selection_sort
from generateFile import resetFile, benchMethods
import csv
import io
import matplotlib.pyplot as plt
import pandas as pd
import random
import time

def generateRandoms(length, minRand, maxRand):
  numbers = random.sample(range(minRand, maxRand + 1), length)
  return numbers

times = {}

def main():

    numbers = generateRandoms(10000, 0, 10000)

    algorithms = {
        "bubbleSort": lambda values: bubble_sort(values),
        "insertionSort": lambda values: insertion_sort(values),
        "mergeSort": lambda values: merge_sort(values, 0, len(values) - 1),
        "quickSort": lambda values: quick_sort(values, 0, len(values) - 1),
        "selectionSort": lambda values: selection_sort(values, len(values)),
    }

    for name, sort in algorithms.items():
        resetFile(f"generatedLists/{name}.csv")
        benchMethods(sort, name, 10000, 100, numbers)

if __name__ == "__main__":
  main()
