from intpy.intpy import initialize_intpy, deterministic
from benchmark.benchmark import Benchmark
import sys
from functions_to_benchmark.fibonacci import fib
from functools import lru_cache, cache
# from memo import memorize



@initialize_intpy(__file__)
def main(n: int):
    benchmark = Benchmark(deterministic(fib), fib)
    benchmark.benchmark1(n, 200)
    benchmark.benchmark2(n, 200)
    benchmark.save_csv('results_intpy.csv', 'results_no_intpy.csv')

if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)