# p, v = map(int, input().split())
# q, m = map(int, input().split())


def trees(p, v, q, m):
    if v <= 0 or m <= 0:
        return 0
    if p == q:
        # return abs(m - v) + v
        return max(m, v) * 2 + 1
    (p, v), (q, m) = sorted([(p, v), (q, m)])
    if p + v >= q - m:
        if p - v >= q - m and p + v <= q + m:
            return m * 2 + 1
        elif p + v >= q + m and p - v >= q - m:
            return v * 2 + 1
        return q + m + abs(p - v) + 1
    return (v * 2 + 1) + (m * 2 + 1)


if __name__ == "__main__":
    # print(trees(p, v, q, m))
    print(trees(12, 5, 0, 7))  # 25
    print(trees(12, 2, 0, 2))  # 10
    print(trees(12, 2, 12, 3))  # 7
    print(trees(-5, 2, 12, 3))  # 12
    print(trees(5, 5, 6, 5))  # 12
    print(trees(-5, 5, -5, 5))  # 11
    print(trees(-10, 5, -5, 5))  # 16
    print(trees(0, 0, 0, 0))  # 1
    print(trees(10, 2, -10, 2))  # 10
    print(trees(-10, 2, 10, 2))  # 10
    print(trees(5, 2, 5, 2))  # 5
    print(trees(-5, 2, -5, 2))  # 5
    print(trees(5, 0, 15, 2))  # 6
    print(trees(5, 1, 15, 2))  # 8
    print(trees(1, 2, -1, 2))  # 7
    print(trees(3, 0, 9, 0))   # 2
    print(trees(-3, 1, -5, 1))   # 5
    print(trees(0, 5, 10, 30))   # 61
    # assert trees(0, 5, 10, 30) == 61, trees(0, 5, 10, 30)
