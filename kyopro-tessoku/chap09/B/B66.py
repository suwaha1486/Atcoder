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
a = []
b = []

for _ in range(m):
    u, v = map(int, input().split())
    a.append(u)
    b.append(v)

q = int(input())
querys = []
not_cut = []

for i in range(q):
    query = list(map(int, input().split()))
    querys.append(query)
    if query[0] == 1:
        not_cut.append(query[1] - 1)
    
uf = UnionFind(n)

not_cut.sort()
j = 0
for i in range(m):
    if i == not_cut[j]:
        j = min(j + 1, len(not_cut) - 1)
        continue
    
    u, v = a[i], b[i]
    uf.unite(u, v)

ans = []
for i in range(q-1, -1, -1):
    query = querys[i]
    if query[0] == 1:
        u, v = a[query[1]-1], b[query[1]-1]
        uf.unite(u, v)
    else:
        u, v = query[1], query[2]
        if uf.same(u, v):
            ans.append("Yes")
        else:
            ans.append("No")

ans.reverse()
for i in range(len(ans)):
    print(ans[i])