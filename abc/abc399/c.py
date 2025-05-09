class UnionFind:
    def __init__(self, n):
        self.root = [-1] * (n + 1)
        self.size = [1] * (n + 1)
    
    def find(self, x):
        while self.root[x] != -1:
            x = self.root[x]
        return x
    
    def unite(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.size[root_u] < self.size[root_v]:
            self.root[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.root[root_v] = root_u
            self.size[root_u] += self.size[root_v]
    
    def same(self, u, v):
        return self.find(u) == self.find(v)
    
    def root_size(self):
        root_size = []
        for i in range(1, len(self.root)):
            if self.root[i] == -1:
                root_size.append(self.size[i])
        return root_size


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    uf = UnionFind(n)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        uf.unite(u, v)
    
    root_size = uf.root_size()
    ans = m
    for i in range(len(root_size)):
        ans -= root_size[i] - 1
    print(ans)


if __name__ == "__main__":
    main()
