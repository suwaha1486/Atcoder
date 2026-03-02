S = input()
T = input()

# 操作1:Sの好きな位置に文字Aを挿入
# 操作2:Sに含まれる文字Aを1つ削除
# 目的：SをTに一致させられるか判定，できるなら最小回数を求める

# 文字列SとTに含まれる，A以外の文字の順序が一致しているか判定
S_notA = S.replace('A', '')
T_notA = T.replace('A', '')

if S_notA != T_notA:
    print(-1)
    exit()

# A以外の文字に挟まれたAの個数をそれぞれ求め，その差を求める
S = '.' + S + '.'
T = '.' + T + '.'

S_A_count_list = []
T_A_count_list = []
A_count_tmp = 0
for i in range(len(S)):
    if S[i] == 'A':
        A_count_tmp += 1
    else:
        S_A_count_list.append(A_count_tmp)
        A_count_tmp = 0

A_count_tmp = 0
for i in range(len(T)):
    if T[i] == 'A':
        A_count_tmp += 1
    else:
        T_A_count_list.append(A_count_tmp)
        A_count_tmp = 0

ans = 0
for i in range(len(S_A_count_list)):
    ans += abs(S_A_count_list[i] - T_A_count_list[i])

print(ans)