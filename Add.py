import pyodbc

try:
    con_string = 'C:\AllHere\Учеба\БД\Первый сем\Дз\Состав_колледжа'
    connect = pyodbc.connect(con_string)
    print("Connected To Database")

    Student = (2, 'Пермяков', 'Дмитрий', 'Евгеньевич', '13.10.2004', 'И', '21', '01.09.2022', 'М', '55500')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO Студенты VALUES (?,?,?,?,?,?,?,?,?,?)', Student)
    connect.commit()
    print('Data Inserted')

except pyodbc.Error as e:
    print("Error in Connection")
