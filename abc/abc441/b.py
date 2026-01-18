N, M = map(int, input().split())
S = input()
T = input()

Takahashi_language = set(list(S))
Aoki_language = set(list(T))

Q = int(input())

for _ in range(Q):
    w = input()
    t_flag = all(c in Takahashi_language for c in w)
    a_flag = all(c in Aoki_language for c in w)

    if t_flag and not a_flag:
        print('Takahashi')
    elif a_flag and not t_flag:
        print('Aoki')
    else:
        print('Unknown')
