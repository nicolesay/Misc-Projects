import sqlite3
current_user = ''

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

CurrentUser()



sqliteConnection = sqlite3.connect('Expenses.db')
cursor = sqliteConnection.cursor()
user_select = 'SELECT * FROM ' + str(current_user)
cursor.execute(user_select)
users = cursor.fetchall()
