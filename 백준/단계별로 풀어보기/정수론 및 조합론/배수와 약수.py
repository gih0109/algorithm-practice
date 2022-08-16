x, y = map(int, input().split())

while (x, y) != (0, 0):
    if x % y == 0:
        print("multiple")
    elif y % x == 0:
        print("factor")
    else:
        print("neither")
    
    x, y = map(int, input().split())