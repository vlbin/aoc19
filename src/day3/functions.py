def getdata():
	file = open('src/day3/input.txt', 'r')
	lines = file.read().split("\n")
	line1 = lines[0]
	line2 = lines[1]
	returnlines = []
	returnlines.append(line1.split(","))
	returnlines.append(line2.split(","))
	
	return returnlines

def takestep(pos, direction):
	newpos = ()
	if direction == 'R':
		newpos = (pos[0] + 1, pos[1])
	elif direction == 'U':
		newpos = (pos[0], pos[1] + 1)
	elif direction == 'L':
		newpos = (pos[0] - 1, pos[1])
	else:
		newpos = (pos[0], pos[1] - 1)
	return newpos

		