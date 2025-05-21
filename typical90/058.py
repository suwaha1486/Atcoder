n, k = map(int, input().split())

def calc_digit_sum(x):
    y = 0
    while x > 0:
        y += x % 10
        x //= 10
    return y

value_to_position = {}
position_to_value = {0: n}
x = n
current_position = 0

while True:
    if x in value_to_position:
        cycle_start = value_to_position[x]
        cycle_length = current_position - cycle_start
        break
    value_to_position[x] = current_position
    y = calc_digit_sum(x)
    x = (x + y) % (10 ** 5)
    current_position += 1
    position_to_value[current_position] = x

if k <= current_position:
    print(position_to_value[k])
else:
    k_position_in_cycle = cycle_start + ((k - cycle_start) % cycle_length)
    print(position_to_value[k_position_in_cycle])
