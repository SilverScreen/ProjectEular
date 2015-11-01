__author__ = 'William'


def calculate_number_of_lattice_paths(n):
    return (n + 1) * n


def main():
    print(calculate_number_of_lattice_paths(20))


main()
