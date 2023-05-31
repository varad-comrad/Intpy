# from memoizer.DecoratorFactoryInstance import factory #! Not Working!!! Memo is for Python2


# @factory.decorator
def fib(n):
    return fib(n-1) + fib(n-2) if n >1 else n

fib(30)