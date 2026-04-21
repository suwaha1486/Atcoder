def process_paren_xx(s):
    stack = []
    for ch in s:
        stack.append(ch)
        # 末尾4文字が "(xx)" なら "xx" に畳み込む
        while (
            len(stack) >= 4
            and stack[-4] == '('
            and stack[-3] == 'x'
            and stack[-2] == 'x'
            and stack[-1] == ')'
        ):
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('x')
            stack.append('x')
    return stack

T = int(input())

for _ in range(T):
    A = input()
    B = input()

    A_que = process_paren_xx(A)
    B_que = process_paren_xx(B)
    
    if A_que == B_que:
        print("Yes")
    else:
        print("No")