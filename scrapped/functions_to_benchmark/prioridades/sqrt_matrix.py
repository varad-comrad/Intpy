import numpy as np
# import time
# import sys
import scipy as sp
# from intpy_dev.intpy import initialize_intpy, deterministic


# @deterministic
def sqrt_matrix_sp(A):
    return sp.linalg.sqrtm(A)

# def sqrt_matrix_np(A):
#     return np.linalg.sqrtm(A)


# @initialize_intpy(__file__)
# def main(A):
#     print(sqrt_matrix(A))


# if __name__ == "__main__":
#     n = int(sys.argv[1])
#     A = np.ones((n, n))
#     for i in range(n):
#         A[i, i] = 6
#     start = time.perf_counter()
#     main(A)
#     print(time.perf_counter()-start)
