def check(a, mid, k):
    count = 0
    prev_pos = 0
    for i in range(1, len(a)):
        if a[i] - a[prev_pos] >= mid:
            count += 1
            prev_pos = i
        
    if count > k:
        return True
    else:
        return False


def main():
    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))

    a = [0] + a + [l]
    
    left = 0
    right = l

    while left + 1 < right:
        mid = (left + right) // 2
        if check(a, mid, k):
            left = mid
        else:
            right = mid

    print(left)

if __name__ == "__main__":
    main()