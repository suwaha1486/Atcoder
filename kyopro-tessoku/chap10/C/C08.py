n = int(input())

st = []
for i in range(n):
    s, t = input().split()
    t = int(t)
    if t == 1:
        print(s)
        exit()
    st.append([s, t])

ans = []

for i in range(10000):
    num = f'{i:04d}'
    flg = True
    for s, t in st:
        cnt = 0
        for j in range(4):
            if num[j] != s[j]:
                cnt += 1
        if t == 2 and cnt != 1:
            flg = False
        elif t == 3 and cnt < 2:
            flg = False
    if flg:
        ans.append(num)

if len(ans) > 1:
    print("Can't Solve")
else:
    print(ans[0])