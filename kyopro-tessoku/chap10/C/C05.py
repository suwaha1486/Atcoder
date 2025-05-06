n = int(input())

n -= 1
xor_mask = 1023
binary_result = f'{n ^ xor_mask:010b}'

new_result_str = ""
for bit in binary_result:
    if bit == '1':
        new_result_str += '4'
    else: 
        new_result_str += '7'
result = int(new_result_str)

print(result)