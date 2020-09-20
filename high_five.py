from heapq import heappush, heappop


class Solution:
    def highFive(self, items):
        students = {}

        for item in items:
            if item[0] not in students:
                min_heap = []
                heappush(min_heap, item[1])
                students[item[0]] = min_heap
            else:
                heappush(students[item[0]], item[1])
                if len(students[item[0]]) > 5:
                    heappop(students[item[0]])

        res = students.keys()

        res = map(lambda x: [x, sum(students[x])//5], res)

        return list(res)

s = Solution()
print(s.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))