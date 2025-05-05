q = int(input())

stack = []

for i in range(q):
    query = list(input().split())
    if query[0] == "1":
        stack.append(query[1])
    elif query[0] == "2":
        print(stack[-1])
    elif query[0] == "3":
        stack.pop()