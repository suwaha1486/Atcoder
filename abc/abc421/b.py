def reverse_number(n):
    return int(str(n)[::-1])

x, y = map(int, input().split())

for i in range(8):
    z = reverse_number(x + y)
    x = y
    y = z

print(z)
