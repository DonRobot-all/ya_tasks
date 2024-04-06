'''
Задача продавец рыбы
'''


def profit(days, day_spoil, cost):
    max_profit = 0
    profit = 0
    step = 0
    for i in range(days - 1):
        if cost[i] > cost[i + 1] or step > day_spoil:
            profit = 0
            step = 0
        elif cost[i] <= cost[i + 1]:
            if step == day_spoil and (cost[i + 1] - cost[i]) + profit > profit - cost[i - day_spoil + 1]:
                profit += (cost[i + 1] - profit) - cost[i - day_spoil + 1]
                max_profit = max(profit, max_profit)
            else:
                profit += cost[i + 1] - cost[i]
                max_profit = max(profit, max_profit)
                step += 1
    return max_profit


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
