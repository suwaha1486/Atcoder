from collections import deque

def bfs(start, end, graph):
    dist = [-1] * len(graph)
    dist[start] = 0
    q = deque()
    q.append(start)

    while len(q) > 0:
        v = q.popleft()
        for u in graph[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)
    
    return dist[end]

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    start = 0
    for i in range(n):
        start += 2 ** i * a[i]
    end = 2 ** n - 1

    xyz = []
    for i in range(m):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        z -= 1
        xyz.append((2 ** x + 2 ** y + 2 ** z))

    graph = [[] for _ in range(2 ** n)]
    for i in range(2 ** n):
        for j in range(m):
            graph[i].append(i ^ xyz[j])
    
    print(bfs(start, end, graph))

if __name__ == "__main__":
    main()