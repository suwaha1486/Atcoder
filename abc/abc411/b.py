n = int(input())
d = list(map(int, input().split()))

for i in range(n-1):
    cum_d = [d[i]]
    for j in range(i+1, n-1):
        cum_d.append(cum_d[-1] + d[j])
    
    print(*cum_d)