inputlow = 152085
inputhigh = 670283

def getpasswords():
	passwords = []
	i = inputlow
	while i <= inputhigh:
		if decrease(i):
			pass
		elif noadjacent(i):
			pass
		else:
			passwords.append(i)
		i += 1
	return passwords

def getnewpasswords():
	passwords = []
	i = inputlow
	while i <= inputhigh:
		if decrease(i):
			pass
		elif not onlytwoadjacent(i):
			pass
		else:
			passwords.append(i)
		i += 1
	return passwords

def decrease(number):
	numarr = list(map(int, str(number)))
	prev = int(str(number)[0])
	for c in numarr:
		if c < prev:
			return True
		prev = c
	return False

def onlytwoadjacent(number):
	numarr = list(map(int, str(number)))
	for c in numarr:
		if numarr.count(c) == 2:
			return True
	return False

def noadjacent(number):
	numarr = list(map(int, str(number)))
	prev = int(str(number)[0])
	adjacent = []
	for c in numarr[1:]:
		if c == prev:
			adjacent.append(c)
		prev = c
	if len(adjacent) > 0:	
		return False
	return True

print(len(getnewpasswords()))