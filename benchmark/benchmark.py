import time
import csv
import typing



class Benchmark:
    def __init__(self, *args):
        self.funcs = list(args)
        self.results: list[list] = []

    def benchmark(self, n: int, iter: int) -> None:
        for func in self.funcs:
            self.benchmark_one(n, iter, func)
        pass

    def benchmark_one(self, n: int, iter: int, func) -> None:
        result1: list = []
        for _ in range(iter):
            aux = []
            for i in range(n):
                t = time.perf_counter()
                func(i)
                aux.append(time.perf_counter()-t)
            result1.append(aux)
        self.results.append(result1)

    def save_csv(self, filepaths: list[str]) -> None:
        for filepath, lst in zip(filepaths,self.results):
            with open(filepath, 'w') as fp:
                writer = csv.writer(fp)
                writer.writerow(range(1,len(lst)+1))
                for element in lst:
                    writer.writerow(element)

