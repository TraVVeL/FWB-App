from tkinter import ttk
from config import *
import tkinter as tk
import os
from tkinter import messagebox
import sqlite3


def sortby(tv, col, descending):
    data = [(tv.set(child, col), child) for child in tv.get_children('')]
    data.sort(reverse=descending)
    for index, item in enumerate(data):
        tv.move(item[1], '', index)
        tv.heading(col, command=lambda: sortby(tv, col, int(not descending)))


def show_table(frame, db_path='data.db', table_name='users'):
    if os.path.isfile(db_path):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(f"SELECT * FROM {table_name}")
                rows_count = cursor.fetchone()[0]
            except sqlite3.OperationalError:
                rows_count = False

            if rows_count:
                cursor.execute(f"SELECT * FROM {table_name}")
                data = cursor.fetchall()
                concatenated_list = ('Пользователь', 'Пароль', 'Карта', 'CVV', 'Скрок истчения карты', 'Баланас')
                # Создаем Treeview-виджет с горизонтальной и вертикальной прокруткой

                style = ttk.Style(frame)
                style.theme_use('alt')
                style.configure("Treeview", background='#242424', foreground='#fff', bordercolor='', font=font3)
                style.configure("Treeview.Heading", background='#242424', foreground='#fff', bordercolor='#242424', font=font3)
                style.map("Treeview.Heading", background=[("active", "#242424")], foreground=[("active", "white")])

                table = ttk.Treeview(frame, show="headings", selectmode="browse")
                table["columns"] = concatenated_list
                table["displaycolumns"] = concatenated_list

                for head in concatenated_list:
                    # Устанавливаем опцию stretch для каждого заголовка столбца
                    table.heading(head, text=head, anchor=tk.CENTER,
                                  command=lambda c=head: sortby(table, c, 0))
                    table.column(head, anchor=tk.CENTER, width=100, minwidth=50, stretch=True)
                for row in data:
                    table.insert('', tk.END, values=tuple(row))
                    table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            else:
                messagebox.showinfo("Пустая таблица", "Таблица не содержит данных.")
    else:
        messagebox.showinfo("Пустая таблица", "Таблица не содержит данных.")
