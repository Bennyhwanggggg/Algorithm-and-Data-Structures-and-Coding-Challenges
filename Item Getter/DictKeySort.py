'''
Sort Dictionary by Key

Problem
You have a list of dictionaries and you would like to sort the entries according to one
or more of the dictionary values.
'''

# Use this module
from operator import itemgetter

rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]

rowbyfname = sorted(rows, key=itemgetter('fname'))
print(rowbyfname)
rowbyuid = sorted(rows, key=itemgetter('uid'))
print(rowbyuid)
