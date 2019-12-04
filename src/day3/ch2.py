from functions import takestep, getdata
from ch1 import getintersections, getclosestintersection

def main():
	lines = getdata()
	intersections = getintersections(lines[0], lines[1])
	print(leaststeps(lines, intersections))

def leaststeps(paths, intersections):
	steparr = []
	for intersection in intersections:
		steparr.append(steps2intersect(paths[0], intersection) +  steps2intersect(paths[1], intersection))
	steparr.sort()
	return steparr[0]
		
def steps2intersect(path, intersect):
	pos = (0, 0)
	stepcounter = 0
	for instruction in path:
		i = 1
		while i <= int(instruction[1:]):
			pos = takestep(pos, instruction[0])
			stepcounter += 1
			if pos == intersect:
				return stepcounter
			i += 1

main()