__author__ = 'William'


def generate_collatz_sequence(n):
    collatz_sequence = [n]

    while n > 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        collatz_sequence.append(int(n))
    return collatz_sequence


def main():
    longest_chain_length = 0
    number_with_longest_chain_length = 0

    for number in range(1, 1000000):
        chain_length = len(generate_collatz_sequence(number))
        if chain_length > longest_chain_length:
            longest_chain_length = chain_length
            number_with_longest_chain_length = number
        print("{number}, {longest_chain_length}, {number_with_longest_chain_length}".format(number=number,
                                                                                            longest_chain_length=longest_chain_length,
                                                                                            number_with_longest_chain_length=number_with_longest_chain_length))

    print("Number with longest chain ==> {}".format(str(number_with_longest_chain_length)))


main()
