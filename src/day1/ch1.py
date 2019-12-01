import math
from functions import getdata, calcfuel
def main():
	data = getdata("input.txt")
	total = 0
	for entry in data:
		total += calcfuel(entry)
	return total


print(main())