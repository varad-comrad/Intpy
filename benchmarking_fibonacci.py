from intpy_dev.intpy import initialize_intpy, deterministic
from benchmark.benchmark import Benchmark
import sys
from functions_to_benchmark.prioridades.fibonacci import fib
from functools import lru_cache
# from memo.memoizer.DecoratorFactoryInstance import factory 

import numpy as np
    
@initialize_intpy(__file__)
def main(n: int, i: int) -> None:
    benchmark = Benchmark(deterministic(fib), fib, lru_cache(fib)) #, factory.decorator(fib))
    benchmark.benchmark(n, i=i)
    benchmark.save_csv(['results_intpy.csv', 'results_vanilla.csv', 'results_lru_cache.csv'], opening_mode='w', folder='results_fibonacci')

if __name__ == '__main__':
    n = int(sys.argv[1])
    i = int(sys.argv[2])
    main(n, i)