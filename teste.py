# from intpy.intpy import initialize_intpy, deterministic
# import sys

# class Test:
#     def __init__(self, name):
#         self.name = name


# @deterministic
# def test(alfa):
#     print(alfa.name)

# @initialize_intpy(__file__)
# def main(n):
#     alfa = Test('shdg')
#     for i in range(n):
#         test(alfa)

# if __name__ == '__main__':
#     n = int(sys.argv[1])   
#     main(n)

import pandas as pd

print(type(pd.Series([4, 5, 6])))