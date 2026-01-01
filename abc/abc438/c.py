n = int(input())
a = list(map(int, input().split()))

stack = []

for i in range(n):
    stack.append(a[i])
    if len(stack) >= 4 and stack[-1] == stack[-2] == stack[-3] == stack[-4]:
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()

print(len(stack))