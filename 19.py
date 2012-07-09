# You are given the following information, but you may prefer to do some
# research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

s = 2 # Jan 1, 1901 is a Tuesday
c = 0

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year in range(1901, 2001):
    for month in range(12):
        if (s) % 7 == 0:
            c += 1
        s += days_in_months[month]
        if month == 1 and year % 4 == 0:
            s += 1

print c