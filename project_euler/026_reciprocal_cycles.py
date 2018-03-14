"""
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
from decimal import *
import re

longest_recurring_cycle = ""
d_longest_recurring = 0


def _find_longest_recurring_cycle(limit):
    getcontext().prec = 10000
    for d in range(2, limit):
        unit_fraction = Decimal(1) / Decimal(d)
        decimal_part = str(unit_fraction).split(".")[1]
        _find_recurring_cycles_in_decimal_part(d, decimal_part)


def _find_recurring_cycles_in_decimal_part(d, decimal_part):
    global longest_recurring_cycle
    global d_longest_recurring

    pattern = re.compile(r'(.+?)\1+')
    recurring_cycles = re.findall(pattern, decimal_part)
    for recurring_cycle in recurring_cycles:
        recurring_cycle_length = len(recurring_cycle)
        if len(longest_recurring_cycle) < recurring_cycle_length < 1000:
            longest_recurring_cycle = recurring_cycle
            d_longest_recurring = d


_find_longest_recurring_cycle(limit=1000)
print(d_longest_recurring)
