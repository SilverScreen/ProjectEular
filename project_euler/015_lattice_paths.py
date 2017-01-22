GRID_SIZE = 20


def calculate_number_of_lattice_paths(grid_size):
    paths = 1
    for i in range(grid_size):
        paths *= (2 * grid_size) - i
        paths /= i + 1
    return paths


def main():
    number_of_lattice_paths = calculate_number_of_lattice_paths(GRID_SIZE)
    print(number_of_lattice_paths)


main()
