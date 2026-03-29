from heapq import heappush, heappop

Q = int(input())

tree_heap = []

for _ in range(Q):
    q, h = map(int, input().split())

    if q == 1:
        heappush(tree_heap, h)

    elif q == 2:
        while tree_heap and tree_heap[0] <= h:
            heappop(tree_heap)
    
    print(len(tree_heap))