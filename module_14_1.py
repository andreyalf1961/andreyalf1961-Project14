import sqlite3

con = sqlite3.connect('not_telegram.db')
cur = con.cursor()

cur.execute("DROP TABLE Users")
cur.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cur.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
                (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', f'1000'))

for i in range(1, 11, 2):
    cur.execute('UPDATE Users SET balance=? WHERE username=?', (500, f"User{i}"))

for i in range(1, 11, 3):
    cur.execute('DELETE FROM Users WHERE username=?', (f'User{i}',))

cur.execute('SELECT username,email, age, balance FROM Users WHERE age!=?', (60,))
users = cur.fetchall()
for user, email, age, balance in users:
    print(f'Имя: {user} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

con.commit()
con.close()
