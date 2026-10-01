from SortingFunctions.bubbleSort import bubble_sort
from SortingFunctions.insertionSort import insertion_sort
from SortingFunctions.mergeSort import merge_sort
from SortingFunctions.quickSort import quick_sort
from SortingFunctions.selectionSort import selection_sort
from generateFile import createFile
import csv
import io
import matplotlib.pyplot as plt
import pandas as pd
import random
import time

def _as_csv(values):
  output = io.StringIO()
  csv.writer(output).writerow(values)
  return output.getvalue()

def generateRandoms(length, minRand, maxRand):
  numbers = random.sample(range(minRand, maxRand + 1), length)
  return _as_csv(numbers)

times = {}

def plot_times():
  results = pd.DataFrame.from_dict(
    times,
    orient="index",
    columns=["Tiempo (segundos)"],
  )
  axis = results.plot(
    kind="bar",
    legend=False,
    title="Tiempo de ordenamiento por algoritmo",
  )
  axis.set_xlabel("Algoritmo")
  axis.set_ylabel("Tiempo (segundos)")
  axis.tick_params(axis="x", labelrotation=25)
  figure = axis.get_figure()
  figure.tight_layout()
  plt.show()
  plt.close(figure)

def main():
  input_path = "generatedLists/unordenatedNumbers.csv"
  createFile(input_path, generateRandoms(10000, 0, 10000))

  with open(input_path, "r", encoding="utf-8", newline="") as file:
    row = next(csv.reader(file), [])
  numbers = [int(value) for value in row]

  algorithms = {
    "bubbleSort": lambda values: bubble_sort(values),
    "insertionSort": lambda values: insertion_sort(values),
    "mergeSort": lambda values: merge_sort(values, 0, len(values) - 1),
    "quickSort": lambda values: quick_sort(values, 0, len(values) - 1),
    "selectionSort": lambda values: selection_sort(values, len(values)),
  }

  for name, sort in algorithms.items():
    sorted_numbers = numbers.copy()
    start = time.perf_counter()
    sort(sorted_numbers)
    times[name] = time.perf_counter() - start
    createFile(f"generatedLists/{name}.csv", _as_csv(sorted_numbers))

  plot_times()
  return times

if __name__ == "__main__":
  main()
