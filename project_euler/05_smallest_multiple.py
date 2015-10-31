__author__ = 'William'


def main():
    smallest_multiple = 1
    while True:
        smallest_multiple_found = True
        for i in range(1, 20):
            if smallest_multiple % i:
                smallest_multiple_found = False
                break

        if smallest_multiple_found:
            print(smallest_multiple)
            break
        else:
            smallest_multiple += 1


main()
