n = 0

def factorial(a: int, b: int):
    if a == n:
        if n == 0:
            print(1)
        else:
            print(b)
    else:
        factorial(a+1, b * (a+1))

factorial(0, 1)