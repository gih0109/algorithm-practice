from collections import defaultdict
answer = []

def dfs(graph: dict, city: str, n: int, result: list):
    if len(answer) == n + 1:
        return
    
    if len(result) == n + 1:
        answer[:] = result[:]
        return
    
    else:
        for idx, n_city in enumerate(graph[city]):
            graph[city].pop(idx)
            result.append(n_city)
            dfs(graph, n_city, n, result)
            graph[city].insert(idx, n_city)
            result.pop()


def solution(tickets: list) -> list:
    global answer

    tickets.sort()
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)

    for key, val in graph.items():
        graph[key] = sorted(val)

    n = len(tickets)
    print(graph)

    result = ["ICN"]
    dfs(graph, "ICN", n, result)

    return answer


if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    print(solution(tickets))
    