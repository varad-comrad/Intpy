from intpy.intpy import initialize_intpy, deterministic
import time
import matplotlib.pyplot as plt


@deterministic
def fibonacci_recursive(n):
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2) if n > 2 else 1

@deterministic
def fibonacci_iterative(n):
    if n <=2:
        return 1
    a = 1
    b = 1
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    return b

def fibonacci_recursive_no_intpy(n):
    return fibonacci_recursive_no_intpy(n-1) + fibonacci_recursive_no_intpy(n-2) if n > 2 else 1


def fibonacci_iterative_no_intpy(n):
    pass

class FibonacciBenchmark:
    def __init__(self, fun1: function, fun2: function):
        self.fun1 = fun1
        self.fun2 = fun2
        self.results_fun1: list = []
        self.results_fun2: list = []
        self.cnt_fun1: int = 0
        self.cnt_fun2: int = 0

    
    def benchmark_fun1(self, *args):
        self.results_fun1.append([])
        for i in range(args[0]):
            self.results_fun1[self.cnt_fun1].append(
                time.perf_counter(self.fun1(i)))
        self.cnt_fun1+=1
            
    
    def benchmark_fun2(self, *args):
        self.results_fun2.append([])
        for i in range(args[0]):
            self.results_fun2[self.cnt_fun2].append(
                time.perf_counter(self.fun2(i)))
        self.cnt_fun2 += 1


@initialize_intpy(__file__)
def main():
    print(fibonacci_iterative(3))
    # benchmark = FibonacciBenchmark(fibonacci_recursive, fibonacci_iterative)
    # benchmark_no_intpy = FibonacciBenchmark(fibonacci_recursive_no_intpy, fibonacci_iterative_no_intpy)

if __name__ == '__main__':
    main()