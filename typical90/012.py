# 毎回bfsでやるとTLEになるので、UnionFindを使う
# 繋がっているかどうかを確認する場合はUnionFindを使う

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

h, w = map(int, input().split())
q = int(input())

square = [[0] * w for _ in range(h)]
uf = UnionFind(h * w)

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        r, c = query[1] - 1, query[2] - 1
        square[r][c] = 1
        current = r * w + c
        
        if r > 0 and square[r - 1][c] == 1:
            uf.unite(current, (r - 1) * w + c)
        if r < h - 1 and square[r + 1][c] == 1:
            uf.unite(current, (r + 1) * w + c)
        if c > 0 and square[r][c - 1] == 1:
            uf.unite(current, r * w + c - 1)
        if c < w - 1 and square[r][c + 1] == 1:
            uf.unite(current, r * w + c + 1)

    elif query[0] == 2:
        ra, ca, rb, cb = query[1] - 1, query[2] - 1, query[3] - 1, query[4] - 1
        if square[ra][ca] == 0 or square[rb][cb] == 0:
            print("No")
        elif ra == rb and ca == cb:
            print("Yes")
        else:
            if uf.same(ra * w + ca, rb * w + cb):
                print("Yes")
            else:
                print("No")
