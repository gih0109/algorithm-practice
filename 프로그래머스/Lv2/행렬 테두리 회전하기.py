from collections import deque

def solution(rows, columns, queries):
    num = 1
    matrix = [[] for _ in range(rows)]
    for i in range(rows):
        for _ in range(columns):
            matrix[i].append(num)
            num += 1
    print(matrix)
    
    result = []
    for query in queries:
        x1, y1, x2, y2 = query
        a, b = x2 - x1, y2 - y1
        # print(a, b)
        tmp_list = []
        num_list = deque()

        # 회전할 좌표 리스트로 만들기
        cnt = 0
        tmp_x, tmp_y = x1, y1
        for _ in range((a + b) * 2):
            tmp_list.append((tmp_x, tmp_y))
            if cnt < b:
                tmp_y += 1
            elif b <= cnt < a + b:
                tmp_x += 1
            elif a + b <= cnt < (2 * b) + a:
                tmp_y -= 1
            else:
                tmp_x -= 1
            cnt += 1

        print(tmp_list)
        # 좌표 리스트에서 숫자 리스트 만들기 및 최소값 확인
        min_val = 10001
        for i, j in tmp_list:
            num_list.append(matrix[i-1][j-1])
            if matrix[i-1][j-1] < min_val:
                min_val = matrix[i-1][j-1]
        result.append(min_val)

        # 회전
        num_list.appendleft(num_list.pop())

        # 회전한 숫자를 다시 좌표에 넣기
        for idx, val in enumerate(tmp_list):
            i, j = val
            matrix[i-1][j-1] = num_list[idx]

    return result

if __name__ == "__main__":
    rows = 6
    columns = 6
    # queries = [[2,2,5,4]]
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    print(solution(rows, columns, queries))