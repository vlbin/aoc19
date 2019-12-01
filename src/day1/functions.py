import math
def getdata(filename):
	file = open(filename, "r")
	return [int(i) for i in file.read().split("\n")]

def calcfuel(module):
	return math.floor(module / 3) - 2