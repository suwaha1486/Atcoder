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

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
length = []

for i in range(m):
    a, b, c = map(int, input().split())
    length.append([c, a, b])

length.sort(reverse=True)    

uf = UnionFind(n)

ans = 0
for i in range(m):
    c, a, b = length[i]
    if not uf.same(a, b):
        ans += c
        uf.unite(a, b)

print(ans)