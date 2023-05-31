def pow(n, m):
    if m == 0:
        return 1
    return n*pow(n, m-1)
