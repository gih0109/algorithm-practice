n, k = 5, 2
p = 1000000007

def factorial(n, p):
    mul_val = 1
    for i in range(2, n+1):
       mul_val *= i
       mul_val %= p
    return mul_val 

def power(x, a, p):
    if a == 1:
        return x % p
    else:
        if a % 2 == 0:
            return (power(x, a//2, p) ** 2) % p
        else:
            return ((power(x, a//2, p) ** 2) * x) % p

print(factorial(n, p) * power(factorial(k, p) * factorial(n-k, p), p-2, p) % p)
