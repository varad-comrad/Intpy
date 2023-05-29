def fib(n: int) -> int:
    return fib(n-1) + fib(n-2) if n>2 else n