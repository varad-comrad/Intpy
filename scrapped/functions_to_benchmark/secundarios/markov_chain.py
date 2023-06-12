import numpy as np

def f(x):
    return np.exp(np.sin(x[0]*5) - x[0]*x[0] - x[1]*x[1])


def markov_chain_function(n):
    x = np.zeros((2))
    p = f(x)
    for i in range(n):
        x2 = x + .01*np.random.randn(x.size)
        p2 = f(x2)
        if (np.random.rand() < (p2/p)):
            x = x2
            p = p2
    return x
