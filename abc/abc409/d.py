def solve(s, n):
    for j in range(n-1):
        pre = ord(s[j])
        post = ord(s[j+1])
        if pre > post:
            for k in range(j+1, n):
                if ord(s[k]) > pre:
                    s.insert(k, s[j])
                    s.pop(j)
                    return s
            s.append(s[j])
            s.pop(j)
            return s
    return s

t = int(input())

for i in range(t):
    n = int(input())
    s = list(input())
    print("".join(solve(s, n)))
    