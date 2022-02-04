from tkinter import *
from string import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showerror
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import csv
import time

model = joblib.load("give-credit.joblib")

#MainFrame
root = Tk()

frame = Frame(root)
frame.pack(side="top", expand=True, fill="both")
root.title("CreditNow...Программа оценки клиента")
root.geometry("575x200")
root.resizable(width=False, height=False)
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
root.wm_geometry("+%d+%d" % (x, y))


def set_data():

    def delete_page():
        for widget in frame.winfo_children():
            widget.destroy()



    def page2_open():
        delete_page()
        root.geometry("560x200")
        main_label = Label(frame, text="""Сейчас вам предстоит пройти опрос, состоящий из 5 вопросов.
        Не переживайте в случае отрицательного результата, 
        окончательный ответ всегда за сотрудником банка
        
        
ВЫ готовы?""", font=("Lucida Sans Unicode", 13))
        main_label.grid(column=0,row=0)
        start_btn = Button(frame, text="Да!", fg="White", bg="Blue", padx=5, pady=5, command=page3_open)
        exit_btn = Button(frame, text="Нет...", fg="Black", bg="White", padx=2, pady=2, command=quit)
        start_btn.grid(column=0, row=1,padx=20, ipadx=30)
        exit_btn.grid(column=0, row=2)

    def quit():
        root.quit()


    def page3_open():
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.wm_geometry("+%d+%d" % (x, y))
        root.geometry("150x150")
        def show_answer():
            global age_data
            if age.get().isdigit() and age.get() != '0':
                age_data = int(age.get())
                btn_confirm.destroy()
                btn_continue = Button(frame, text="Продолжить", command=page4_open)
                btn_continue.grid(row=2, ipadx=30, ipady=8, pady=30, padx=5)
                return (age_data)
            else:
                messagebox.showerror("Внимание!", "Вы можете нам доверять, отвечайте честно)")
        delete_page()
        main_label = Label(frame, text="""Сколько вам лет?""", font=("Lucida Sans Unicode", 12))
        main_label.grid(column=0, row=0, sticky=W)
        age = Entry(frame)
        age.focus_set()
        age.grid(column=0, row=1)
        btn_confirm = Button(frame, text="Подтвердить", command=show_answer)
        btn_confirm.grid(row=2, ipadx=30, ipady=8, pady=30, padx=5)

    def page4_open():
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
        root.wm_geometry("+%d+%d" % (x, y))
        root.geometry("357x200")
        def show_answer():
            global amount_data
            if amount.get().isdigit() and amount.get() != '0':
                amount_data = int(amount.get())
                btn_confirm.destroy()
                btn_continue = Button(frame, text="Продолжить", command=page5_open)
                btn_continue.grid(row=2, ipadx=30, ipady=8, pady=30, padx=5)
                return (amount_data)
            else:
                messagebox.showerror("Внимание!", "Введите допустимое значение!")
        delete_page()
        main_label = Label(frame, text="""На какую сумму кредита вы рассчитываете?""", font=("Lucida Sans Unicode", 12))
        main_label.grid(column=0, row=0, sticky=W)
        amount = Entry(frame)
        amount.focus_set()
        amount.grid(column=0, row=1)
        btn_confirm = Button(frame, text="Подтвердить", command=show_answer)
        btn_confirm.grid(row=2, ipadx=30, ipady=8, pady=30, padx=5)

    def page5_open():
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
        root.wm_geometry("+%d+%d" % (x, y))
        root.geometry("490x200")
        def show_answer():
            global income_data
            if income.get().isdigit():
                income_data = int(income.get())
                btn_confirm.destroy()
                btn_continue = Button(frame, text="Продолжить", command=page6_open)
                btn_continue.grid(row=2, ipadx=30, ipady=8, pady=30, padx=5)
                return (income_data)
            else:
                messagebox.showerror("Внимание!", "Введите число")
        delete_page()
        main_label = Label(frame, text="""Ваш средний ежемесячный доход за последние 6 месяцев?""", font=("Lucida Sans Unicode", 12))
        main_label.grid(column=0, row=0, sticky=W)
        income = Entry(frame)
        income.focus_set()
        income.grid(column=0, row=1)
        btn_confirm = Button(frame, text="Подтвердить", command=show_answer)
        btn_confirm.grid(row=2, ipadx=30, ipady=8, pady=30, padx=5)

    def page6_open():
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
        root.wm_geometry("+%d+%d" % (x, y))
        root.geometry("375x200")
        term_data = []
        def show_answer():
            global term_data
            if term.get().isdigit() and term.get() != '0':
                term_data = term.get()
                btn_confirm.destroy()
                btn_continue = Button(frame, text="Продолжить", command=page7_open)
                btn_continue.grid(row=2, ipadx=30, ipady=8, pady=30, padx=5)
                return (term_data)
            else:
                messagebox.showerror("Внимание!", "Введите допустимое значение!")
        delete_page()
        main_label = Label(frame, text="""На какой срок Вы хотите взять кредит?(мес)""", font=("Lucida Sans Unicode", 12))
        main_label.grid(column=0, row=0, sticky=W)
        term = Entry(frame)
        term.focus_set()
        term.grid(column=0, row=1)
        btn_confirm = Button(frame, text="Подтвердить", command=show_answer)
        btn_confirm.grid(row=2, ipadx=30, ipady=8, pady=30, padx=5)
        return (term_data)

    def page7_open():
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.wm_geometry("+%d+%d" % (x, y))
        root.geometry("200x30")
        def get_data():
            payouts = int(amount_data) / int(term_data)
            predictions = model.predict([[age_data, amount_data, income_data, payouts, term_data]])
            delete_page()
            progress_bar = ttk.Progressbar(frame, orient="horizontal",
                                           mode="determinate", maximum=100, value=0)
            label_1 = tk.Label(frame, text="Progress Bar")
            label_1.grid(row=0, column=0)
            progress_bar.grid(row=0, column=1)
            frame.update()
            progress_bar['value'] = 0
            frame.update()
            while progress_bar['value'] < 100:
                progress_bar['value'] += 1
                frame.update()
                time.sleep(0.1)
            if predictions == ['Кредит одобрен']:
                messagebox.showwarning("Поздравляем!", predictions)
                x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
                y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
                root.wm_geometry("+%d+%d" % (x, y))
                root.geometry("146x66")
                delete_page()
                exit_btn = Button(frame, text="Выход", command=quit).grid(column=0, row=0, ipadx=50, ipady=20)
            else:
                messagebox.showwarning("Сожалеем!", predictions)
                x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
                y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
                root.wm_geometry("+%d+%d" % (x, y))
                root.geometry("146x66")
                delete_page()
                exit_btn = Button(frame, text="Выход", command=quit).grid(column=0, row=0, ipadx=50, ipady=20)

        get_data()
    main_label = Label(frame, text="""Доброго времени суток! 
    Далее вам предлагается пройти небольшой опрос,
    чтобы узнать ваши шансы получить кредит в нашем банке""", font=("Lucida Sans Unicode", 12))
    main_label.grid(column=0, row=0)

    Ps_lbl1 = Label(frame,
                    text="""Нажимая кнопку "Приступить", вы соглашаетесь с тем, что ваши данные будут записаны и обработаны.*""",
                    foreground="Gray", font=("Lucida Sans Unicode", 8)).grid(column=0, row=3)
    Ps_lbl2 = Label(frame, text="*Не волнуйтесь, мы всё удалим;)", foreground="Gray",
                    font=("Lucida Sans Unicode", 7)).grid(column=0, row=4)

    start_btn = Button(frame, text="Приступить", command=page2_open).grid(column=0, row=1, ipadx=50, ipady=20)

set_data()
frame.pack()
root.mainloop()