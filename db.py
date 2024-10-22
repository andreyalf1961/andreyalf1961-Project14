import sqlite3
from random import randint

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# cursor.execute("DROP TABLE Users") #удалить таблицу

# for i in range(30):
#     cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
#                    (f'username{i}', f'email{i}ex@gmail.com', str(randint(14,92))))


# cursor.execute('UPDATE Users SET age=? WHERE username=?', (29, 'username0'))
#
# cursor.execute('DELETE FROM Users WHERE username=?', ('username1',))

# cursor.execute('SELECT * FROM Users') # выбрать всех
# users = cursor.fetchall()
# for user in users:
#     print(user)

#cursor.execute('SELECT username,age FROM Users WHERE age>?', (29,))
# users = cursor.fetchall()
# for user in users:
#     print(user)

# cursor.execute(("SELECT username, age FROM Users GROUP BY AGE"))
# users = cursor.fetchall()
# for user in users:
#     print(user)

# общее количество
# cursor.execute('SELECT COUNT(*) FROM Users')
# total1=cursor.fetchone()[0] #вытаскивает 1-й элемент выборки
# total1_1=cursor.fetchone()# если зарешетить total1, то результат [30,], если нет - None
# total2=cursor.fetchall()#вся выборка? пустой список,т.к только один элемент
# print(total1)
# print(total1_1)
# print(total2)

# выборка по возрасту(кол-во)
# cursor.execute('SELECT COUNT(*) FROM Users WHERE age>?', (33,))
# tot=cursor.fetchone()[0]
# print(tot)

# суммирование и ср возраст, max, min
cursor.execute('SELECT SUM(age) FROM Users')
tot1=cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM Users')
tot2=cursor.fetchone()[0]
print(tot1, tot1/tot2)

cursor.execute('SELECT AVG(age) FROM Users')
avg_age=cursor.fetchone()[0]
print(avg_age)

cursor.execute('SELECT MAX(age) FROM Users')
max_age=cursor.fetchone()[0]
print(max_age)

cursor.execute('SELECT MIN(age) FROM Users')
min_age=cursor.fetchone()[0]
print(min_age)




connection.commit()
connection.close()
