H, W = map(int, input().split())
bmi = W * 10000 / H / H

if bmi < 25:
    print("No")
else:
    print("Yes")