import sqlite3

def MakeTable(table_name):
    try:
        sqliteConnection = sqlite3.connect('Expenses.db')
        cursor = sqliteConnection.cursor()
        # sqlite_insert_with_param = """CREATE TABLE ? ('Name' TEXT)'"""
        cursor.execute(f"""CREATE TABLE {table_name} ('Name' TEXT)""")
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

table_name = input('Enter name of new table > ')
MakeTable(table_name)