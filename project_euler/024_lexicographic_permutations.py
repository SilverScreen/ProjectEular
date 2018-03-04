"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from itertools import permutations


def _get_all_permutations(input_numbers):
    all_permutations_for_input_numbers = permutations(input_numbers, (len(input_numbers)))
    return [''.join(perm) for perm in all_permutations_for_input_numbers]


def _get_nth_number(input_list, index):
    return input_list[index - 1]


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lexicographic_permutations = _get_all_permutations(input_numbers=numbers)
nth_permutation = _get_nth_number(input_list=lexicographic_permutations, index=1000000)
print(nth_permutation)
