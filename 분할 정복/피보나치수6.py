n = 1000
p = 1000000007
a = [[1, 1], [1, 0]]

def matrix_mul(x: list, y: list) -> list:
    result = [[0] * (len(y[0])) for _ in range(len(x[0]))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(x[0])):
                result[i][j] += x[i][k] * y[k][j]
            result[i][j] %= p 
    return result

# text_matrix = [[2], [1]]
# # print(len(text_matrix[0]))

# print(matrix_mul(a, text_matrix))

def fibo(n):
    if n == 1:
        return a
        
    tmp = fibo(n//2)
    if n % 2 == 0:
        return matrix_mul(tmp, tmp)
    else:
        return matrix_mul(matrix_mul(tmp, tmp), a)

print(fibo(n)[0][1])