a, b = map(int, input().split())

a_div_b = a / b
up = int(a_div_b)
down = up + 1

up_diff = abs(up - a_div_b)
down_diff = abs(down - a_div_b)

if up_diff <= down_diff:
    print(up)
else:
    print(down)
