'''
Unpacking Elements from Iterables of Arbitrary Length

Problem
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception.
'''

# Use * to pack multiple elements
record = ['John', 'John@example.com', '04512313', '32324', '2234']
# pack all the numbers together
name, email, *numbers = record 
print(name) #John
print(email) #John@example.com
print(numbers) #('04512313', '32324', 2234)

# Pack all middle elements
Array = [1,2,3,4,5,6]
_, *middle, _ = Array
print(middle)

          
