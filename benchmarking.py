from intpy.intpy import initialize_intpy, deterministic
from benchmark.benchmark import Benchmark
import sys
from functions_to_benchmark.fibonacci import fib
from functools import lru_cache
# from memo import memorize

import numpy as np
    
@initialize_intpy(__file__)
def main(n: int):
    benchmark = Benchmark(deterministic(fib), fib, lru_cache(fib))
    benchmark.benchmark(n, i=200)
    benchmark.save_csv(['results_intpy.csv', 'results_vanilla.csv', 'results_lru_cache.csv'], folder='./results')

if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)