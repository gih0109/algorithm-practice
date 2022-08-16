from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    while progresses:
        # 작업완료된 작업을 앞에서부터 pop
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
        
        # 작업진도 더하기
        for idx in range(len(progresses)):
            progresses[idx] += speeds[idx]
            
    return answer