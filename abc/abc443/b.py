N, K = map(int, input().split())

beans_sum = 0
years = 0

while K > beans_sum:
    beans_sum += N + years
    years += 1

print(years - 1)
