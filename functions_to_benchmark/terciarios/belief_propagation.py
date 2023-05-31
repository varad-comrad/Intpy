import numpy as np

def f(A, x):
    x0 = np.log(np.dot(A, np.exp(x)))
    x0 -= np.log(np.sum(np.exp(x0)))
    return x0


def belief_propagation(N):
    dim = 5000
    A = np.random.rand(dim, dim)
    x = np.ones((dim,))
    for i in range(N):
        x = f(A, x)
    return x
