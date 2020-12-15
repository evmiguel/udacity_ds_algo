"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Algorithm
#  Create a phone number dictionary
#  For each call
#    if the sending number is in the dict
#      add the time spent to the dict entry
#    else
#      add the number as an entry to the dict
#
#    if the receiving number is in the dict
#      add the time spent to the dict entry
#    else
#      add the number as an entry to the dict
#
#   return the max time

phone_dict = {}
for call in calls:
    if call[0] in phone_dict:
        phone_dict[call[0]] += int(call[3])
    else:
        phone_dict[call[0]] = int(call[3])

    if call[1] in phone_dict:
        phone_dict[call[1]] += int(call[3])
    else:
        phone_dict[call[1]] = int(call[3])

max_phone_number = max(phone_dict, key = lambda k: phone_dict[k])
max_time = phone_dict[max_phone_number]

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(max_phone_number, str(max_time)))

