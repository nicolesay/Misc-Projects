import os
def double_digit(d):
    q, r = divmod(2 * d, 10)
    return q + r

cc = input('Enter a Credit Card #: ')

single_digits = 0
double_digits = 0

if len(str(cc)) < 13 or not type(int):
    print('Less than 13 digits or not an integer , please try again.')
    os._exit(1)
elif int(cc[0]) == 4 and len(cc) == 13:
    print('This is a Visa Card')
elif int(cc[0]) == 4 and len(cc) == 16:
    print('This is a Visa Card')
elif int(cc[0]) == 5 and len(cc) == 16:
    print('This is a Mastercard')
elif int(cc[0]) == 2 and len(cc) == 16:
    print('This is a Mastercard')
elif int(cc[0]) == 3 and len(cc) == 15:
    print('This is an American Express Card')
elif int(cc[0]) == 6 and len(cc) == 16:
    print('This is a Discover Card')
else:
    print('This card is not a Visa, Mastercard, Discover or American Express, lease try again.')
    sys.exit()

for s in list(cc)[-3::-2]:
    single_digits += int(s)

for d in list(cc)[-2::-2]:
    d = int(d)
    double_digits += double_digit(d)

if (((single_digits + double_digits) * 9) %10) == int(cc[-1]):
    print('Card is Valid!')
else:
    print('Card is Invalid!')