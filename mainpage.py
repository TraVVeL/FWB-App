from tkinter import messagebox
import bcrypt
import customtkinter as ctk
from data_base import *
from config import *
from Validator import *
import main


def change_appearance_mode_event(new_appearance_mode):
    ctk.set_appearance_mode(new_appearance_mode)


class App(ctk.CTk):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.title("Главная")
        self.geometry("700x650")
        self.resizable(False, False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.transaction = {}
        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Онлайн-Банк",
                                                   font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=0, pady=20)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="Профиль",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"), anchor="w",
                                         command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                            border_spacing=10, text="Вывод и пополнение",
                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"), anchor="w",
                                            command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                            border_spacing=10, text="Выход",
                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"), anchor="w",
                                            command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # create theme appearance mode menu
        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame,
                                                      values=["Light", "Dark", "System"],
                                                      command=change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.uData = list(get_user_data(self.name).values())
        entry_text = f"Доброго времени, {self.uData[0]}", f"Номер карты: {self.uData[2]}", \
            f"CVV карты: {self.uData[3]}", f"Дата истчения срока: {self.uData[4]}", f"Баланс: {self.uData[5]}"

        for y, text in enumerate(entry_text):
            self.label = ctk.CTkLabel(self.home_frame, text=text, font=font2)
            self.label.place(x=20, y=40 * (y + 1))

        # create second frame
        self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.label_name = ctk.CTkLabel(self.second_frame, corner_radius=0, text='Логин от аккаунта',
                                       font=font3, width=250, anchor='w')
        self.label_name.place(x=150, y=25)

        self.label_password = ctk.CTkLabel(self.second_frame, corner_radius=0, text='Пароль от аккаунта',
                                           font=font3, width=250, anchor='w')
        self.label_password.place(x=150, y=115)

        self.label_card_sender = ctk.CTkLabel(self.second_frame, corner_radius=0, text='Карта отправителя',
                                              font=font3, width=250, anchor='w')
        self.label_card_sender.place(x=150, y=195)

        self.label_card_cvv = ctk.CTkLabel(self.second_frame, corner_radius=0, text='cvv', font=font3,
                                           width=250, anchor='w')
        self.label_card_cvv.place(x=150, y=285)
        self.label_card_date = ctk.CTkLabel(self.second_frame, corner_radius=0, text='Срок службы',
                                            font=font3, width=250, anchor='w')
        self.label_card_date.place(x=280, y=285)

        self.label_card_receiver = ctk.CTkLabel(self.second_frame, corner_radius=0, text='Карта получателя',
                                                font=font3, width=250, anchor='w')
        self.label_card_receiver.place(x=150, y=355)

        self.label_card_sum = ctk.CTkLabel(self.second_frame, corner_radius=0, text='Сумма перевода',
                                           font=font3, width=250, anchor='w')
        self.label_card_sum.place(x=150, y=445)

        self.entry_name = ctk.CTkEntry(self.second_frame, width=250, height=50, font=font2)
        self.entry_name.place(x=150, y=50)

        self.entry_password = ctk.CTkEntry(self.second_frame, show='*', width=250, height=50, font=font2)
        self.entry_password.place(x=150, y=140)

        self.entry_card_sender = ctk.CTkEntry(self.second_frame, placeholder_text='XXXX-XXXX-XXXX-XXXX',
                                              width=250, height=50, font=font2)
        self.entry_card_sender.place(x=150, y=220)
        self.entry_card_sender.bind("<KeyRelease>", lambda event: self.validate_1(event))

        self.entry_cvv = ctk.CTkEntry(self.second_frame, placeholder_text='XXX', width=120, height=30,
                                      font=font2)
        self.entry_cvv.place(x=150, y=310)
        self.entry_cvv.bind("<KeyRelease>", lambda event: self.validate_2(event))

        self.entry_date_exp = ctk.CTkEntry(self.second_frame, placeholder_text='XX/XXXX', width=120,
                                           height=30, font=font2)
        self.entry_date_exp.place(x=280, y=310)
        self.entry_date_exp.bind("<KeyRelease>", lambda event: self.validate_3(event))

        self.entry_card_receiver = ctk.CTkEntry(self.second_frame, placeholder_text='XXXX-XXXX-XXXX-XXXX',
                                                width=250, height=50, font=font2)
        self.entry_card_receiver.place(x=150, y=380)
        self.entry_card_receiver.bind("<KeyRelease>", lambda event: self.validate_4(event))

        self.entry_card_sum = ctk.CTkEntry(self.second_frame, placeholder_text='100', width=250, height=50,
                                           font=font2)
        self.entry_card_sum.place(x=150, y=470)
        self.entry_card_sum.bind("<KeyRelease>", lambda event: self.validate_5(event))

        self.button_submit = ctk.CTkButton(self.second_frame, text='Отправить', font=font2, width=250,
                                           height=50, command=self.final_event)
        self.button_submit.place(x=150, y=550)

        #
        # LABELS ERROR
        #
        self.label_card_sender_error = ctk.CTkLabel(self.second_frame, text='', height=20)
        self.label_card_sender_error.place(x=150, y=270)
        self.label_cvv_error = ctk.CTkLabel(self.second_frame, text='', height=20)
        self.label_cvv_error.place(x=150, y=340)
        self.label_date_error = ctk.CTkLabel(self.second_frame, text='', height=20)
        self.label_date_error.place(x=280, y=340)
        self.label_card_receiver_error = ctk.CTkLabel(self.second_frame, text='', height=20)
        self.label_card_receiver_error.place(x=150, y=430)
        self.label_card_sum_error = ctk.CTkLabel(self.second_frame, text='', height=20)
        self.label_card_sum_error.place(x=150, y=520)

    def validate_1(self, event):
        entry_name = event.widget
        entry_value = entry_name.get()
        result = is_card(entry_value)
        if result:
            self.entry_card_sender.configure(border_color="green", text_color='green')
            self.label_card_sender_error.configure(text="")
            self.transaction.update({'sender': entry_value})
        else:
            self.entry_card_sender.configure(border_color="#993333", text_color='#993333')
            self.label_card_sender_error.configure(text="Неверный формат")
            self.transaction.update({'sender': None})

    def validate_2(self, event):
        entry_name = event.widget
        entry_value = entry_name.get()
        result = is_cvv(entry_value)
        if result:
            self.entry_cvv.configure(border_color="green", text_color='green')
            self.label_cvv_error.configure(text="")
            self.transaction.update({'cvv': entry_value})
        else:
            self.entry_cvv.configure(border_color="#993333", text_color='#993333')
            self.label_cvv_error.configure(text="Неверный формат")
            self.transaction.update({'cvv': None})

    def validate_3(self, event):
        entry_name = event.widget
        entry_value = entry_name.get()
        result = is_card_date(entry_value)
        if result:
            self.entry_date_exp.configure(border_color="green", text_color='green')
            self.label_date_error.configure(text="")
            self.transaction.update({'date_exp': entry_value})
        else:
            self.entry_date_exp.configure(border_color="#993333", text_color='#993333')
            self.label_date_error.configure(text="Неверный формат")
            self.transaction.update({'date_exp': None})

    def validate_4(self, event):
        entry_name = event.widget
        entry_value = entry_name.get()
        result = is_card(entry_value)
        if result:
            self.entry_card_receiver.configure(border_color="green", text_color='green')
            self.label_card_receiver_error.configure(text="")
            self.transaction.update({'receiver': entry_value})
        else:
            self.entry_card_receiver.configure(border_color="#993333", text_color='#993333')
            self.label_card_receiver_error.configure(text="Неверный формат")
            self.transaction.update({'receiver': None})

    def validate_5(self, event):
        entry_name = event.widget
        entry_value = entry_name.get()
        result = is_digit(entry_value)
        if result:
            self.entry_card_sum.configure(border_color="green", text_color='green')
            self.label_card_sum_error.configure(text="")
            self.transaction.update({'sum': entry_value})
        else:
            self.entry_card_sum.configure(border_color="#993333", text_color='#993333')
            self.label_card_sum_error.configure(text="Неверный формат")
            self.transaction.update({'sum': None})

    def final_event(self):
        entry_uName = self.entry_name.get()
        entry_uPassword = self.entry_password.get()
        entry_uCard = self.entry_card_sender.get()
        entry_uCvv = self.entry_cvv.get()
        entry_uDate = self.entry_date_exp.get()
        entry_uBalance = self.entry_card_sum.get()
        entry_uReceiver = self.entry_card_receiver.get()
        if entry_uName != '' and entry_uPassword != '':
            cursor.execute('SELECT password, CARD, CVV, DATE_EXP, balance FROM users WHERE username=?', [entry_uName])
            result, card, cvv, date_exp, balance = cursor.fetchone()
            if result:
                if bcrypt.checkpw(entry_uPassword.encode('utf-8'), result):
                    if card == conc_card(entry_uCard):
                        if cvv == entry_uCvv:
                            if date_exp == entry_uDate:
                                if (conc_card(entry_uReceiver),) in get_all_card():
                                    if balance >= float(entry_uBalance) and float(entry_uBalance) > 0:
                                        if conc_card(entry_uCard) != conc_card(entry_uReceiver):
                                            cursor.execute('UPDATE users SET balance = balance + ? WHERE CARD = ?',
                                                           (float(entry_uBalance), conc_card(entry_uReceiver)))
                                            cursor.execute('UPDATE users SET balance = balance - ? WHERE CARD = ?',
                                                           (float(entry_uBalance), conc_card(entry_uCard)))
                                            conn.commit()
                                            messagebox.showinfo('Успешно', 'Транцакия была успешно оправлена')
                                        else:
                                            messagebox.showerror('Ошибка', 'Нелья делать транзацкию на свой счёт')
                                    else:
                                        messagebox.showerror('Ошибка', 'Баланс вашей карты меньше, суммы, которую хотите снять\nили\n')
                                else:
                                    messagebox.showerror('Ошибка',
                                                         'Похоже, что карты, на которую вы хотите перевести не существует')
                            else:
                                messagebox.showerror('Ошибка', 'Срок действия карты неверный')
                        else:
                            messagebox.showerror('Ошибка', 'CVV-код неверный')
                    else:
                        messagebox.showerror('Ошибка',
                                             'Похоже, что карты, с которой вы хотите снять денежные средства не существует')
                else:
                    messagebox.showerror('Ошибка', 'Пароль не верный')
            else:
                messagebox.showerror('Ошибка', 'Логин не верный')
        else:
            messagebox.showerror('Ошибка', 'Введите значения во все поля')

    def home_button_event(self):
        self.select_frame_by_name('Профиль')

    def frame_2_button_event(self):
        self.select_frame_by_name('Вывод и пополнение')

    def frame_3_button_event(self):
        if messagebox.askyesno('Выход', 'Вы действительно хотите выйти?'):
            App.destroy(self)


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == 'Профиль' else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == 'Вывод и пополнение' else "transparent")

        # show selected frame
        if name == 'Профиль':
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == 'Вывод и пополнение':
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
