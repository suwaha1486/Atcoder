S = input()

cnt_E = 0
cnt_W = 0

for i in range(len(S)):
    if S[i] == "E":
        cnt_E += 1
    elif S[i] == "W":
        cnt_W += 1

if cnt_E > cnt_W:
    print("East")
else:
    print("West")