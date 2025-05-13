s = input()
q = int(input())
K = list(map(int, input().split()))

ans = []
for k in K:
    k -= 1
    blk = k // len(s)
    pt = k % len(s)

    # give up -> 思いつかなかった
    # blockの2進数での1の数が奇数なら反転、偶数ならそのまま
    if bin(blk).count('1') % 2:
        ans.append(s[pt].swapcase())
    else:
        ans.append(s[pt])

print(*ans)