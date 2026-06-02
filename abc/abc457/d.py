N, K = map(int, input().split())
A = list(map(int, input().split()))

# 答えの二分探索
# left = min(A)
# right = A[0] + K

def check(x):
    # x以上にするために必要な操作回数
    count = 0

    for i in range(N):
        if x > A[i]:
            count += (x - A[i] + i) // (i + 1)
            if count > K:
                return False

    return count <= K

left = min(A)
right = A[0] + K + 1

while right - left > 1:
    mid = (left + right) // 2

    if check(mid):
        left = mid
    else:        
        right = mid

print(left)