def twoCitySchedCost(costs):
    costs = sorted(costs, key=lambda x: x[0] - x[1])
    sum = 0
    for i in range(len(costs)):
        if i < (len(costs) / 2):
            sum += costs[i][0]
        else:
            sum += costs[i][1]
    return sum

print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
