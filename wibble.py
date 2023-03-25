def wibble(n):
    return 17 / n

def frob(n):
    return wibble(n) + wibble(n)

print(frob(10))