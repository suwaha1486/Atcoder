# ★4
from collections import deque

def bfs(s, graph):
    n = len(graph)
    q = deque()
    dist = [-1] * n
    q.append(s)
    dist[s] = 0

    while len(q) > 0:
        v = q.popleft()
        for u in graph[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)

    max_dist = max(dist)
    farthest_node = dist.index(max_dist)
    return farthest_node, max_dist
    
def main():
    n = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    farthest_node, _ = bfs(1, graph)
    farthest_node, max_dist = bfs(farthest_node, graph)
    
    print(max_dist + 1)

if __name__ == "__main__":
    main()
