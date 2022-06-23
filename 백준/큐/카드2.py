from collections import deque

n = 6
cards = deque([i for i in range(1, n+1)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])