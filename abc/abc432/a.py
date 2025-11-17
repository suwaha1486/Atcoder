num = list(map(int, input().split()))
num.sort(reverse=True)

print(num[0] * 100 + num[1] * 10 + num[2])