'''
Задача минимальный прямоугольник
'''


cells = int(input())

min_x = 10 ** 9
max_x = 0
min_y = 10 ** 9
max_y = 0

for i in range(cells):
    x, y = map(int, input().split())

    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print(min_x, min_y, max_x, max_y)
