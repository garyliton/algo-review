from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        for time in times:
            node = time[0]
            neighbour = time[1]
            distance = time[2]
            graph[node].append([neighbour, distance])

        pq = []
        heappush(pq, (0, K))

        visited = {}
        while len(pq) != 0:
            d1, node = heappop(pq)
            if node in visited:
                continue
            visited[node] = d1
            for nei, d2 in graph[node]:
                heappush(pq, (d1 + d2, nei))

        if len(visited) == N:
            return max(visited.values())
        else:
            return -1
