from collections import defaultdict
answer = []

def dfs(graph: dict, city: str, n: int, result: list) -> list:

    if len(result) == n:
        answer[:] = result[:]
        return

    else:
        for n_city in graph[city]:
            result.append(n_city)
            dfs(graph, n_city, n, result)
            result.pop()


def solution(tickets: list) -> list:
    tickets.sort()
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)

    for key, val in graph.items():
        graph[key] = sorted(val)

    n = len(tickets)

    dfs(graph, "ICN", n, ["ICN"])
    return answer


if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    print(solution(tickets))
    