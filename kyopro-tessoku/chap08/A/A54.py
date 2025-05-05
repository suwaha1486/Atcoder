q = int(input())

score = dict()

for i in range(q):
    query = list(input().split())
    if query[0] == '1':
        score[query[1]] = query[2]
    elif query[0] == '2':
        print(score[query[1]])