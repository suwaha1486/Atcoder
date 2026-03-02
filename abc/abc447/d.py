from collections import deque

S = input()

A_que = deque()
B_que = deque()
C_que = deque()

for i in range(len(S)):
    if S[i] == 'A':
        A_que.append(i)
    elif S[i] == 'B':
        B_que.append(i)
    elif S[i] == 'C':
        C_que.append(i)

ans = 0
while len(A_que) > 0 and len(B_que) > 0 and len(C_que) > 0:
    if A_que[0] < B_que[0] < C_que[0]:
        ans += 1
        A_que.popleft()
        B_que.popleft()
        C_que.popleft()
    elif A_que[0] > B_que[0]:
        B_que.popleft()
    elif B_que[0] > C_que[0]:
        C_que.popleft()

print(ans)