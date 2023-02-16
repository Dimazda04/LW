import pyodbc

try:
    con_string = 'C:\AllHere\Учеба\БД\Первый сем\Дз\Состав_колледжа'
    connect = pyodbc.connect(con_string)
    print("Connected To Database")

    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Студенты')
    for row in cursor.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Error in Connection")
