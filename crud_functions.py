import sqlite3


def initiate_db():
    con = sqlite3.connect('products.db')
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER  NOT NULL
    )
    ''')

    con.commit()
    con.close()


def add_user(username, email, age):
    con = sqlite3.connect('products.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)',
                (f'{username}', f'{email}', f'{age}', 1000))

    con.commit()
    con.close()


def is_included(username):
    con = sqlite3.connect('products.db')
    cur = con.cursor()
    user = cur.execute('SELECT * FROM Users WHERE username=?', (username,))
    if user.fetchone() is None:
        con.close()
        return False
    else:
        con.close()
        return True


def get_all_products():
    con = sqlite3.connect('products.db')
    cur = con.cursor()
    cur.execute('SELECT COUNT(*) FROM Products')
    count = cur.fetchone()[0]

    if count == 0:
        for i in range(1, 5):
            cur.execute('INSERT INTO Products (id,title,description, price) VALUES(?,?,?,?)',
                        (f'{i}', f'Продукт{i}', f'Описание{i}', f'{i * 100}'))
    cur.execute('SELECT * FROM Products')
    products = cur.fetchall()

    con.commit()
    con.close()
    return products
