'''
Mapping Names to Sequence Elements

Using collections.namedtuple to create a subclass in Python
'''

from collections import namedtuple

Player = namedtuple('Player', ['Name', 'Age', 'Position'])
p = Player('Tom', 23, 'Forward')
print(p) # Player(Name='Tom', Age=23, Position='Forward')
print(p.Name, p.Age, p.Position) # (Tom, 23, Forward)
