def FibbRecusion(num):
    if num <= 0:
        return 0

    elif num == 1 or num == 2:
        return 1

    else:
        return FibbRecusion(num-1) + FibbRecusion(num-2)


def Fibb(num):
    if num <= 0:
        return 0

    elif num == 1 or num == 2:
        return 1

    fibbs = [0, 1]

    for i in range(num):
        fibbs[0], fibbs[1] = fibbs[1], fibbs[0]
        fibbs[1] += fibbs[0]

    return fibbs[0]


print(Fibb(6))

# Input:  6
# Output: 8
