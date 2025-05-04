s = input()

stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append([s[i], i+1])
    else:
        print(stack[-1][1], i+1)
        stack.pop()