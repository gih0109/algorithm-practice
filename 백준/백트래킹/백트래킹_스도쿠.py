import sys
sys.stdin = open(r"input.txt", "r")

def sudoku_func(sudoku):
    pass
    # 





if __name__ == "__main__":
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    for i in sudoku:
        print(i)