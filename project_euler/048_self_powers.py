"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def _calculate_sum_of_self_powers(last_digit):
    sum_of_self_powers = 0
    for i in range(last_digit, 0, -1):
        sum_of_power = i ** i
        sum_of_self_powers += sum_of_power
    return sum_of_self_powers


def _get_last_ten_digits(number):
    number_as_string = str(number)
    if len(number_as_string) <= 10:
        return number
    else:
        return int(number_as_string[-10:])


def main():
    sum_of_self_powers = _calculate_sum_of_self_powers(last_digit=1000)
    print("Last ten digits =", _get_last_ten_digits(sum_of_self_powers))


main()
