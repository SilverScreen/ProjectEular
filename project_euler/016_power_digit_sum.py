
def calc_sum_of_digits(power):
    result = 2 ** power
    return sum(int(digit) for digit in str(result))


def main():
    print(calc_sum_of_digits(1000))


main()
