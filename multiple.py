def mul(*args):
    n = 1
    
    for i in args:
        n *= i

    return n

print(mul(2, 3, 4))
