from collections import deque
import heapq as hq

def solution(jobs):
    n = len(jobs)
    jobs = deque(jobs)
    heap = []
    working = []
    time, sum_time = 0, 0 # 시간, 요청부터 종료까지 시간 합
    cnt = 0 # 작업하는데 걸리는 시간
    while working or jobs:
        while jobs and time >= jobs[0][0]: # 작업대기줄에 집어넣기
            cur = jobs.popleft()
            hq.heappush(heap, (cur[1], cur[0]))

        if working and working[0][0] == cnt: # 작업 완료 시
            sum_time += time - working[0][1]
            working.pop()

        if heap and not working: # 작업대기줄이 있고 작업중이 아닐 때
            working.append(hq.heappop(heap))
            cnt = 0

        time += 1
        cnt += 1

    return sum_time // n

if __name__ == "__main__":
    jobs = [[10, 10], [30, 10], [50, 2], [51, 2]]
    print(solution(jobs))