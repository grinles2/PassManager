# импорты

from tkinter import *
from random import choice

# функции
def SavePass():
    NameOfService = e.get()
    print(NameOfService)
    thePass = a.get()
    print(thePass)
    with open("password.txt", "a", encoding="UTF-8") as file: # записываем пароль
        file.write(f"{NameOfService} --->>> {thePass}\n")


root = Tk()
root.title("Менеджер Паролей")
root.geometry("600x600")
root.config(bg = "cyan")
root.iconbitmap('logo.ico') # лого
root.resizable(width=False, height=False) # запрет на расширение

service = Label(root,
             text = "Сервис",
             font = ("Comic Sans MS", 13, "bold"),

             )

# показать кнопку
service.place(relx = 0.5, y = 10, anchor=CENTER)
# Сервис Откуда Пароль

e = Entry(root, font = "Ariel 13") # текстовое поле
e.place(relx= 0.5, y=60, anchor=CENTER)  # координаты текстового поля


password = Label(root,
             text = "Пароль",
             font = ("Comic Sans MS", 13, "bold"),

             )

password.place(relx = 0.5, y = 110, anchor=CENTER)

a = Entry(root, font = "Ariel 13") # текстовое поле
a.place(relx= 0.5, y=160, anchor=CENTER)  # координаты текстового поля


btn = Button(root, text="Сохранить Пароль", font= ("Seymour One", 17, "bold"), command=SavePass) # отпровляемся к функц SavePass
btn.place(relx=0.5, y=200, anchor= CENTER)









root.mainloop()   # показываем окно