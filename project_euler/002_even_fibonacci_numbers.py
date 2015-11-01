__author__ = 'William'


def main():
    previous_two_number = 0
    previous_one_number = 1
    sum_of_even_value_terms = 0

    while True:
        current_number = previous_one_number + previous_two_number
        if current_number >= 4000000:
            break
        if current_number % 2 == 0:
            sum_of_even_value_terms += current_number
        previous_two_number = previous_one_number
        previous_one_number = current_number

    print(sum_of_even_value_terms)

main()