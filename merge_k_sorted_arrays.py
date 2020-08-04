from heapq import heappush, heappop


def merge(lists):
    min_heap = []
    for lst in lists:
        for num in lst:
            heappush(min_heap, num)

    res = []

    while len(min_heap):
        res.append(heappop(min_heap))

    return res

print(merge([[3,5,7], [0,6], [0,6,8]]))