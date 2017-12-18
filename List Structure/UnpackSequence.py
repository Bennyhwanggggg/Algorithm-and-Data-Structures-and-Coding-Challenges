'''
Unpacking a Sequence into Separate Variables

Problem:
You have an N-element tuple or sequence that you would like to unpack into a collection
of N variables.
'''

# Any sequence can be unpacked like this:
data = ['data1', 23, 11.2, (2017, 12, 13)]
name, number, floatN, date = data
print(name) #data1
print(number) #23
print(floatN) #11.2
print(date) #(2017, 12, 13)

# Restriction is that the number of elements must match in the assignment.

# Unpack also work with any iterables such as strings, files, iterators and generators
s = "qwert"
a, b, c, d, e = s
print(a,b,c,d,e) #('q', 'w', 'e', 'r', 't')


