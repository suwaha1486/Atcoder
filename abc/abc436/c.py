n, m = map(int, input().split())

used = set()
ans = 0

for i in range(m):
    r, c = map(int, input().split())
    cells = [(r-1, c-1), (r, c-1), (r-1, c), (r, c)]

    if any(cell in used for cell in cells):
        continue

    for cell in cells:
        used.add(cell)
    ans += 1

print(ans)