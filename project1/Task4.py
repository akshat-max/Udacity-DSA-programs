"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def real_numbers_set(texts, calls):
    real_num = set()
    for info in texts:  # add any texted number
        real_num.add(info[0])
        real_num.add(info[1])
    for info in calls:
        real_num.add(info[1])  # add called number
    return real_num


def telemarketers_set(real_num, calls):
    scammers = set()
    for info in calls:
        number = info[0]
        if number not in real_num:
            scammers.add(number)
    return scammers


def answer():
    real_num = real_numbers_set(texts, calls)
    scammers = telemarketers_set(real_num, calls)
    print("These numbers could be telemarketers: ")
    for number in sorted(scammers):
        print(number)
    pass


answer()
