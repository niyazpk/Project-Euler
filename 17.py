# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when
# writing out numbers is in compliance with British usage.

import re


def digit_to_word(n, units=0, tens=False, tenth=False):
    m = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

    m_tenth = {
        0: '',
        1: 'ten',
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }

    m_tens = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }

    m = m_tenth if tenth else m
    m = m_tens if tens else m

    if tens:
        n = n * 10 + units
    return m[n]


def in_words(n):
    _1000 = n / 1000
    _100 = (n % 1000) / 100
    _10 = (n % 100) / 10
    _1 = n % 10

    w = ''

    if _1000:
        w += ' ' + digit_to_word(_1000) + ' thousand'
    if _100:
        w += ' ' + digit_to_word(_100) + ' hundred'
    if (_1000 or _100) and (_10 or _1):
        w += ' and'
    if _10:
        w += ' ' + digit_to_word(_10, _1, tenth=True, tens=(_10 == 1))
    if _1 and _10 != 1:
        w += ' ' + digit_to_word(_1)

    return w


s = 0
for i in range(1, 1001):
    s += len(re.sub('[^a-z]', '', in_words(i)))

print s
