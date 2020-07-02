def dietPlanPerformance(calories, k, lower, upper):
    points = 0

    for i in range((len(calories) + 1) - k):
        if i == 0:
            total = sum(calories[:k])
        else:
            total -= calories[i - 1]
            total += calories[i + (k - 1)]

        if total < lower:
            points -= 1
        elif total > upper:
            points += 1

    return points


print(dietPlanPerformance([3,10,17,12,19,6,17,4,15,18], 5, 34, 53))
