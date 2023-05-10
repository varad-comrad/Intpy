import sys
import time
import csv


def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else n


def timeit(func, n):
    t = time.perf_counter()
    func(n)
    return time.perf_counter() - t


def benchmark_once(func, n):
    return [timeit(func, i) for i in range(n)]


def benchmark(func, n):
    results = []
    for _ in range(n):
        results.append(benchmark_once(func, n))
    return results


def main():
    l1 = benchmark(fib, n)
    # l2 = benchmark(no_intpy_fib, n)
    with open('results_no_intpy.csv', 'w') as fp:
        writer = csv.writer(fp)
        writer.writerow(range(len(l1)))
        for element in l1:
            writer.writerow(element)


if __name__ == '__main__':
    n = int(sys.argv[1])
    main()
