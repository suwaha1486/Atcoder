n = list(input())
cnt1 = 0
cnt2 = 0
cnt3 = 0
for i in range(len(n)):
    if n[i] == "1":
        cnt1 += 1
    elif n[i] == "2":
        cnt2 += 1
    elif n[i] == "3":
        cnt3 += 1

if cnt1 == 1 and cnt2 == 2 and cnt3 == 3:
    print("Yes")
else:
    print("No")