"""
The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""


ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
WORD_FILE = "p042_words.txt"


def _convert_to_word_value(word):
    word_value = 0
    for c in word:
        word_value += ALPHABET.index(c) + 1
    return word_value


def _is_triangle_number(number):
    for n in range(0, 9999):
        tn = (0.5 * n) * (n + 1)
        if tn == number:
            return True
    return False


def main():
    with open(WORD_FILE, "r") as file_stream:
        for content in file_stream:
            words = content.split(",")
            triangle_word_count = 0
            for word in words:
                word = word.replace("\"", "")
                word_value = _convert_to_word_value(word)
                if _is_triangle_number(word_value):
                    print("%s is a triangle word" % word)
                    triangle_word_count += 1
            print("\nFound %d triangle words" % triangle_word_count)


main()
