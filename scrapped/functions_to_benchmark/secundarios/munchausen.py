# import time
# import sys
# from intpy_dev.intpy import initialize_intpy, deterministic


def raised_to_string(x):
    x = int(x)
    if x == 0:
        return 0
    else:
        return x**x


def raised_to(x):
    if x == 0:
        return 0
    else:
        return x**x


power_of_digits = [raised_to(i) for i in range(10)]


def is_munchausen_number(i):
    return i == sum(power_of_digits[int(x)] for x in str(i))

# @deterministic
def find_munchausen_numbers(n):
    i = 0
    while True:
        if is_munchausen_number(i):
            number += 1
            print("Munchausen number %d: %d" % (n, i))
        if (number == 4):
            break
        i += 1
    return i


# @initialize_intpy(__file__)
# def main():
#     n = int(sys.argv[1])
#     start = time.perf_counter()
#     find_munchausen_numbers(n)
#     print(time.perf_counter()-start)


# if __name__ == "__main__":
#     main()
