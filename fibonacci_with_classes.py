from intpy.intpy import initialize_intpy, deterministic

import time
import sys
import csv

class Benchmark:
    def __init__(self, func1, func2):
        self.func1 = func1
        self.func2 = func2
        self.results1 = []
        self.results2 = []

    def benchmark1(self, n, iter):
        for _ in range(iter):
            aux = []
            for i in range(n):
                t = time.perf_counter()
                self.func1(i)
                aux.append(time.perf_counter()-t)
            self.results1.append(aux)

    def benchmark2(self, n, iter):
        for _ in range(iter):
            aux = []
            for i in range(n):
                t = time.perf_counter()
                self.func2(i)
                aux.append(time.perf_counter()-t)
            self.results2.append(aux)

    def save_csv(self, filename1, filename2):
        with open(filename1, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(range(len(self.results1)))
            for element in self.results1:
                writer.writerow(element)

        with open(filename2, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(range(len(self.results2)))
            for element in self.results2:
                writer.writerow(element)


@deterministic
def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else n


def no_intpy_fib(n):
    return no_intpy_fib(n-1) + no_intpy_fib(n-2) if n > 2 else n


@initialize_intpy(__file__)
def main(n: int):
    benchmark = Benchmark(fib, no_intpy_fib)
    benchmark.benchmark1(n, 200)
    benchmark.benchmark2(n, 200)
    benchmark.save_csv('results_intpy.csv', 'results_no_intpy.csv')

if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)