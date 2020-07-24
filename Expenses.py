import sqlite3
import time
current_user = ''
expense_category = ''
income_category = ''

### Initialize Main SQLite Connection ###
sqliteConnection = sqlite3.connect('Expenses.db')
cursor = sqliteConnection.cursor()

### List That is Printed out for the User Navigation ###
navigation = ['1 - Enter a Transaction', '2 - Display Transactions', '3 - Modify a Transaction', '4 - Delete a Transaction', '5 - Change User', '6 - Quit']
expense_nav = ['1 - Debts', '2 - Entertainment', '3 - Food','4 - Healthcare', '5 - Home Improvement', '6 - Rent or Mortgage', '7 - Saving and Investing', '8 - Transportation', '9 - Utilities']
income_nav = ['1 - Salary', '2 - Other Income', '3 - Refunds', '4 - Balance Adjustment']


### Function to Select Expense Category
def ExpenseSelection():
	global expense_category
	ExpenseFlag = False
	while ExpenseFlag == False:
		print('Please Choose From the Following Expense Categories:\n')
		for i in expense_nav:
			print(i)
		expense_category = ''
		expense_selection = input('> ')
		if expense_selection == str(1):
			ExpenseFlag = True
			expense_category += 'Debts'
			return(expense_category)
		elif expense_selection == str(2):
			ExpenseFlag = True
			expense_category += 'Entertainment'
			return(expense_category)
		elif expense_selection == str(3):
			ExpenseFlag = True
			expense_category += 'Food'
			return(expense_category)
		elif expense_selection == str(4):
			ExpenseFlag = True
			expense_category += 'Healthcare'
			return(expense_category)
		elif expense_selection == str(5):
			ExpenseFlag = True
			expense_category += 'Home Improvement'
			return(expense_category)
		elif expense_selection == str(6):
			ExpenseFlag = True
			expense_category += 'Rent or Mortgage'
			return(expense_category)
		elif expense_selection == str(7):
			ExpenseFlag = True
			expense_category += 'Saving & Investing'
			return(expense_category)
		elif expense_selection == str(8):
			ExpenseFlag = True
			expense_category += 'Transportation'
			return(expense_category)
		elif expense_selection == str(9):
			ExpenseFlag = True
			expense_category += 'Utilities'
			return(expense_category)
		elif expense_selection != range(1,9):
			print()
			print('Please Make a Valid Selection!')
			cont = input('Press any Key to Continue.')

### Function to Select Income Category
def IncomeSelection():
	global income_category
	IncomeFlag = False
	while IncomeFlag == False:
		print('Please Choose From the Following Income Categories:\n')
		for i in income_nav:
			print(i)
		income_category = ''
		income_selection = input('> ')
		if income_selection == str(1):
			IncomeFlag = True
			income_category += 'Salary'
			return income_category
		elif income_selection == str(2):
			IncomeFlag = True
			income_category += 'Other Income'
			return income_category
		elif income_selection == str(3):
			IncomeFlag = True
			income_category += 'Refunds'
			return income_category
		elif income_selection == str(4):
			IncomeFlag = True
			income_category += 'Balance Adjustment'
			return income_category
			print(income_category)
		elif income_selection != range(1,4):
			print()
			print('Please Make a Valid Selection!')
			cont = input('Press any Key to Continue.')


### Function that Returns the Current User ###
def CurrentUser():
    global current_user
    sqliteConnection = sqlite3.connect('Expenses.db')
    cursor = sqliteConnection.cursor()
    user_select = 'SELECT * FROM Users'
    cursor.execute(user_select)
    users = cursor.fetchall()
    users_list = []

    for i in users:
        users_list.append(i)
    print('Current User List is: ')
    print()
    for i in users_list:
        print(str(i[0]) + ' - ' + str(i[1]))

    user_selection = input('Please Select Your User ID\n> ')

    for i in users_list:
        if user_selection == str(i[0]):
            current_user += str(i[1])
            # print('Current User is: ' +  str(current_user))
    return current_user




### Function to Insert Date in to the Database ###
def InsertToTable(Date, Merchant, Description, Amount, Category, User):
	try:
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		sqlite_insert_with_param = """INSERT INTO Expenses
											(Date, Merchant, Description, Amount, Category, User)
											VALUES (?, ?, ?, ?, ?, ?);"""
		data_tuple = (Date, Merchant, Description, Amount, Category, User)
		cursor.execute(sqlite_insert_with_param, data_tuple)
		sqliteConnection.commit()
		print()
		print('Data Successfully Inserted in to Table.')
		print()
		# cursor.close()
	except sqlite3.Error as error:
			print('Failed to Insert Data in to Table.', error)
			print()
	finally:
			if (sqliteConnection):
				sqliteConnection.close()
				print()
				escape = input('Press any key to continue.')

### Function to Select Transactions Between a Start and End Date ###
def SelectTransactions(date1, date2, user):
	try:
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		sql_select_query = """SELECT * FROM Expenses WHERE Date BETWEEN ? and ? and User = ? ORDER BY Date DESC"""
		cursor.execute(sql_select_query, (date1, date2, user))
		records = cursor.fetchall()
		print()
		print('|--------|-----------------|---------------------------|-----------------|-------------|---------------------|')
		print('|   ID   |      Date       |          Merchant         |   Description   |    Amount   |       Category      |')
		print('|--------|-----------------|---------------------------|-----------------|-------------|---------------------|')
		records_list = []
		for i in records:
			records_list.append(i)
		for i in records_list:
			time.sleep(.1)
			print('| ' + "{:^6}".format(i[0]) + ' | ' + "{:^15}".format(i[1]) + ' | ' + "{:^25}".format(i[2]) + ' | ' + "{:^15}".format(i[3])
			+ ' | ' + "${:^10.2f}".format(i[4]) + ' | ' + "{:^20}".format(i[5]) + '|')
		print('|--------|-----------------|---------------------------|-----------------|-------------|---------------------|')
		print()
	except sqlite3.Error as error:
		print("Failed to read data from sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()


### Function to Totalize the Selected Transactions, Runs in Conjunction with the SelectTransactions Functuion ###
def SelectTransactionsTotal(date1, date2, user):
	try:
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		total_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(total_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Total Expenses Are: $' + '{:.2f}'.format(item[0] or 0))

		cursor2 = sqliteConnection.cursor()
		deposits_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) > 0 AND Date BETWEEN ? and ? and User = ?"""
		cursor2.execute(deposits_query, (date1, date2, user))
		deposits = cursor2.fetchmany()
		for item in deposits:
			print('Total Deposits Are: $' + '{:.2f}'.format(item[0] or 0))

		print()
		cont = input('Press Enter to Continue')
	except sqlite3.Error as error:
		print("Failed to read data from sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()

### Function to Update a Record ###
def updateSqliteTable(Date, Merchant, Description, Amount, Category, ID, User):
	try:
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		sql_update_query = """Update Expenses Set Date = ?, Merchant = ?, Description = ?, Amount = ?, Category = ? WHERE ID = ? AND User = ?"""
		data = (Date, Merchant, Description, Amount, Category, ID, User)
		cursor.execute(sql_update_query, data)
		sqliteConnection.commit()
		print()
		print("Record Updated successfully")
		print()
		esc = input('Press Enter to Continue')
		cursor.close()

	except sqlite3.Error as error:
		print("Failed to update sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()
			print("The sqlite connection is closed")

### FUNCTION TO DELETE RECORD ###
def DeleteRecord(id):
    try:
        sqliteConnection = sqlite3.connect('Expenses.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """DELETE from Expenses where id = ?"""
        cursor.execute(sql_update_query, (id, ))
        sqliteConnection.commit()
        esc = input("\nRecord deleted successfully\nPress Enter to Continue")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


print()
print('|------------------------------------------------------------------------------------------------------------|')
time.sleep(.2)
print('|                                                                                                            |')
time.sleep(.2)
print('|                          WELCOME TO THE EXPENSE-O-TRON 9000 ACCOUNTING SYSTEM                              |')
time.sleep(.2)
print('|                                                                                                            |')
time.sleep(.2)
print('|------------------------------------------------------------------------------------------------------------|')
print()
# time.sleep(1)
cont = input('Press any Key to Continue...')

CurrentUser()
print('Current User is ' + str(current_user))

### Flag That Runs the For Loop ###
flag = False

while flag == False:
	print()
	for i in navigation:
		print(i)
	ask = input('> ')
	if ask == str(1):
		selectionnav1 = False
		while selectionnav1 == False:
			print()
			selection1 = input('Is this an Expense or Deposit? \n1 - Expense\n2 - Income\n3 - Return to Previous Menu\n> ')
			if selection1 == str(1):
				selectionnav1 == True
				print('Please Input Transaction Information:')
				print()
				i_date = input('Enter Date as MM/DD/YYYY > ')
				i_merchant = input('Enter Merchant Name > ')
				i_description = input('Enter Transaction Description > ')
				i_amount = input('Enter Amount of Transaction > ')\
				### Function to Load the Selection of Expense Categories
				ExpenseSelection()
				InsertToTable(i_date, i_merchant, i_description, (float(i_amount) * -1), expense_category, current_user)
			elif selection1 == str(2):
				selectionnav1 == True
				print('Please Input Transaction Information:')
				print()
				i_date = input('Enter Date as MM/DD/YYYY > ')
				i_merchant = input('Enter Merchant Name > ')
				i_description = input('Enter Transaction Description > ')
				i_amount = input('Enter Amount of Transaction > ')
				### Function to Load the Selection of Income Categories
				IncomeSelection()
				InsertToTable(i_date, i_merchant, i_description, i_amount, income_category, current_user)
			elif selection1 == str(3):
				break
			else:
				break
		cursor.close()
	elif ask == str('2'):
		start_date = input('Enter Start Date as MM/DD/YYYY > ')
		end_date = input('Enter End Date as MM/DD/YYYY > ')
		SelectTransactions(start_date, end_date, current_user)
		SelectTransactionsTotal(start_date, end_date, current_user)
		cursor.close()
	elif ask == str('3'):
		selectionnav3 = False
		while selectionnav3 == False:
			selection3 = input('Is this an Expense or Deposit? \n1 - Expense\n2 - Deposit\n3 - Return to Previous Menu\n> ')
			if selection3 == str(1):
				selectionnav3 == True
				print('Please Input Transaction Information:')
				print()
				i_ID = input('Enter Transaction ID > ')
				i_date = input('Enter Date as MM/DD/YYYY > ')
				i_merchant = input('Enter Merchant Name > ')
				i_description = input('Enter Transaction Description > ')
				i_amount = input('Enter Amount of Transaction > ')
				### Function to Load the Selection of Expense Categories
				ExpenseSelection()
				updateSqliteTable(i_date, i_merchant, i_description, (float(i_amount) * -1), expense_category, i_ID, current_user)
			elif selection3 == str(2):
				selectionnav3 == True
				print('Please Input Transaction Information:')
				print()
				i_ID = input('Enter Transaction ID > ')
				i_date = input('Enter Date as MM/DD/YYYY > ')
				i_merchant = input('Enter Merchant Name > ')
				i_description = input('Enter Transaction Description > ')
				i_amount = input('Enter Amount of Transaction > ')
				### Function to Load the Selection of Income Categories
				IncomeSelection()
				updateSqliteTable(i_date, i_merchant, i_description, i_amount, income_category, i_ID, current_user)
			elif selection3 == str(3):
				break
			else:
				break
	elif ask == str('4'):
		i_ID = input('Input the ID of the Transaction to be Deleted\n>')
		DeleteRecord(i_ID, current_user)
	elif ask == str('5'):
		current_user = ''
		CurrentUser()
		print('Current User is: ' + str(current_user))
	elif ask == str('6') or 'goodbye':
		print('Goodbye!')
		flag = True
