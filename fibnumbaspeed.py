import numba as nb, time, sys
from speedupy import initialize_intpy, deterministic

@deterministic
@nb.njit
def fib(n):
    return fib(n-1) + fib(n-2) if n>2 else n

@initialize_intpy(__file__)
def main(n):
    t=time.perf_counter()
    fib(n)
    print(time.perf_counter()-t)

if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)
