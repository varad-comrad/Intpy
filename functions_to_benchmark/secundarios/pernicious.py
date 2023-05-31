# import numpy as np
# import time
# import sys
# import scipy as sp
# from intpy_dev.intpy import initialize_intpy, deterministic

# @deterministic
def is_prime_number(n):
    if n in (2, 3):
        return True
    if 2 > n or 0 == n % 2:
        return False
    if 9 > n:
        return True
    if 0 == n % 3:
        return False

    return not any(map(
        lambda x: 0 == n % x or 0 == n % (2 + x),
        range(5, 1 + int(n ** 0.5), 6)
    ))

# @deterministic
def get_number_of_ones(n):
    return bin(n).count("1")

# @deterministic
def find_pernicious_numbers(n):
    i = 1
    counter = 0
    while counter < n:
        if is_prime_number(get_number_of_ones(i)):
            counter += 1
        i += 1
    return i-1, counter

# @initialize_intpy(__file__)
# def main():
#     N = int(sys.argv[1])
#     start = time.perf_counter()
#     find_pernicious_numbers(N)
#     print(time.perf_counter()-start)
#     print()


# if __name__ == "__main__":
#     main()
