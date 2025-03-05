#Рівень 3
import unittest


def func(x):
    n = len(x)
    if n < 3:
        return 0

    s = 0

    for i in range(1, n - 1):
        if x[i] > x[i - 1] and x[i] > x[i + 1]:
            left = i - 1
            while left >= 0 and x[left] < x[left + 1]:
                left -= 1
            right = i + 1
            while right < n and x[right] < x[right - 1]:
                right += 1
            s = max(s, right - left - 1)
    return s


if __name__ == '__main__':
    print(func([15, 7, 22, 9, 36, 2, 42, 18]))
