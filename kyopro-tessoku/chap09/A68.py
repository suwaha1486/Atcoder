import sys
sys.setrecursionlimit(10**6)

class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

class MaximumFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(self.n + 1)]
    
    def add_edge(self, u, v, cap):
        forward_edge = maxflow_edge(v, cap, len(self.graph[v]))
        self.graph[u].append(forward_edge)
        backward_edge = maxflow_edge(u, 0, len(self.graph[u]) - 1)
        self.graph[v].append(backward_edge)
    
    def dfs(self, start, target, f):
        if start == target:
            return f
        self.visited[start] = True

        for edge in self.graph[start]:
            if edge.cap > 0 and not self.visited[edge.to]:
                flow = self.dfs(edge.to, target, min(f, edge.cap))
                if flow > 0:
                    edge.cap -= flow
                    reverse_edge = self.graph[edge.to][edge.rev]
                    reverse_edge.cap += flow
                    return flow
        return 0
    
    def solve(self, start, target):
        total_flow = 0
        
        while True:
            self.visited = [False] * (self.n + 1)
            flow = self.dfs(start, target, float('inf'))
            if flow == 0:
                break
            total_flow += flow

        return total_flow


def main():
    n, m = map(int, input().split())
    maxflow = MaximumFlow(n)

    for _ in range(m):
        u, v, c = map(int, input().split())
        maxflow.add_edge(u, v, c)

    ans = maxflow.solve(1, n)
    print(ans)

if __name__ == '__main__':
    main()