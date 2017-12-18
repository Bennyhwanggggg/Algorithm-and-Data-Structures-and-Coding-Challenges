'''
Slicing

Problem
Your program has become an unreadable mess of hardcoded slice indices and you want
to clean it up.
'''

r = list('1234613221564613128567893464612313231')
record = [int(n) for n in r]
v1 = slice(2,10) 
v2 = slice(12, 20)

v3 = sum(record[v1])*sum(record[v2])
print(v3) # 660

print(v1.start) # 2
print(v1.stop) # 10
print(v1.step) #None

v4 = slice(4,11,2)
print(v4.start) # 4
print(v4.stop) # 11
print(v4.step) # 2
