def getdata(filename):
	file = open("src/day2/%s.txt" % (filename)) #full path
	return [int(i) for i in file.read().split(",")]

data = getdata("input")

i = 0

data[1] = 12
data[2] = 2
while i + 3 < len(data):
	opcode = data[i]
	if opcode == 1 or 2:
		index1 = data[i + 1]
		index2 = data[i + 2]
		insertindex = data[i + 3]
		if opcode == 1:
			data[insertindex] = data[index1] + data[index2]
		else:
			data[insertindex] = data[index1] * data[index2]
	elif opcode == 99:
		break
	i += 4


print(data)