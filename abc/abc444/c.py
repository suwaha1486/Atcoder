N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

# 1. 長さLである1本として残っている
# 1の場合，長さLの候補は最長のもののみ
# 長さL以外の棒で，小さい方と大きい方からペアを作成し，
# 全てのペアがLとなればLが一つ目の答え
max_len = A[0]
ans = [max_len]

idx = N-1
for i in range(1, N):
    # 長さLの候補と一致している場合
    if A[i] == max_len:
        continue

    # 全てのペアの長さの合計がLになる必要がある
    # ペアにならない場合もダメ
    elif A[i] + A[idx] != max_len:
        ans.pop()
        break
    
    elif A[i] + A[idx] == max_len:
        idx -= 1
        if i + 1 == idx:   # 1本余る => ダメ
            ans.pop()
            break
        if i >= idx:       # すべて消費できた => OK
            break

# 2. 長さの和がLであるような2本に分かれた
# 2の場合，最小のものと最大のものを順番にペアにしていく
# 全てのペアの長さの合計がLになる必要がある
# ペアにならない場合もダメ
if N % 2 == 0:
    max_len = A[0] + A[N-1]
    ans.append(max_len)
    for i in range(N//2+1):
        if A[i] + A[N-i-1] != max_len:
            ans.pop()
            break

print(*ans, sep=' ')
        