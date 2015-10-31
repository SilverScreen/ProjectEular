__author__ = 'William'


def list_prime_numbers(n):
    current_number = 2
    prime_number_counter = 0

    while True:
        if is_prime(current_number):
            print("Prime number: " + str(current_number) + ", counter: " + str(prime_number_counter))
            prime_number_counter += 1
        if prime_number_counter == n:
            break
        else:
            current_number += 1
    return current_number


def is_prime(number):
    for index in range(2, number):
        if number % index == 0:
            return False
    return True


def main():
    print(list_prime_numbers(10001))


main()