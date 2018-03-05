"""
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def _print_fibonacci_sequence(num_digits):
    fn_1 = 0
    fn_2 = 1
    index = 1
    while True:
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
        if len(str(fn)) == num_digits:
            print("term =", fn)
            print("index =", index)
            break
        index += 1


_print_fibonacci_sequence(num_digits=1000)
