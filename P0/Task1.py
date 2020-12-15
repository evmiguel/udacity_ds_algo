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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Algorithm:
#   For each in (sending texts, receiving texts, sending calls, receiving calls)
#      add to set
#   return set length

phone_number_set = set()

# Add the numbers from sending and receiving text
for line in texts:
    phone_number_set.add(line[0])
    phone_number_set.add(line[1])

# Add the numbers from sending and receiving calls
for line in calls:
    phone_number_set.add(line[0])
    phone_number_set.add(line[1])

print("There are {0} different telephone numbers in the records.".format(len(phone_number_set)))
