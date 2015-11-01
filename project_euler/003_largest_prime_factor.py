__author__ = 'William'


def main():
    result = largest_prime_factor(600851475143)
    print(result)


def largest_prime_factor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
    return num

main()