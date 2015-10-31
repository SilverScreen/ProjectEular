__author__ = 'William'


def main():
    largest_palindrome = 0

    for i in range(1000, -1, -1):
        for j in range(1000, -1, -1):
            product = i * j
            if is_palindrome_number(product) and product > largest_palindrome:
                largest_palindrome = product
    print(largest_palindrome)


def is_palindrome_number(num):
    num_to_string = str(num)

    if num_to_string == num_to_string[::-1]:
        return True
    return False


main()