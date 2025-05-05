def black_count(c, h, w, remain_k):
    w_count = []
    for j in range(w):
        col_sum = sum(c[i][j] for i in range(h))
        w_count.append((col_sum, j))

    w_count.sort()

    for k in range(remain_k):
        col_index = w_count[k][1]
        for i in range(h):
            c[i][col_index] = 1 
    
    total_black = sum(sum(row) for row in c)

    return total_black


def main():
    h, w, k = map(int, input().split())
    c = []

    for i in range(h):
        c.append([1 if x == '#' else 0 for x in list(input())])
    
    ans = 0

    for i in range(2 ** h):
        c_tmp = [list(c[i]) for i in range(h)]
        remain_k = k
        for j in range(h):
            if (i >> j) & 1:
                c_tmp[j] = [1] * w
                remain_k -= 1

        if remain_k >= 0:
            cnt = black_count(c_tmp, h, w, remain_k)
            ans = max(ans, cnt)

    print(ans)

if __name__ == "__main__":
    main()