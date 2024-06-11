# импорты

from tkinter import *
from tkinter import messagebox as mb
from random import choice
#import json
import os
from plyer import notification


# функции
def SavePass():
    NameOfService = e.get()
    print(NameOfService)
    thePass = a.get()
    print(thePass)
    userEmailGet = userEmailText.get()
    print(userEmailGet)
    with open("AccountPass.json", "a", encoding="UTF-8") as file:  # записываем пароль
        file.write(f"{NameOfService};{thePass};{userEmailGet}\n")
        notification.notify(message="Пароль сохранён", app_icon="logo.ico")
        e.delete(0, END)  # всё с него
        a.delete(0, END)  # всё с него
        userEmailText.delete(0, END)  # всё с него


def clearFile():
    try:
        answer = mb.askyesno(title="Вопрос",message="Вы уверены? Аккаунты будут удалены навсегда")
        if answer:
            os.remove("AccountPass.json")
    except FileNotFoundError:
        notification.notify(message="Файл Утерян/Повреждён/Пароль не был сохранён прежде", app_icon="logo.ico")


def clearPass():
    try:
        answer = mb.askyesno(title="Вопрос",message="Вы уверены? Пароли будут удалены навсегда")
        if answer:
            os.remove("GenPass.json")
    except FileNotFoundError:
        notification.notify(message="Файл Утерян/Повреждён/Пароль не был сохранён прежде", app_icon="logo.ico")


def deleteLast():
    try:
        answer1 = mb.askyesno(title="Вопрос", message="Вы уверены?")
        if answer1:
            with open('AccountPass.json', 'r') as f:
                lines = f.readlines()
                lines = lines[:-1]

            with open('AccountPass.json', 'w') as f:
                f.writelines(lines)
    except FileNotFoundError:
        notification.notify(message="Файл Утерян/Повреждён/Пароль не был сохранён прежде", app_icon="logo.ico")

def BlackBG():
    root.config(bg="grey")
    #with open('settings.json', 'w'):
        #with open("settings.json", "a", encoding="UTF-8") as file:  # записываем выбор
            #file.write(f"Colour;grey\n")

def CyanBG():
    root.config(bg="cyan")
    #with open('settings.json', 'w'):
       # with open("settings.json", "a", encoding="UTF-8") as file:  # записываем выбор
           # file.write(f"Colour;cyan\n")

def RedBG():
    root.config(bg="red")
    #with open('settings.json', 'w'):
       # with open("settings.json", "a", encoding="UTF-8") as file:  # записываем выбор
            #file.write(f"Colour;red\n")

def YellowBG():
    root.config(bg="yellow")
    #with open('settings.json', 'w'):
       # with open("settings.json", "a", encoding="UTF-8") as file:  # записываем выбор
           # file.write(f"Colour;yellow\n")

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

#---------------------------------------------------------------------------------
# Функции для страниц


def clearField():
    PassWord.delete(0, END)
    ExtraText.delete(0, END)
    b.delete(0, END)

def clearField1():
    d.delete(0, END)


def secondPage():
    root = Tk()

    mainmenu = Menu(root)
    root.title("Все Сервисы ")
    root.geometry("600x600")
    root.config(bg="cyan")
    root.iconbitmap('logo.ico')  # лого
    root.resizable(width=False, height=False)  # запрет на расширение

# -----------------------------------------------------------------------------------
    #Лейблы
    Title = Label(root,
             text = "Менеджер Паролей",
             font = ("Comic Sans MS", 17, "bold"),
             )
# показать кнопку
    Title.place(relx = 0.5, y = 40, anchor=CENTER)

    Title1 = Label(root,
             text = "Список Сервисов",
             font = ("Comic Sans MS", 17, "bold"),
             )

# показать кнопку
    Title1.place(relx = 0.5, y = 80, anchor=CENTER)

# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Текстовые Поля

    Output = Entry(root, font="Ariel 13")  # текстовое поле
    Output.place(relx=0.5, y=160, anchor=CENTER)  # координаты текстового поля


# -----------------------------------------------------------------------------------
# функции

    def OutputAllServices():
        try:
            with open("AccountPass.json", "r", encoding="UTF-8") as file:
                services = [line.strip().split(";")[0] for line in file.readlines()]
                output_text = " --->>> ".join(services)
                Output.delete(0, END)  # Очищаем текстовое поле
                Output.insert(END, output_text)  # Выводим имена сервисов в текстовое поле
        except FileNotFoundError:
            Output.insert(0, "Файл Утерян или не найден")
            notification.notify(message="Файл Утерян/Повреждён/Пароль не был сохранён прежде", app_icon="logo.ico")



    # Кнопки
    btn = Button(root, text="Вывести", font=("Seymour One", 17, "bold"),command=OutputAllServices)  # отпровляемся к функц OutputAllServices
    btn.place(relx=0.5, y=300, anchor=CENTER)



# -----------------------------------------------------------------------------------
# Маин лооп
    root.mainloop()


# -----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Очистить Все Аккаунты", command= clearFile)
filemenu.add_command(label="Удалить Последний Аккаунт", command= deleteLast)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Серый фон", command= BlackBG)
helpmenu.add_command(label="Бирюзовый Фон", command= CyanBG)
helpmenu.add_command(label="Красный фон", command= RedBG)
helpmenu.add_command(label="Жёлтый фон", command= YellowBG)


passwordList = Menu(mainmenu, tearoff=0)
passwordList.add_command(label="Очистить КЭШ Пароли", command= clearPass)


window = Menu(mainmenu, tearoff=0)
window.add_command(label="Прочитать", command= readEula)


pagemenu = Menu(mainmenu, tearoff=0)
pagemenu.add_command(label="Список всех сервисов", command= secondPage)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Менеджер Паролей", menu=filemenu)
mainmenu.add_cascade(label="Генератор Паролей", menu=passwordList)
mainmenu.add_cascade(label="Фон", menu=helpmenu)
mainmenu.add_cascade(label="Дополнительно", menu=pagemenu)
#mainmenu.add_cascade(label="EULA", menu=window)



root.title("Менеджер Паролей")
root.geometry("600x600")
root.config(bg = "cyan")
root.iconbitmap('logo.ico') # лого
root.resizable(width=False, height=False) # запрет на расширение
# ---------------------------------------------------------------------------------------


Title = Label(root,
             text = "Менеджер Паролей",
             font = ("Comic Sans MS", 17, "bold"),

             )

# показать кнопку
Title.place(relx = 0.5, y = 40, anchor=CENTER)





service = Label(root,
             text = "Сохранить Пароль",
             font = ("Comic Sans MS", 13, "bold"),

             )

service.place(relx = 0.3, y = 110, anchor=CENTER)


# -----------------------------------------------------------------------------------------------
serviceName = Label(root,
             text = "Сервис",
             font = ("Comic Sans MS", 13, "bold"),
             )
serviceName.place(relx = 0.07, y = 160, anchor=CENTER)




e = Entry(root, font = "Ariel 13") # текстовое поле
e.place(relx= 0.3, y=160, anchor=CENTER)  # координаты текстового поля

# -------------------------------------------------------------------------------------------------------

password = Label(root,
             text = "Пароль",
             font = ("Comic Sans MS", 13, "bold"),
             )

password.place(relx = 0.07, y = 260, anchor=CENTER)

a = Entry(root, font = "Ariel 13") # текстовое поле
a.place(relx= 0.3, y=260, anchor=CENTER)  # координаты текстового поля



userEmail = Label(root,
             text = "Доп",
             font = ("Comic Sans MS", 13, "bold"),
             )

userEmail.place(relx = 0.07, y = 210, anchor=CENTER)


userEmailText = Entry(root, font = "Ariel 13") # текстовое поле
userEmailText.place(relx= 0.3, y=210, anchor=CENTER)  # координаты текстового поля


btn = Button(root, text="Сохранить", font= ("Seymour One", 13, "bold"), command=SavePass)  # отпровляемся к функц SavePass
btn.place(relx=0.25, y=300, anchor= CENTER)


#--------------------------------------------------------------------------------------------------------------------------------------------

allPass = Label(root,
             text = "Найти Пароль",
             font = ("Comic Sans MS", 13, "bold"),
             )
allPass.place(relx = 0.7, y = 110, anchor=CENTER)


ServiceName = Label(root,
             text = "Сервис",
             font = ("Comic Sans MS", 13, "bold"),
             )
ServiceName.place(relx = 0.55, y = 160, anchor=CENTER)



b = Entry(root, font = "Ariel 13") # текстовое поле
b.place(relx= 0.78, y=160, anchor=CENTER)  # координаты текстового поля

#---------------------------------------------------------------------------------------------------------------------------------------

def SearchPass():
    findService = b.get()   # из текстового поля ServiceName
    print(findService)

    with open("AccountPass.json", "r", encoding="UTF-8") as file:  # Читаем пароли из файла
        lines = file.readlines()

    passwords = {}
    for line in lines:
        parts = line.strip().split(";")  # Разделяем строку на части по символу ";"
        if len(parts) == 3:  # Проверяем, что в строке есть три части
            service, password, extra = parts
            passwords[service] = (password, extra)

    if findService in passwords:  # Проверяем, есть ли введенный сервис в словаре паролей
        thePass, extra = passwords[findService]
        PassWord.delete(0, END)  # Очищаем текстовое поле c
        userEmailText.delete(0, END)  # Очищаем текстовое поле userEmailText
        ExtraText.delete(0, END)  # Очищаем текстовое поле ExtraText
        PassWord.insert(0, thePass)  # Выводим пароль в текстовое поле c
        ExtraText.insert(0, extra)  # Выводим дополнительную информацию в текстовое поле ExtraText
        root.clipboard_clear()
        root.clipboard_append(thePass)  # вставить в буфер обмена
    else:
        PassWord.delete(0, END)  # Очищаем текстовое поле c
        userEmailText.delete(0, END)  # Очищаем текстовое поле userEmailText
        ExtraText.delete(0, END)  # Очищаем текстовое поле ExtraText
        PassWord.insert(0, "Сервис Не Найден")  # Выводим сообщение об ошибке
        notification.notify(message="Сервис Не найден", app_icon="logo.ico")

# -----------------------------------------------------------------------------------------------------------------------------------------


userLabel = Label(root,
             text = "Доп",
             font = ("Comic Sans MS", 13, "bold"),
             )
userLabel.place(relx = 0.55, y = 260, anchor=CENTER)

ExtraText = Entry(root, font = "Ariel 13") # текстовое поле
ExtraText.place(relx= 0.78, y=260, anchor=CENTER)  # координаты текстового поля




#--------------------------------------------------------------------------------------------------------------------------------------
passWordLabel = Label(root,
             text = "Пароль",
             font = ("Comic Sans MS", 13, "bold"),
             )
passWordLabel.place(relx = 0.55, y = 300, anchor=CENTER)

PassWord = Entry(root, font = "Ariel 13") # текстовое поле
PassWord.place(relx= 0.78, y=300, anchor=CENTER)  # координаты текстового поля
# -----------------------------------------------------------------------------------------------------------------------------------------
btn1 = Button(root, text="Найти", font= ("Seymour One", 13, "bold"), command=SearchPass) # отпровляемся к функц SavePass
btn1.place(relx=0.7, y=210, anchor= CENTER)

btn2 = Button(root, text="Очистить", font= ("Seymour One", 13, "bold"), command=clearField) # отпровляемся к функц clearField
btn2.place(relx=0.87, y=210, anchor= CENTER)

# -----------------------------------------------------------------------------------------------------------------------------------------
# генератор пароля

def randomize():
    PassL = d.get()  # получаем длину пароля
    allowedPassL = 19
    try:
        PassL = int(PassL)  # преобразуем строку в целое число
        if PassL > allowedPassL:
            d.delete(0, END)
            d.insert(0, "Превышен Лимит")
            notification.notify(message="Превышен лимит на длину пароля", app_icon="logo.ico")
            return  # выходим из функции, чтобы не продолжать генерацию пароля
    except ValueError:  # если не удается преобразовать в целое число
        d.delete(0, END)
        d.insert(0, "Некорректный ввод")
        notification.notify(message="Некорректный ввод длины пароля", app_icon="logo.ico")
        return  # выходим из функции, чтобы не продолжать генерацию пароля

    d.delete(0, END)  # очищаем текстовое поле
    for i in range(int(PassL)):
        d.insert(0, choice(alphabet))  # добавляем символы в текстовое поле


def SavingPass():
    PassPrefix = "Пароль"
    Pass = d.get() # получить пароль из текст поля
    root.clipboard_clear()
    root.clipboard_append(Pass) # вставить в буфер обмена
    print(Pass)
    with open("GenPass.json", "a", encoding="UTF-8") as file: # записываем пароль
        file.write(f"{PassPrefix} --->>> {Pass}\n")
        d.delete(0, END)
        notification.notify(message="Пароль Сохранён В буфер Обмена", app_icon="logo.ico")

alphabet = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "j", "K", "L", "M", "N", "O", "P", "Q", "R", "T", "U", "V", "W", "X", "Y", "Z",
            "!", "@", "$", "&", "*", "#", "?"
            ] # словарь


PassGen = Label(root,
             text = "Генератор Паролей",
             font = ("Comic Sans MS", 17, "bold"),
             )
PassGen.place(relx = 0.47, y = 420, anchor=CENTER)




LengthPass = Label(root,
             text = "Кол.во символов",
             font = ("Comic Sans MS", 13, "bold"),
             )
LengthPass.place(relx = 0.2, y = 490, anchor=CENTER)



d = Entry(root, font = "Ariel 13") # текстовое поле
d.place(relx= 0.5, y=490, anchor=CENTER)  # координаты текстового поля

btn = Button(root, text="Сгенерировать", font= ("Seymour One", 15, "bold"), command=randomize) # отпровляемся к функц randomize
btn.place(relx=0.2, y=570, anchor= CENTER)

btn4 = Button(root, text="Сохранить Пароль", font= ("Seymour One", 15, "bold"), command=SavingPass) # отпровляемся к функц SavePass
btn4.place(relx=0.55, y=570, anchor= CENTER)

btn3 = Button(root, text="Очистить", font= ("Seymour One", 15, "bold"), command=clearField1) # отпровляемся к функц SavePass
btn3.place(relx=0.85, y=570, anchor= CENTER)



# -----------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()   # показываем окно