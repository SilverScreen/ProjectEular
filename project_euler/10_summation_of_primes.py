__author__ = 'William'


def sum_of_primes(below):
    total = 0
    for number in range(2, below):
        if is_prime(number):
            print(number)
            total += number
    return total


def is_prime(number):
    for index in range(2, number):
        if number % index == 0:
            return False
    return True


def main():
    print(sum_of_primes(2000000))


main()