# Resolvendo da forma recursiva
def fib(n): 
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib (n - 2)
    

# Resolvendo na forma da Programacao Dinamica
def dyna_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if lookup[n] is not None:
        return lookup[n]
    
    lookup[n] = dyna_fib(n - 1) + dyna_fib(n-2)
    return lookup[n]

lookup = [None] * 1000

print (dyna_fib(1000))
