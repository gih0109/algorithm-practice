import sys
sys.stdin = open(r"분할 정복\test.txt", "r")

a, b, c = map(int, input().split())
# print(a, b, c)

dy_dict = {}

def tree(a, b):
    if b <= 2:
        dy_dict.setdefault(b, 0)
        dy_dict[b] = (a**b) % c
        return dy_dict[b]
    else:
        dy_dict.setdefault(b, 0)
        if b % 2 == 0:
            if dy_dict[b] > 0:
                return dy_dict[b]
            else:
                dy_dict[b] = (tree(a, b//2) ** 2) % c
                return dy_dict[b]
        else:
            if dy_dict[b] > 0:
                return dy_dict[b]
            else:
                dy_dict[b] = (tree(a, (b-1)//2) * tree(a, (b-1)//2) * tree(a, 1)) % c
                return dy_dict[b]

print(tree(a, b))