# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

# ========== MY ORIGINAL SOLUTION (RUNS TOO SLOWLY!!) ==============
# def _get_sum_of_proper_divisors(n):
#     sum_of_proper_divisors = 0
#     for num in range(n - 1, 0, -1):
#         if n % num == 0:
#             sum_of_proper_divisors += num
#     return sum_of_proper_divisors
#
#
# def main():
#     amicable_numbers = []
#     max_number = 10000
#     for a in range(1, max_number):
#         d_a = _get_sum_of_proper_divisors(a)
#         for b in range(1, max_number):
#             # print("a == {0}, b == {1}".format(a, b))
#             d_b = _get_sum_of_proper_divisors(b)
#             if d_a == b and d_b == a and a != b:
#                 print("amicable pair: a == {0}, b == {1}".format(a, b))
#                 amicable_numbers.append(a)
#                 amicable_numbers.append(b)
#     print(sum(amicable_numbers))
#
#
# if __name__ == '__main__':
#     main()
#
# ============== BETTER SOLUTION ==============


def _calculate_amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"

    if limit < 1:
        return "Input must be greater than 0!"

    amicables = set()

    for num in range(2, limit + 1):
        if num in amicables:
            continue

        sum_factorial_a = sum([fact for fact in range(1, num) if num % fact == 0])
        sum_factorial_b = sum([fact for fact in range(1, sum_factorial_a) if sum_factorial_a % fact == 0])
        if num == sum_factorial_b and num != sum_factorial_a:
            amicables.add(num)
            amicables.add(sum_factorial_b)

    return sum(amicables)


print(_calculate_amicable_numbers_sum(10000))
