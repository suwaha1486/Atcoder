q = int(input())
query = []
for i in range(q):
    query.append(list(map(int, input().split())))

head_pos = 0
snake_list = [0]
for i in range(q):
    if query[i][0] == 1:
        # 累積長
        snake_list.append(snake_list[-1] + query[i][1])

    elif query[i][0] == 2:
        # 先頭１つ後ろに
        head_pos += 1

    elif query[i][0] == 3:
        print(snake_list[head_pos + query[i][1]-1] - snake_list[head_pos])