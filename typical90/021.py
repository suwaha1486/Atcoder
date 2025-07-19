# ★5
# WA submission
# 1 -> 2 -> 3
# 3 -> 4 -> 1
# パスを考慮できていない
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

n, m = map(int, input().split())

if m == 1:
    print(0)
    exit()

edges = []

for i in range(m):
    a, b = map(int, input().split())
    c = 0
    if a > b:
        a, b = b, a
        c = 1
    edges.append((a, b, c))

edges.sort()

uf = UnionFind(n)
for i in range(1, m):
    if edges[i][0] == edges[i-1][0] and edges[i][1] == edges[i-1][1] and edges[i][2] + edges[i-1][2] == 1:
        uf.unite(edges[i][0], edges[i][1])

root_size = uf.root_size()

ans = 0
for i in range(len(root_size)):
    ans += root_size[i] * (root_size[i] - 1) // 2

print(ans)