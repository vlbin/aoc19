def main():
	lines = getdata()
	intersections = getintersections(lines[0], lines[1])
	#closest = getclosestintersection(intersections)



def getintersections(path1, path2):
	line1 = getlinecords(path1)
	line2 = getlinecords(path2)
	return list(set(line1).intersection(line2))


def getclosestintersection(intersections):
	closest = abs(intersections[0][0]) + abs(intersections[0][1])
	for intersection in intersections:
		in1 = abs(intersection[0])
		in2 = abs(intersection[1])
		if in1 + in2 < closest:
			closest = in1 + in2
	return closest
	

def getlinecords(line):
	coordlist = []
	start = (0, 0)
	for instruction in line:
		coordlist.extend(readinstruction(start, instruction[0], int(instruction[1:])))
		start = coordlist[-1]
	return coordlist

def readinstruction(pos, direction, steps):
	list = []
	
	i = 1
	while i <= steps:
		new_pos = ()
		if direction == 'R':
			new_pos = (pos[0] + i, pos[1])
		elif direction == 'U':
			new_pos = (pos[0], pos[1] + i)
		elif direction == 'L':
			new_pos = (pos[0] - i, pos[1])
		else:
			new_pos = (pos[0], pos[1] - i)
		if new_pos not in list:
			list.append(new_pos)

		i = i + 1
	return list

def getdata():
	file = open('src/day3/input2.txt', 'r')
	lines = file.read().split("\n")
	line1 = lines[0]
	line2 = lines[1]
	returnlines = []
	returnlines.append(line1.split(","))
	returnlines.append(line2.split(","))
	
	return returnlines

main()