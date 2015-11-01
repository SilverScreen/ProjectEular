__author__ = 'William'


def sum_of_the_squares(n):
    total = 0
    for number in range(1, n + 1):
        total += number * number
    return total


def square_of_the_sum(n):
    sum_of_numbers = 0
    for number in range(1, n + 1):
        sum_of_numbers += number
    return sum_of_numbers * sum_of_numbers


def main():
    n = 100
    print(square_of_the_sum(n) - sum_of_the_squares(n))


main()