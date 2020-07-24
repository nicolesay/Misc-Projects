var = input('> ')
var = int(var)

flag = False

while flag == False:
	if var == str(var):
		print('Pass')
		flag = True
	else:
		if var != str:
			print('Try again')