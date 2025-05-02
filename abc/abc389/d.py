r = int(input())

upper = r-1
ans = 0

for i in range(1, r):
    while 2*upper*upper+2*upper+2*i*i+2*i+1 > 2*r*r:
        upper -= 1
    ans += upper+1

print(4 * ans + 1)