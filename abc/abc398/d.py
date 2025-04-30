n, r, c = map(int, input().split())
s = input()

'''
方針
・高橋を動かす
・煙は発生時点がずれるだけで，動かない
→煙を集合で管理

'''

r_s = 0
c_s = 0 
ans =[]
smoke = set()
smoke.add((r_s, c_s))

for i in range(n):
    if s[i] == 'N':
        r_s += 1
        r += 1
    elif s[i] == 'W':
        c_s += 1
        c += 1
    elif s[i] == 'S':
        r_s -= 1
        r -= 1
    elif s[i] == 'E':
        c_s -= 1
        c -= 1
    
    smoke.add((r_s, c_s))
        
    if (r, c) in smoke:
        ans.append(1)
    else:
        ans.append(0)

print(*ans, sep='')