N, K = map(int, input().split())

A = [0] * N

def dfs(i, rem):
    if i == N:
        if rem % N == 0:
            A[N - 1] = rem // N
            print(*A)
            return
    
    else:
        for x in range(rem // i + 1):
            A[i - 1] = x
            dfs(i + 1, rem - i * x)
        
dfs(1, K)