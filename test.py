# from memoizer.DecoratorFactoryInstance import factory #! Not Working!!! Memo is for Python2
import argparse
import pathlib
# from intpy_dev.intpy import initialize_intpy, get_params


# @factory.decorator
def fib(n):
    return fib(n-1) + fib(n-2) if n >1 else n
def pfib(n):
    print(fib(n))
fib(30)

# # @initialize_intpy(__file__)
# def main():
#     pass
# if __name__ == "__main__":
#     # main()
#     # parser = argparse.ArgumentParser(parents=[get_params()])
#     # parser.add_argument('-f', '--fib')
#     # args = parser.parse_args()
#     # print(args.fib)
# class A:
#     def __new__(cls, *args, **kwargs):
#         if hasattr(cls, 'instance'):
#             return cls.instance
#         cls.instance = super().__new__(cls)
#         return cls.instance
    
#     def __init__(self, a) -> None:
#         self.a = a

# a = A('sjff')
# print(a.a)
# a = A('wkjdhgw')
# print(a.a)

# import pandas as pd
# l = [pd.read_csv('results_fibonacci/results_intpy.csv') for _ in range(5)]
# df = pd.Series(l)
# print(df[0])