# WA 貪欲解法であり，最適解でない可能性あり

# 目標：全ての頂点の次数が2である単純無向グラフにする

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

cnt = 0

# 次数が2未満の頂点のセット
less_than_2 = set()

# 無向辺の削除
for i in range(n):
    # 次数が2未満の頂点のリストに追加
    if len(graph[i]) < 2:
        less_than_2.add(i)

    # 1. 次数が3以上の頂点を探す
    if len(graph[i]) >= 3:
        # 接続先の次数が多い順にソート
        neighbors = sorted(graph[i], key=lambda x: len(graph[x]), reverse=True)
        
        # 次数が2になるまで辺を削除
        while len(graph[i]) > 2:
            for neighbor in neighbors:
                if neighbor in graph[i]:
                    graph[neighbor].remove(i)
                    graph[i].remove(neighbor)

                    # 削除回数をカウント
                    cnt += 1
                    
                    if len(graph[neighbor]) < 2:
                        less_than_2.add(neighbor)
                    break

# 次数が2未満の頂点がなければ出力
if len(less_than_2) == 0:
    print(cnt)
    exit()

# 部分的な閉回路になっている場合，その閉回路の辺を削除
# この時点で全ての頂点の次数が2以下である
# 次数が2の頂点を辿り，閉回路を探す
visited = [False] * n

for i in range(n):
    if len(graph[i]) == 2 and not visited[i]:
        v = i
        start = i
        visited[v] = True
        path = [v]
        
        # 次数が2の頂点を辿って閉回路を探す
        while True:
            next_v = None
            for neighbor in graph[v]:
                # 開始点に戻ってきた場合の特別処理
                if neighbor == start and len(path) > 2:
                    # 閉回路が見つかった
                    # 閉回路の一つの辺を削除
                    graph[start].remove(v)
                    graph[v].remove(start)
                    cnt += 1
                    # 次数が2未満の頂点のセットに追加
                    less_than_2.add(v)
                    less_than_2.add(start)
                    break
                elif len(graph[neighbor]) == 2 and neighbor not in path:
                    next_v = neighbor
                    break
            
            if next_v is None:
                # 閉回路が見つからない場合
                break
            
            v = next_v
            visited[v] = True
            path.append(v)
        
# 無向辺の追加
edge_to_add = 0
for v in less_than_2:
    if len(graph[v]) == 0:
        edge_to_add += 2
    elif len(graph[v]) == 1:
        edge_to_add += 1

cnt += edge_to_add // 2

print(cnt)
