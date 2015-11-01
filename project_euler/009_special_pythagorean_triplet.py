__author__ = 'William'

import math


def main():
    total = 0
    b = 1
    while total != 1000:
        for a in range(1, b):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer():
                print("{a}^2 + {b}^2 = {c}^2".format(a=a, b=b, c=c))
                total = a + b + c
                print("{a} + {b} + {c} = {total}".format(a=a, b=b, c=c, total=total))
                print("{a} * {b} * {c} = {product}\n".format(a=a, b=b, c=c, product=(a * b * c)))
        b += 1

main()
