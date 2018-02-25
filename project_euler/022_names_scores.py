# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

import string


def _read_names_from_file():
    names = []
    names_file = "p022_names.txt"
    with open(names_file, "r") as file_stream:
        for line in file_stream:
            names_in_line = line.split(",")
            for name in names_in_line:
                names.append(name.strip('\"'))
    return names


def _calculate_total_name_scores(names):
    total_name_scores = 0
    position_in_list = 1
    for name in names:
        alphabetical_value = _calculate_alphabetical_value_for_name(name)
        total_name_scores += position_in_list * alphabetical_value
        position_in_list += 1
    return total_name_scores


def _calculate_alphabetical_value_for_name(name):
    alphabetical_value = 0
    for char in name:
        alphabetical_value += (string.ascii_uppercase.index(char) + 1)
    return alphabetical_value


names_from_file = _read_names_from_file()
names_from_file.sort()
print(_calculate_total_name_scores(names_from_file))
