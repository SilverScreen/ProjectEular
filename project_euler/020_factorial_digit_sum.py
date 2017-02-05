# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!


def _get_factorial(number):
    factorial = number
    for num in range(number - 1, 0, -1):
        factorial *= num
    return factorial


def main():
    factorial = _get_factorial(100)
    factorial_digit_sum = 0
    for num in str(factorial):
        factorial_digit_sum += int(num)
    print(factorial_digit_sum)


if __name__ == '__main__':
    main()
