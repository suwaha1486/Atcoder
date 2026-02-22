from collections import deque

T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    q = deque()
    for i in range(N):
        q.append((i, A[i]))

    for i in range(N):
        while q[0][0] < i - D:
            q.popleft()
        
        Used_sum = 0
        while Used_sum < B[i] and q[0][0] <= i:
            Used_sum += q[0][1]
            tmp_index = q[0][0]
            q.popleft()
        q.appendleft((tmp_index, Used_sum - B[i]))

    while q[0][0] < N - D:
        q.popleft()
        
    ans = 0
    for q_i in q:
        ans += q_i[1]
    print(ans)