from datetime import datetime

SUNDAY = 6
sunday_count = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        date = datetime(year=year, month=month, day=1)
        if date.weekday() == SUNDAY:
            sunday_count += 1

print("Number of Sundays: ", sunday_count)
