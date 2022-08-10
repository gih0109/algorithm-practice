T = int(input())

def check_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    else:
        return True

for _ in range(T):
    n = int(input())

    for i in range(n//2):
        a, b = (n // 2) - i, (n // 2) + i
        if check_prime(a) and check_prime(b):
            print(a, b)
            break


