# from memoizer.DecoratorFactoryInstance import factory #! Not Working!!! Memo is for Python2
import argparse

# @factory.decorator
def fib(n):
    return fib(n-1) + fib(n-2) if n >1 else n
def pfib(n):
    print(fib(n))
fib(30)

parser = argparse.ArgumentParser(prog='fib')
parser.add_argument('-f', '--fib')
args = parser.parse_args()
print(args.fib)
