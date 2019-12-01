from functions import getdata, calcfuel
def main():
	total = 0
	data = getdata("input.txt")
	for entry in data:
		fuel = calcfuel(entry)
		total_for_entry = fuel
		while calcfuel(fuel) > 0:
			fuel = calcfuel(fuel)
			total_for_entry += fuel
		total += total_for_entry
	return total


print(main())