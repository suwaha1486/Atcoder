N, Q = map(int, input().split())
A = [0] * N
ans = 0
not_0_idx = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        idx = query[1] - 1
        
        if A[idx] == 0:
            not_0_idx.append(idx)
        
        ans ^= A[idx]
        ans ^= A[idx] + 1
        A[idx] += 1
    
    elif query[0] == 2:
        new_idx = []
        for idx in not_0_idx:
            ans ^= A[idx]
            ans ^= A[idx] - 1
            A[idx] -= 1
            if A[idx] != 0:
                new_idx.append(idx)
        not_0_idx = new_idx

    print(ans)