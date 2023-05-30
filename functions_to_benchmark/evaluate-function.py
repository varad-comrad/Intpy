import numpy as np
import time
import sys
import scipy as sp
from intpy.intpy import initialize_intpy, deterministic


@deterministic
def evaluate_functions(n):
    vector1 = np.linspace(-1500.00, 1500.0, n)
    iterations = 10000
    for i in range(iterations):
        vector2 = np.sin(vector1)
        vector1 = np.arcsin(vector2)
        vector2 = np.cos(vector1)
        vector1 = np.arccos(vector2)
        vector2 = np.tan(vector1)
        vector1 = np.arctan(vector2)
    return vector2

@initialize_intpy(__file__)
def main():
    n = int(sys.argv[1])
    print('Evaluate Function: ', n)
    start = time.perf_counter()
    evaluate_functions(n)
    print(time.perf_counter()-start)
    print()

if __name__ == "__main__":
    main()