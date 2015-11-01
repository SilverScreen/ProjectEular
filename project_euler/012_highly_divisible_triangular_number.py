__author__ = 'William'

import itertools

flatten_iter = itertools.chain.from_iterable
highest_num_factors = 0


def get_triangular_number(divisors):
    index = 2
    triangular_number = 0
    while True:
        triangular_number = sum(range(index))
        if len(get_factors(triangular_number)) > divisors:
            break
        index += 1
    return triangular_number


def get_factors(number):
    global highest_num_factors
    factors = set(flatten_iter((i, number // i) for i in range(1, int(number ** 0.5) + 1) if number % i == 0))
    if len(factors) > highest_num_factors:
        highest_num_factors = len(factors)
    print("[{0}][{1}]{2}".format(highest_num_factors, len(factors), factors))
    return factors


def main():
    print("Result={}".format(get_triangular_number(500)))


main()
