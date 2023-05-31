import numpy as np

def compute_FFT(n):
    A = np.eye(n) + 1j * np.eye(n)
    result = np.fft.fft2(A)
    return np.abs(result)
