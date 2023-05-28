import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL, 
    password TEXT NOT NULL,
    CARD TEXT NOT NULL,
    CVV TEXT NOT NULL,
    DATE_EXP TEXT NOT NULL,
    balance INTEGER
    )''')


def get_user_data(name):
    cursor.execute("SELECT * FROM users WHERE username=?", [name])
    row = cursor.fetchone()
    user_dict = {'uName': row[0], 'uPassword': row[1], 'uCard': row[2], 'uCvv': row[3], 'uDate_exp': row[4], 'uBalance': row[5]}
    return user_dict


def get_all_card():
    cursor.execute("SELECT CARD FROM users")
    get_card = cursor.fetchall()
    return get_card
