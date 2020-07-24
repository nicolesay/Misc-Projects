from math import floor


#def main():
#	while True:
#		dollars_owed = get_float("Change owed: ")
#		cents_owed = floor(dollars_owed * 100)
#
#		if cents_owed > 0:
#			break
#
quarters = 565 // 25
dimes = (565 % 25) // 10
nickels = ((565 % 25) % 10) // 5
pennies = ((565 % 25) % 10) % 5
#
#	print(f"{quarters + dimes + nickels + pennies}")
#
#
#if __name__ == "__main__":
#	main()
	
print(floor(float(5.65 * 100)))
print(quarters)
print(dimes)
print(nickels)
print(pennies)
