from tkinter import messagebox
from data_base import *
import bcrypt
import mainpage
import admin_menu
from generate_card import *


def signup(user_username, user_password):
    username = user_username.get()
    password = user_password.get()

    if username != '' and password != '':
        cursor.execute('SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Ошибка', 'Пользователь уже существует!')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)',
                           [username, hashed_password, generate_credit_card_number(), generate_cvv(),
                            generate_expiry_date(), 10000])
            conn.commit()
            messagebox.showinfo('Успешно', 'Аккаунт был создан!')
    else:
        messagebox.showerror('Ошибка', 'Введите значения во все поля!')


def login_account(user_username, user_password, destroy_window):
    username = user_username.get()
    password = user_password.get()
    if username != '' and password != '':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                if username == 'admin':
                    admin = admin_menu.App()
                    destroy_window()
                    admin.mainloop()
                app = mainpage.App(name=username)
                destroy_window()
                app.mainloop()
            else:
                messagebox.showerror('Ошибка', 'Пароль не верный')
        else:
            messagebox.showerror('Ошибка', 'Логин не верный')

    else:
        messagebox.showerror('Ошибка', 'Введите значения во все поля')
