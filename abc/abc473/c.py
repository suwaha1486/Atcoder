N, K = map(int, input().split())
A = list(map(int, input().split()))

class_size = [0] * K

for i in range(N):
    class_size[A[i] - 1] += 1

max_class_size = max(class_size)
ans = class_size.count(max_class_size)
ans += class_size.count(max_class_size - 1)
print(ans)