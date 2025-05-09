# give up
def couple_cnt(n, a):
    # 各数字の位置を記録
    position = [[] for _ in range(n + 1)]
    for i in range(2 * n):
        position[a[i]].append(i)
    
    # 答えを格納する集合
    answers = set()
    
    # 隣接する2つの数字について調べる
    for i in range(2 * n - 1):
        a_val = a[i]
        b_val = a[i + 1]
        
        # 同じ数字が既に隣接している場合はスキップ
        if position[a_val][0] + 1 == position[a_val][1]:
            continue
        if position[b_val][0] + 1 == position[b_val][1]:
            continue
        
        # 4つの位置をソート
        v = [position[a_val][0], position[a_val][1], 
             position[b_val][0], position[b_val][1]]
        v.sort()
        
        # 隣接する2組のカップルが作れるかチェック
        if v[0] + 1 == v[1] and v[2] + 1 == v[3]:
            answers.add((min(a_val, b_val), max(a_val, b_val)))
    
    return len(answers)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(couple_cnt(n, a))

if __name__ == "__main__":
    main()
