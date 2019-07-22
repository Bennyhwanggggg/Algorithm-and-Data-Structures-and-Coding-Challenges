"""
Given an on screen keyboard
A B C D E F G H I J
K L M N O P Q R S
T U V W X Y Z

and buttons UDLRE for up down left right enter

and we need to spell something out like BAT, give the commands: so RELEDDE
"""
import collections

def pressButtonToPrintAWord(word):
	if not word:
		return ''
	keyboard = ["ABCDEFGHIJ",
				"KLMNOPQRS",
				"TUVWXYZ"];

	mapping = dict()
	for row in range(len(keyboard)):
		for col in range(len(keyboard[row])):
			mapping[keyboard[row][col]] = (row, col)

	result = []
	curr = (0, 0)
	for w in word:
		x, y = mapping[w]
		distX = x - curr[0]
		distY = y - curr[1]
		if distX:
			result.append(('U' if distX < 0 else 'D') * abs(distX))
		if distY:
			result.append(('L' if distY < 0 else 'R') * abs(distY))
		result.append('E')
		curr = (x, y)
	return ''.join(result)


if __name__ == '__main__':
	print(pressButtonToPrintAWord('BAT') == 'RELEDDE') # True
	print(pressButtonToPrintAWord('AAZR') == 'EEDDRRRRRREURE') # True
	print(pressButtonToPrintAWord('AZBC') == 'EDDRRRRRREUULLLLLERE') # True
