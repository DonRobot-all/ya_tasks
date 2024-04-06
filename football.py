# g1, g2 = map(int, input().split(':'))
# gn_1, gn_2 = map(int, input().split(':'))
# guest = int(input())


def football(g1, g2, gn_1, gn_2, guest):
    if g1 + gn_1 > g2 + gn_2:
        return 0
    if g1 + gn_1 == g2 + gn_2:
        return 1
    if guest == 2:
        g1, gn_1, g2, gn_2 = gn_1, g1, gn_2, g2
    if g2 > gn_2:
        return g2 - g1 + g2 - gn_1
    if gn_2 > g2:
        return g2 - g1 + gn_2 - gn_1


if __name__ == "__main__":
    # print(football(g1, g2, gn_1, gn_2, guest))
    assert football(0, 0, 0, 0, 1) == 1, football(0, 0, 0, 0, 1)
    assert football(0, 2, 0, 3, 1) == 5, football(0, 2, 0, 3, 1)
    assert football(0, 2, 0, 3, 2) == 6, football(0, 2, 0, 3, 2)
    assert football(1, 2, 1, 3, 2) == 4, football(0, 2, 0, 3, 2)

3 2
2 3
