from math import ceil


def max_custom(list):
    max_val = list[0]
    for i in list:
        if i > max_val:
            max_val = i
    return max_val


def min_speed(piles, hours):
    left = 1
    right = max_custom(piles)
    while left < right:
        mid = (left + right) // 2
        hours_1 = 0
        for pile in piles:
            hours_1 += ceil(pile / mid)
        if hours_1 <= hours:
            right = mid
        else:
            left = mid + 1
    return left