N = int(input())
A = list(map(int, input().split()))

A3 = A[0:3]
A3.sort()
print(A3[0])

# 数列の中で3番目に大きな数字を返す
# 3つの数字を管理
# その中で最小の数字と比較して、最小の数字より大きい場合は、最小の数字を削除して、新しい数字を追加
for i in range(3, N):
    if A3[0] < A[i]:
        A3[0] = A[i]
        A3.sort()
    print(A3[0])
