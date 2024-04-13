'''
Задача продавец рыбы
'''


def profit(days, day_spoil, cost):
    maxint = 0
    for i in range(days):
        for j in range(day_spoil + 1):
            if i + j < days:
                print(i , j)
                maxint = max(maxint, cost[i + j] - cost[i])
    return maxint


days, day_spoil = map(int, input().split())
cost = list(map(int, input().split()))
print(profit(days, day_spoil, cost))

days, day_spoil = 5, 3
cost = [4, 6, 8, 3, 10]
assert profit(days, day_spoil, cost) == 7, profit(days, day_spoil, cost)

days, day_spoil = 10, 2
cost = [4, 6, 8, 3, 10, 1, 0, 7, 16, 27]
assert profit(days, day_spoil, cost) == 20, profit(days, day_spoil, cost)

days, day_spoil = 10, 2
cost = [1, 2, 10, 9, 27, 26, 7, 6, 5, 4]
assert profit(days, day_spoil, cost) == 18, profit(days, day_spoil, cost)

days, day_spoil = 10, 2
cost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert profit(days, day_spoil, cost) == 0, profit(days, day_spoil, cost)

days, day_spoil = 10, 2
cost = [0, 6, 0, 0, 10, 0, 0, 0, 0, 0]
assert profit(days, day_spoil, cost) == 10, profit(days, day_spoil, cost)

days, day_spoil = 0, 2
cost = []
assert profit(days, day_spoil, cost) == 0, profit(days, day_spoil, cost)
