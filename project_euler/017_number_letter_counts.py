
def map_number_to_word(number):
    word = ""

    if number < 20:
        word = map_first_part_to_word(number)

    elif 20 <= number < 100:
        number_as_string = str(number)
        second_part = int(number_as_string[0])
        first_part = int(number_as_string[1])
        word += map_second_part_to_word(second_part)
        word += map_first_part_to_word(first_part)

    elif 100 <= number < 1000:
        number_as_string = str(number)
        third_part = int(number_as_string[0])
        second_part = int(number_as_string[1])
        first_part = int(number_as_string[2])
        word += map_third_part_to_word(third_part)

        if second_part > 0 or first_part > 0:
            word += "and"
        if second_part == 1:
            first_part = int("1" + str(first_part))
        else:
            word += map_second_part_to_word(second_part)
        word += map_first_part_to_word(first_part)

    elif number == 1000:
        word = "onethousand"

    return word


def map_first_part_to_word(number):
    word = ""
    if number == 1:
        word = "one"
    elif number == 2:
        word = "two"
    elif number == 3:
        word = "three"
    elif number == 4:
        word = "four"
    elif number == 5:
        word = "five"
    elif number == 6:
        word = "six"
    elif number == 7:
        word = "seven"
    elif number == 8:
        word = "eight"
    elif number == 9:
        word = "nine"
    elif number == 10:
        word = "ten"
    elif number == 11:
        word = "eleven"
    elif number == 12:
        word = "twelve"
    elif number == 13:
        word = "thirteen"
    elif number == 14:
        word = "fourteen"
    elif number == 15:
        word = "fifteen"
    elif number == 16:
        word = "sixteen"
    elif number == 17:
        word = "seventeen"
    elif number == 18:
        word = "eighteen"
    elif number == 19:
        word = "nineteen"
    return word


def map_second_part_to_word(number):
    word = ""
    if number == 2:
        word = "twenty"
    elif number == 3:
        word = "thirty"
    elif number == 4:
        word = "forty"
    elif number == 5:
        word = "fifty"
    elif number == 6:
        word = "sixty"
    elif number == 7:
        word = "seventy"
    elif number == 8:
        word = "eighty"
    elif number == 9:
        word = "ninety"
    return word


def map_third_part_to_word(number):
    word = ""
    if number == 1:
        word = "onehundred"
    elif number == 2:
        word = "twohundred"
    elif number == 3:
        word = "threehundred"
    elif number == 4:
        word = "fourhundred"
    elif number == 5:
        word = "fivehundred"
    elif number == 6:
        word = "sixhundred"
    elif number == 7:
        word = "sevenhundred"
    elif number == 8:
        word = "eighthundred"
    elif number == 9:
        word = "ninehundred"
    return word


def main():
    number_words = ""
    for number in range(1, 1001):
        number_words += map_number_to_word(number)
    print(number_words)
    print(len(number_words))


main()
