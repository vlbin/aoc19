def intcode(data, val1, val2):
	i = 0
	data[1] = val1
	data[2] = val2
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
	return data[0]	


def main():
	for i in range(0,100):
		for k in range(0,100):		
			if intcode(getdata(), i, k) == 19690720:
				print(100 * i + k)
				break


def getdata():
	file = open("src/day2/input.txt") #full path
	return [int(i) for i in file.read().split(",")]

main()