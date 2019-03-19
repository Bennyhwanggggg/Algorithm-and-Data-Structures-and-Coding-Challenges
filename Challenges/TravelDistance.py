import math
def main():
	a = 'LOC:CHI:41.836944:-87.684722'
	b = 'LOC:NYC:40.7127:-74.0059'
	c = 'TRIP:COFEE1C:CHI:NYC'

	locations = dict()

	a = a.split(':')
	if a[0] == 'LOC':
		locations[a[1]] = {'lat': math.radians(float(a[2])), 'long': math.radians(float(a[3]))}

	b = b.split(':')
	if b[0] == 'LOC':
		locations[b[1]] = {'lat': math.radians(float(b[2])), 'long': math.radians(float(b[3]))}

	print(locations)
	c = c.split(':')
	if c[0] == 'TRIP':
		account = c[1]
		dep = c[2]
		arr = c[3]
		
		absdiff = abs(locations[arr]['long'] - locations[dep]['long'] )
		print(absdiff)
		angle = math.acos(math.sin(locations[arr]['lat'])*math.sin(locations[dep]['lat']) + 
											math.cos(locations[arr]['lat'])*math.cos(locations[dep]['lat'])*math.cos(absdiff))

		print(angle)
		dist = 3963*angle
		print(dist)



if __name__ == '__main__':
	main()