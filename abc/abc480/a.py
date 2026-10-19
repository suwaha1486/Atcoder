S = [list(input()) for _ in range(2)]

for i in range(2):
    for j in range(2):
        if S[i][j] == "A":
            if S[(i + 1) % 2][j] == "D" or S[i][(j + 1) % 2] == "D":
                print("Yes")
                exit()

print("No")