import customtkinter as ctk
from config import *
from tkinter import messagebox
from DataBaseTable import show_table


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Админ-Панель")
        self.geometry("700x650")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="МЕНЮ", font=font3, anchor='w',
                                                   width=150, height=50)
        self.navigation_frame_label.grid(row=0, column=0, padx=10, pady=10)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="База данных",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"), anchor="w",
                                         command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                            border_spacing=10, text="Выход",
                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"), anchor="w",
                                            command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # create data base frame
        self.data_base = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        show_table(self.data_base)

    def home_button_event(self):
        self.select_frame_by_name('База данных')

    def frame_2_button_event(self):
        self.select_frame_by_name('Вывод и пополнение')

    def frame_3_button_event(self):
        if messagebox.askyesno('Выход', 'Вы действительно хотите выйти?'):
            App.destroy(self)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == 'База данных' else "transparent")
        # show selected frame
        if name == 'База данных':
            self.data_base.grid(row=0, column=1, sticky="nsew")
        else:
            self.data_base.grid_forget()
