from functools import lru_cache


@lru_cache(maxsize=None)
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


print(FibbRecusion(200))

# Input:  200
# Output: 280571172992510140037611932413038677189525
