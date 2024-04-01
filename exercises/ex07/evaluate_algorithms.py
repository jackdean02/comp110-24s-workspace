"""Evaluate EX07 Algorithms."""
__author__ = "730385160"
import matplotlib.pyplot as plt
from runtime_analysis_functions import evaluate_runtime

START_SIZE: int = 0
END_SIZE: int = 1000
times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - 730385160")
plt.show()