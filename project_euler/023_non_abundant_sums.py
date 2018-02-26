"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def _is_number_abundant(number):
    return _sum_of_proper_divisors(number) > number


def _sum_of_proper_divisors(number):
    return sum(n for n in range(1, number) if number % n == 0)


def _print_sum_of_non_abundant_numbers():
    abundant_sums = set()
    abundant_numbers = _get_set_of_abundant_numbers()
    print("Number of abundant numbers: ", len(abundant_numbers))
    print("Generating set of abundant number sums...")
    for a in abundant_numbers:
        for b in abundant_numbers:
            sum_of_nums = a + b
            if sum_of_nums <= 28123:
                abundant_sums.add(sum_of_nums)
            else:
                break

    print("Generating set of all integers up to and including 28123...")
    list_all_integers = set(n for n in range(1, 28123))

    print("Getting diff between these lists to get all the positive integers which cannot"
          "be written as the sum of two abundant numbers...")
    non_abundant_sums = list_all_integers - abundant_sums

    print("sum of all the positive integers which cannot be written as the sum of two abundant numbers...")
    print("Is...")
    print(sum(non_abundant_sums))


def _get_set_of_abundant_numbers():
    print("Getting set of abundant numbers...")
    return set(num for num in range(1, 28123) if _is_number_abundant(num))


_print_sum_of_non_abundant_numbers()
