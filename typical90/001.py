# ★4
def check(x, a, k):
    cnt = 0
    tmp = 0
    for i in range(len(a)):
        if a[i] - tmp >= x:
            cnt += 1
            tmp = a[i]
    if cnt >= k + 1:
        return True
    else:
        return False

def main():
    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))
    a.append(l)

    left = 1
    right = l
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid, a, k):
            left = mid
        else:
            right = mid
    print(left)

if __name__ == "__main__":
    main()
