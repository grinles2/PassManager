# импорты

from tkinter import *
from tkinter import messagebox as mb
from random import choice
from plyer import notification
from win10toast import ToastNotifier
toast = ToastNotifier()


# функции
def SavePass():
    NameOfService = e.get()
    print(NameOfService)
    thePass = a.get()
    print(thePass)
    with open("password.txt", "a", encoding="UTF-8") as file: # записываем пароль
        file.write(f"{NameOfService} --->>> {thePass}\n")
        notification.notify(message="Пароль сохранён", app_icon="logo.ico")
        e.delete(0, END)  # всё с него
        a.delete(0, END)  # всё с него


def clearFile():
    answer = mb.askyesno(title="Вопрос",message="Вы уверены?")
    if answer:
        with open('password.txt', 'w'):
            pass

def deleteLast():
    answer1 = mb.askyesno(title="Вопрос", message="Вы уверены?")
    if answer1:
        with open('password.txt', 'r') as f:
            lines = f.readlines()
            lines = lines[:-1]

        with open('password.txt', 'w') as f:
            f.writelines(lines)




def BlackBG():
    root.config(bg="grey")
def CyanBG():
    root.config(bg="cyan")
def RedBG():
    root.config(bg="red")
def YellowBG():
    root.config(bg="yellow")

#---------------------------------------------



def readEula():
    a = Toplevel()
    root.iconbitmap('logo1.ico')  # лого
    a.geometry('300x300')
    a['bg'] = 'white'
    b = Label(root,
                    text="Бу",
                    font=("Comic Sans MS", 13, "bold")
                    )
    b.place(relx=1, y=50, anchor=CENTER)

#--------------------------------------------------------------

root = Tk()

mainmenu = Menu(root)


filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Очистить", command= clearFile)
filemenu.add_command(label="Удалить Последний", command= deleteLast)


helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Серый фон", command= BlackBG)
helpmenu.add_command(label="Бирюзовый Фон", command= CyanBG)
helpmenu.add_command(label="Красный фон", command= RedBG)
helpmenu.add_command(label="Жёлтый фон", command= YellowBG)



window = Menu(mainmenu, tearoff=0)
window.add_command(label="Прочитать", command= readEula)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Пароли", menu=filemenu)
mainmenu.add_cascade(label="Фон", menu=helpmenu)
#mainmenu.add_cascade(label="EULA", menu=window)


root.title("Менеджер Паролей")
root.geometry("600x600")
root.config(bg = "cyan")
root.iconbitmap('logo1.ico') # лого
root.resizable(width=False, height=False) # запрет на расширение
# ---------------------------------------------------------------------------------------


service = Label(root,
             text = "Сохранить Пароль",
             font = ("Comic Sans MS", 13, "bold"),

             )

# показать кнопку
service.place(relx = 0.3, y = 10, anchor=CENTER)
# Сервис Откуда Пароль

# -----------------------------------------------------------------------------------------------
serviceName = Label(root,
             text = "Сервис",
             font = ("Comic Sans MS", 13, "bold"),

             )
serviceName.place(relx = 0.07, y = 60, anchor=CENTER)




e = Entry(root, font = "Ariel 13") # текстовое поле
e.place(relx= 0.3, y=60, anchor=CENTER)  # координаты текстового поля

# -------------------------------------------------------------------------------------------------------

password = Label(root,
             text = "Пароль",
             font = ("Comic Sans MS", 13, "bold"),

             )

password.place(relx = 0.07, y = 110, anchor=CENTER)

a = Entry(root, font = "Ariel 13") # текстовое поле
a.place(relx= 0.3, y=110, anchor=CENTER)  # координаты текстового поля


btn = Button(root, text="Сохранить", font= ("Seymour One", 13, "bold"), command=SavePass)  # отпровляемся к функц SavePass
btn.place(relx=0.25, y=200, anchor= CENTER)


#--------------------------------------------------------------------------------------------------------------------------------------------

allPass = Label(root,
             text = "Найти Пароль",
             font = ("Comic Sans MS", 13, "bold"),
             )
allPass.place(relx = 0.7, y = 10, anchor=CENTER)


ServiceName = Label(root,
             text = "Сервис",
             font = ("Comic Sans MS", 13, "bold"),
             )
ServiceName.place(relx = 0.55, y = 60, anchor=CENTER)



b = Entry(root, font = "Ariel 13") # текстовое поле
b.place(relx= 0.78, y=60, anchor=CENTER)  # координаты текстового поля

#---------------------------------------------------------------------------------------------------------------------------------------
def SearchPass():
    findService = b.get()   # из текстового поля ServiceName
    print(findService)

    with open("password.txt", "r", encoding="UTF-8") as file:  # Читаем пароли из файла
        lines = file.readlines()

    passwords = {}
    for line in lines:
        service, password = line.strip().split(" --->>> ")  # Разделяем имя сервиса и пароль
        passwords[service] = password

    if findService in passwords:  # Проверяем, есть ли введенный сервис в словаре паролей
        thePass = passwords[findService]
        PassWord.delete(0, END)  # Очищаем текстовое поле c
        PassWord.insert(0, thePass)  # Выводим пароль в текстовое поле c
        root.clipboard_clear()
        root.clipboard_append(thePass)  # вставить в буфер обмена
    else:
        PassWord.delete(0, END)  # Очищаем текстовое поле c
        PassWord.insert(0, "Сервис Не Найден")  # Выводим сообщение об ошибке
        notification.notify(message="Сервис Не найден", app_icon="logo.ico")
#--------------------------------------------------------------------------------------------------------------------------------------
passWordLabel = Label(root,
             text = "Пароль",
             font = ("Comic Sans MS", 13, "bold"),
             )
passWordLabel.place(relx = 0.55, y = 200, anchor=CENTER)

PassWord = Entry(root, font = "Ariel 13") # текстовое поле
PassWord.place(relx= 0.78, y=200, anchor=CENTER)  # координаты текстового поля

btn1 = Button(root, text="Найти", font= ("Seymour One", 13, "bold"), command=SearchPass) # отпровляемся к функц SavePass
btn1.place(relx=0.7, y=110, anchor= CENTER)
root.mainloop()   # показываем окно