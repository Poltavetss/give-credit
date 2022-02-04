#Text
welcome_lbl = Label(window, text="Доброго времени суток!",foreground="Blue", font=("Arial Black", 28,))
main_lbl = Label(window, text=""" Далее вам предлагается пройти небольшой опрос,
чтобы узнать ваши шансы получить кредит в нашем банке""", font=("Lucida Sans Unicode", 16))
Ps_lbl1 = Label(window, text="""Нажимая кнопку 'Пройти тест', вы соглашаетесь с тем, что ваши данные будут записаны и обработаны.*""", foreground="Gray", font=("Lucida Sans Unicode", 8))
Ps_lbl2 = Label(window, text="*Не волнуйтесь, мы всё удалим;)", foreground="Gray", font=("Lucida Sans Unicode", 7))

#TextPosition
welcome_lbl.grid(column=0, row=0)
main_lbl.grid(column=0, row=1)
Ps_lbl1.grid(column=0, row=3)
Ps_lbl2.grid(column=0, row=5)


def clicked():
    window.geometry("900x215")
    main_lbl.grid(column=0, row=0)
    main_lbl(text="""                 Опрос состоит всего из 5 вопросов.
        И помните- итоговое решенеие всегда принимает сотрудник банка,
         поэтому в случае отказа- не растраивайтесь!!!""", font=("Lucida Sans Unicode", 16))

    def start():
        start_btn = Button(window, text="Я готов, начинаем!", fg="White", bg="Blue", padx=5, pady=5, command=test_start)
        start_btn.grid(column=0, row=2, )
        start_btn.place(relx=.45, rely=.7)

    start()

#Button


def delete():
    destroy_object = [Ps_lbl1, Ps_lbl2, next_btn, chk, welcome_lbl, main_lbl]
    for object_name in destroy_object:
        if object_name.winfo_viewable():
            object_name.grid_remove()
        else:
            object_name.grid()

def next_screen():
    if chk_state.get():
        messagebox.showwarning("Внимание!", "Вы не согласны с условиями работы по!")
    else:
        clicked()
        delete()

next_btn = Button(window, text="Пройти тест", fg="White", bg="Blue", command=next_screen)
next_btn.grid(column=0, row=2)


def test_start():
    age_lbl = Label(window, text="Сколько вам лет?",font=("Lucida Sans Unicode", 15))
    age_lbl.grid(column=0, row=1)
    age_lbl.place(relx=.42, rely=.2)
    age = Entry(window)
    age.grid(column=4, row=4)