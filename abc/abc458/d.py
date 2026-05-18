import heapq

X = int(input())
Q = int(input())

# small_heap: i + 1個
# large_heap: i個

small_heap = [-X]
large_heap = []

heapq.heapify(small_heap)
heapq.heapify(large_heap)

mid = X
for _ in range(Q):
    a, b = map(int, input().split())
    if a < mid:
        heapq.heappush(small_heap, -a)
    else:
        heapq.heappush(large_heap, a)

    if b < mid:
        heapq.heappush(small_heap, -b)
    else:
        heapq.heappush(large_heap, b)
    
    # small_heapとlarge_heapのサイズを調整
    while len(small_heap) > len(large_heap) + 1:
        heapq.heappush(large_heap, -heapq.heappop(small_heap))
    
    while len(large_heap) + 1 > len(small_heap):
        heapq.heappush(small_heap, -heapq.heappop(large_heap))
    
    mid = -small_heap[0]
    print(mid)