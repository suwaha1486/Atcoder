N = int(input())
A = [0] + list(map(int, input().split()))

# 訪問履歴情報を活用．
# 今のままだとTLE
result_list = [None] * (N + 1)

for i in range(1, N + 1):
    if result_list[i] is not None:
        continue

    start_pos = i
    loop_list = [start_pos]
    loop_set = set(loop_list)
    next_pos = A[start_pos]
    flg_absorb = False

    while next_pos != start_pos:
        # 吸収状態がある場合，そのマスで終了
        if next_pos == A[next_pos]:
            flg_absorb = True
            for j in loop_set:
                result_list[j] = next_pos
            break

        loop_list.append(next_pos)
        loop_set.add(next_pos)
        next_pos = A[next_pos]
    
    if not flg_absorb:
        for j in range(len(loop_list)):
            result_list[loop_list[j]] = loop_list[(10 ** 100 - 1) % len(loop_list) + j]

for i in range(1, N + 1):
    print(result_list[i])