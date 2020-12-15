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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Algorithm
#  define get_area_code function
#
#  all_calls = []
#  for each call:
#    if get_area_code(sending_call) is from bangalore
#      append call to all_calls
#
#  Part A:
#    area_codes = set()
#    for call in all_calls:
#      area_codes.add(get_area_code(receiving_number))
#    for each area code in sorted(set):
#      print area code
#
#  Part B:
#    fixed line received = 0
#    for call in all_calls:
#      if get_area_code(receiving_number) is fixed line
#        increment fixed line received

def get_area_code(phone_number):
  if "(" in phone_number and ")" in phone_number:
    return phone_number[1:phone_number.find(')')]
  elif ' ' in phone_number:
    return phone_number[0:4]
  else:
    return phone_number[0:3]

all_calls = []
for line in calls:
  if get_area_code(line[0]) == '080':
    all_calls.append(line)

# Part A and B consolidated
print('Area codes called by people in Banglore:')
area_codes = set()
fixed_line_received = 0
for call in all_calls:
  # Part A
  area_code = get_area_code(call[1])
  area_codes.add(area_code)

  # Part B
  if area_code == '080':
    fixed_line_received += 1

for area_code in sorted(area_codes):
  print(area_code)

print('\n---------------------\n')

percentage_to_bangalore = round(fixed_line_received / len(all_calls) * 100, 2)
print("{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage_to_bangalore))


