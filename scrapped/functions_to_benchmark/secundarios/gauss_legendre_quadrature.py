import numpy as np
# import time
import sys
# import scipy as sp
# from intpy_dev.intpy import initialize_intpy, deterministic


def integrand(x): return np.exp(x)


# @deterministic
def compute_quadrature(n):
    a = -3.0
    b = 3.0

    x, w = np.polynomial.legendre.leggauss(n)

    t = 0.5*(x + 1)*(b - a) + a

    gauss = sum(w * integrand(t)) * 0.5*(b - a)
    return gauss


if len(sys.argv) < 1:
    print('Usage:')
    print('     python ' + sys.argv[0] + ' N')
    print('Please specify the order of the quadrature.')
    sys.exit()


# @initialize_intpy(__file__)
# def main():
#     order = int(sys.argv[1])
#     print('Gauss-Legendre Quadrature of order: ', order)
#     start = time.perf_counter()
#     compute_quadrature(order)
#     print(time.perf_counter()-start)
#     print()


# if __name__ == '__main__':
#     main()
