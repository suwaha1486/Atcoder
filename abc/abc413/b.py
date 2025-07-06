n = int(input())

s = []
for i in range(n):
    s.append(input())

concat = set()
for i in range(n):
    for j in range(n):
        if i != j:
            concat.add(s[i] + s[j])

print(len(concat))
