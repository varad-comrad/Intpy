from intpy.intpy import initialize_intpy, deterministic
import time
import matplotlib.pyplot as plt
import sys
import multiprocessing
import numpy as np
import pandas as pd


def fibonacci_recursive(n):
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2) if n >=2 else n

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

class FibonacciBenchmark:
    def __init__(self, fun1, fun2, title = ''):
        self.fun1 = fun1
        self.fun2 = fun2
        self.results_fun1 = []
        self.results_fun2 = []
        self.cnt_fun1 = 0
        self.cnt_fun2 = 0
        self.title = title

    def benchmark_fun1(self, *args):
        self.results_fun1.append([])
        for i in range(args[0]):
            t = time.perf_counter()
            self.fun1(i)
            self.results_fun1[self.cnt_fun1].append(
                time.perf_counter() - t)
        self.cnt_fun1 += 1

    def benchmark_fun2(self, *args):
        self.results_fun2.append([])
        for i in range(args[0]):
            t = time.perf_counter()
            self.fun2(i)
            self.results_fun2[self.cnt_fun2].append(
                time.perf_counter() - t)
        self.cnt_fun2 += 1
        
    def to_numpy(self):
        aux_results_fun1 = np.array(self.results_fun1)
        aux_results_fun2 = np.array(self.results_fun2)
        return aux_results_fun1.mean(axis=0), aux_results_fun2.mean(axis=0)


def plot_graphic(bench1, bench2, n: int):
    aux1, subtitles = (bench1.to_numpy(), bench2.to_numpy()), ['Recursive Fibonacci', 'Iterative Fibonacci']
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle('benchmark')
    for i in range(2): 
        for j in range(2):
            axes[i,j].plot(np.arange(n), aux1[i][j], color='bisque')
            axes[i,j].set_title(subtitles[j])
            axes[i,j].grid(color='lawngreen', linestyle='--')
            axes[i,j].set_facecolor('royalblue')
    fig.show()

def improvement(bench1, bench2):
    aux1, aux2 = bench1.to_numpy(), bench2.to_numpy()
    vec1 = (aux1[0]-aux2[0])/aux2[0]
    vec2 = (aux1[1]-aux2[1])/aux2[1]
    return {'Recursive':vec1,'Iterative':vec2}

def save_results(data):
    data.to_csv('results.csv',mode = 'a')

@initialize_intpy(__file__)
def main(n):
    benchmark = FibonacciBenchmark(deterministic(fibonacci_recursive), deterministic(fibonacci_iterative), 'Intpy')
    benchmark_no_intpy = FibonacciBenchmark(fibonacci_recursive, fibonacci_iterative, 'No Intpy')
    for _ in range(100): 
        benchmark.benchmark_fun1(n)
        benchmark.benchmark_fun2(n)
        benchmark_no_intpy.benchmark_fun1(n)
        benchmark_no_intpy.benchmark_fun2(n)
    plot_graphic(benchmark, benchmark_no_intpy, n)
    d = improvement(benchmark, benchmark_no_intpy)
    df = pd.DataFrame(d)
    df.index = range(1,df.shape[0]+1)
    print(df)
    save_results(df)
    input()
    
if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)