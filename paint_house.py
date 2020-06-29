class Solution:
    def minCost(self, costs):
        if not costs:
            return 0

        if len(costs) == 1:
            return min(costs[0])

        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][1], costs[i - 1][0])

        return min(costs[-1])
