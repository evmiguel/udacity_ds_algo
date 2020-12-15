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

# Algorithm
#  Get all unique the phone numbers that don't receive incoming calls
#  Define a set of telemarketers
#  For each number that doesn't receive calls
#   if that number is not in sending or receiving text columns
#       add that number to the set

def get_phone_numbers(data, column):
    numbers = set()
    for line in data:
        numbers.add(line[column])
    return numbers

def get_possible_telemarketers_from_calls():
    sending = get_phone_numbers(calls, 0)
    receiving = get_phone_numbers(calls, 1)
    possible_telemarketers = set()

    for number in sending:
        if number not in receiving:
            possible_telemarketers.add(number)
    return possible_telemarketers

possible_telemarketers = get_possible_telemarketers_from_calls()
telemarketers = set()
sending_text_numbers = get_phone_numbers(texts, 0)
receiving_text_numbers = get_phone_numbers(texts, 1)
for possible in possible_telemarketers:
    if possible not in sending_text_numbers and possible not in receiving_text_numbers:
        telemarketers.add(possible)

print("These numbers could be telemarketers: ")
for telemarketer in sorted(telemarketers):
    print(telemarketer)