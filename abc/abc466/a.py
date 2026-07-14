N = int(input())
X = list(map(int, input().split()))
if all(x < 0 for x in X):
    print("Yes")
else:
    print("No")