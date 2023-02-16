import pyodbc

try:
    con_string = 'C:\AllHere\Учеба\БД\Первый сем\Дз\Состав_колледжа'
    connect = pyodbc.connect(con_string)
    print("Connected To Database")

    Student_ID = 7

    cursor = connect.cursor()
    cursor.execute('DELETE FROM Студенты WHERE Шифр = ?', Student_ID)
    connect.commit()
    print("Data deleted")

except pyodbc.Error as e:
    print("Error in Connection")
