from tkinter import *    
import pymysql
def click_bt(name):
    con = pymysql.connect(host="127.0.0.1",
                          user='root', 
                          password='lev2904', 
                          db='touragency',
                          charset='utf8'
                          )
     
    with con:
        cur = con.cursor()
        cur.execute(name)
        data=cur.fetchall()
        for row in data:
                    print(row)
    
        con.commit()
  
main_window = Tk()
main_window.title('Главная форма')
main_window.geometry('600x400')
wl_lbl = Label(main_window, text = 'Вы успешно зарегистрировались!', fg="#eee", bg="#555")
wl_lbl.grid(column=1, row=0)
to_lbl = Label(main_window, text = 'Перейти К:', font = 'Arial 16', pady = 10)
to_lbl.grid(column=1, row=1)
# def used_button(window, label, n_column, n_row):
#     button = Button(window, 
#              text=label,          # текст кнопки 
#              background="#555",     # фоновый цвет кнопки
#              foreground="#ccc",     # цвет текста
#              padx="20",             # отступ от границ до содержимого по горизонтали
#              pady="8",              # отступ от границ до содержимого по вертикали
#              font="16",              # высота шрифта
#              width=8
#              )
#     button.grid(column=n_column, row=n_row)
clients_btn =Button(main_window, 
             text="Clients",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             width=8,
             command = click_bt('SELECT * FROM clients')
             )
clients_btn.grid(column=0, row=3)
trips_btn =Button(main_window, 
             text="Trips",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16" ,            # высота шрифта
             width=8,
             command = click_bt('SELECT * FROM trips')
             )
trips_btn.grid(column=1, row=3)
travels_btn =Button(main_window, 
             text="Travels",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             width=8,
             command = click_bt('SELECT * FROM travels')
             )
travels_btn.grid(column=0, row=4)
tours_btn =Button(main_window, 
             text="Tours",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             width=8,
             command = click_bt('SELECT * FROM tours')
             )
tours_btn.grid(column=2, row=3)
countryes_btn =Button(main_window, 
             text="Countryes",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             width=8,
             command = click_bt('SELECT * FROM countryes')
             )
countryes_btn.grid(column=2, row=4)

hist_print = Label(main_window, text = 'Графики:', font = 'Arial 16', pady = 10, width = 15)
hist_print .grid(column=0, row=5)

f_hist_btn =Button(main_window, 
             text="Первый запрос",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             width=8
             )
f_hist_btn.grid(column=0, row=6)
s_hist_btn =Button(main_window, 
             text="Второй запрос",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             width=8
             )
s_hist_btn.grid(column=0, row=7)
t_hist_btn =Button(main_window, 
             text="Третий запрос",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             width=8
             )
t_hist_btn.grid(column=0, row=8)
tableau_lbl = Label(main_window, text = 'Аналитика Таблеу:', font = 'Arial 16', pady = 10, width = 15)
tableau_lbl .grid(column=2, row=5)
tabopen_btn =Button(main_window, 
             text="TABLEAU",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             width=8
             )
tabopen_btn.grid(column=2, row=7)
main_window.mainloop()
