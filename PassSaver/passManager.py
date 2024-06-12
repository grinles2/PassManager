from tkinter import *
from tkinter import messagebox as mb
from random import choice
import os
from plyer import notification
from cryptography.fernet import Fernet
import json

# Ключ шифрования
EncryptKey = "b9a5VmpGWxb8r_H-PM9dV8NjCMpPhlYgV6F8KJ9Zraw="

# Функции для работы с шифрованием
def encrypt(data, key):
    f = Fernet(key)
    json_data = json.dumps(data).encode('utf-8')
    encrypted_data = f.encrypt(json_data)
    return encrypted_data

def decrypt(encrypted_data, key):
    f = Fernet(key)
    json_data = f.decrypt(encrypted_data)
    data = json.loads(json_data.decode('utf-8'))
    return data

# Функции SavePass и SearchPass
def SavePass():
    NameOfService = ServiceEntry.get()
    thePass = PassEntry.get()
    userEmailGet = userEmailText.get()

    data = {
        "service": NameOfService,
        "password": thePass,
        "email": userEmailGet
    }

    encrypted_data = encrypt(data, EncryptKey.encode())

    with open("AccPass.json", "ab") as file:
        file.write(encrypted_data + b'\n')
        notification.notify(message="Пароль сохранён", app_icon="logo.ico")
        ServiceEntry.delete(0, END)
        PassEntry.delete(0, END)
        userEmailText.delete(0, END)

def clearFile():
    try:
        answer = mb.askyesno(title="Вопрос", message="Вы уверены? Аккаунты будут удалены навсегда")
        if answer:
            os.remove("AccPass.json")
    except FileNotFoundError:
        print("Файл Не найден")
        notification.notify(message="Файл Утерян/Повреждён/Пароль не был сохранён прежде", app_icon="logo.ico")

def clearPass():
    try:
        answer = mb.askyesno(title="Вопрос", message="Вы уверены? Пароли будут удалены навсегда")
        if answer:
            os.remove("GenPass.json")
    except FileNotFoundError:
        print("Файл Не найден")
        notification.notify(message="Файл Утерян/Повреждён/Пароль не был сохранён прежде", app_icon="logo.ico")

def deleteLast():
    try:
        answer1 = mb.askyesno(title="Вопрос", message="Вы уверены?")
        if answer1:
            with open('AccPass.json', 'r') as f:
                lines = f.readlines()
                lines = lines[:-1]
            with open('AccPass.json', 'w') as f:
                f.writelines(lines)
    except FileNotFoundError:
        print("Файл Не найден")
        notification.notify(message="Файл Утерян/Повреждён/Пароль не был сохранён прежде", app_icon="logo.ico")

def BlackBG():
    root.config(bg="grey")

def CyanBG():
    root.config(bg="cyan")

def RedBG():
    root.config(bg="red")

def YellowBG():
    root.config(bg="yellow")

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

root = Tk()
mainmenu = Menu(root)

# Функции для страниц
def clearField():
    PassWord.delete(0, END)
    ExtraText.delete(0, END)
    SecondServiceEntry.delete(0, END)

def clearField1():
    passwordEntry.delete(0, END)


def secondPage():
    page_root = Tk()
    page_root.title("Все Сервисы")
    page_root.geometry("600x600")
    page_root.config(bg="cyan")
    page_root.iconbitmap('logo.ico')  # лого
    page_root.resizable(width=False, height=False)  # запрет на расширение

    # Лейблы
    Title = Label(page_root,
                  text="Менеджер Паролей",
                  font=("Comic Sans MS", 17, "bold"),
                  )
    Title.place(relx=0.5, y=40, anchor=CENTER)

    Title1 = Label(page_root,
                   text="Список Сервисов",
                   font=("Comic Sans MS", 17, "bold"),
                   )
    Title1.place(relx=0.5, y=80, anchor=CENTER)

    # Текстовые Поля
    Output = Entry(page_root, font="Ariel 13")  # текстовое поле
    Output.place(relx=0.5, y=160, anchor=CENTER)  # координаты текстового поля

    # Функции
    def OutputAllServices():
        try:
            with open("AccPass.json", "rb") as file:
                lines = file.readlines()

            services = []
            for line in lines:
                encrypted_data = line.strip()
                data = decrypt(encrypted_data, EncryptKey.encode())
                services.append(data['service'])

            output_text = " --->>> ".join(services)
            Output.delete(0, END)  # Очищаем текстовое поле
            Output.insert(END, output_text)  # Выводим имена сервисов в текстовое поле
        except FileNotFoundError:
            Output.delete(0, END)
            Output.insert(0, "Файл Утерян или не найден")
            notification.notify(message="Файл Утерян/Повреждён/Пароль не был сохранён прежде", app_icon="logo.ico")

    # Кнопки
    OutputButton = Button(page_root, text="Вывести", font=("Seymour One", 17, "bold"), command=OutputAllServices)
    OutputButton.place(relx=0.5, y=300, anchor=CENTER)

    # Main loop
    page_root.mainloop()

# Меню
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Очистить Все Аккаунты", command=clearFile)
filemenu.add_command(label="Удалить Последний Аккаунт", command=deleteLast)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Серый фон", command=BlackBG)
helpmenu.add_command(label="Бирюзовый Фон", command=CyanBG)
helpmenu.add_command(label="Жёлтый фон", command=YellowBG)
helpmenu.add_command(label="Красный фон", command=RedBG)

passwordList = Menu(mainmenu, tearoff=0)
passwordList.add_command(label="Очистить КЭШ Пароли", command=clearPass)

window = Menu(mainmenu, tearoff=0)
window.add_command(label="Прочитать", command=readEula)

pagemenu = Menu(mainmenu, tearoff=0)
pagemenu.add_command(label="Список всех сервисов", command=secondPage)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Менеджер Паролей", menu=filemenu)
mainmenu.add_cascade(label="Генератор Паролей", menu=passwordList)
mainmenu.add_cascade(label="Фон", menu=helpmenu)
mainmenu.add_cascade(label="Дополнительно", menu=pagemenu)

root.title("Менеджер Паролей")
root.geometry("600x600")
root.config(bg="cyan")
root.iconbitmap('logo.ico')  # лого
root.resizable(width=False, height=False)  # запрет на расширение

# Основной интерфейс
Title = Label(root,
              text="Менеджер Паролей",
              font=("Comic Sans MS", 17, "bold"),
              )
Title.place(relx=0.5, y=40, anchor=CENTER)

service = Label(root,
                text="Сохранить Пароль",
                font=("Comic Sans MS", 13, "bold"),
                )
service.place(relx=0.3, y=110, anchor=CENTER)

serviceName = Label(root,
                    text="Сервис",
                    font=("Comic Sans MS", 13, "bold"),
                    )
serviceName.place(relx=0.07, y=160, anchor=CENTER)

ServiceEntry = Entry(root, font="Ariel 13")  # текстовое поле
ServiceEntry.place(relx=0.3, y=160, anchor=CENTER)  # координаты текстового поля

password = Label(root,
                 text="Пароль",
                 font=("Comic Sans MS", 13, "bold"),
                 )
password.place(relx=0.07, y=260, anchor=CENTER)

PassEntry = Entry(root, font="Ariel 13")  # текстовое поле
PassEntry.place(relx=0.3, y=260, anchor=CENTER)  # координаты текстового поля

userEmail = Label(root,
                  text="Доп",
                  font=("Comic Sans MS", 13, "bold"),
                  )
userEmail.place(relx=0.07, y=210, anchor=CENTER)

userEmailText = Entry(root, font="Ariel 13")  # текстовое поле
userEmailText.place(relx=0.3, y=210, anchor=CENTER)  # координаты текстового поля

ButtonSave = Button(root, text="Сохранить", font=("Seymour One", 13, "bold"), command=SavePass)
ButtonSave.place(relx=0.25, y=300, anchor=CENTER)

# Поиск паролей
allPass = Label(root,
                text="Найти Пароль",
                font=("Comic Sans MS", 13, "bold"),
                )
allPass.place(relx=0.7, y=110, anchor=CENTER)

ServiceName = Label(root,
                    text="Сервис",
                    font=("Comic Sans MS", 13, "bold"),
                    )
ServiceName.place(relx=0.55, y=160, anchor=CENTER)

SecondServiceEntry = Entry(root, font="Ariel 13")  # текстовое поле
SecondServiceEntry.place(relx=0.78, y=160, anchor=CENTER)  # координаты текстового поля

def SearchPass():
    try:
        findService = SecondServiceEntry.get()

        found = False
        with open("AccPass.json", "rb") as file:
            lines = file.readlines()

        for line in lines:
            encrypted_data = line.strip()
            data = decrypt(encrypted_data, EncryptKey)

            if data['service'] == findService:
                found = True
                thePass = data['password']
                extra = data['email']

                PassWord.delete(0, END)
                ExtraText.delete(0, END)

                PassWord.insert(0, thePass)
                ExtraText.insert(0, extra)
                root.clipboard_clear()
                root.clipboard_append(thePass)
                break

        if not found:
            PassWord.delete(0, END)
            userEmailText.delete(0, END)
            ExtraText.delete(0, END)
            PassWord.insert(0, "Сервис Не Найден")
            notification.notify(message="Сервис Не найден", app_icon="logo.ico")
    except FileNotFoundError:
        PassWord.delete(0, END)
        userEmailText.delete(0, END)
        ExtraText.delete(0, END)
        PassWord.insert(0, "Файл Утерян")
        notification.notify(message="Файл Утерян/Повреждён/Пароль не был сохранён прежде", app_icon="logo.ico")



userLabel = Label(root,
                  text="Доп",
                  font=("Comic Sans MS", 13, "bold"),
                  )
userLabel.place(relx=0.55, y=260, anchor=CENTER)

ExtraText = Entry(root, font="Ariel 13")  # текстовое поле
ExtraText.place(relx=0.78, y=260, anchor=CENTER)  # координаты текстового поля

passWordLabel = Label(root,
                      text="Пароль",
                      font=("Comic Sans MS", 13, "bold"),
                      )
passWordLabel.place(relx=0.55, y=300, anchor=CENTER)

PassWord = Entry(root, font="Ariel 13")  # текстовое поле
PassWord.place(relx=0.78, y=300, anchor=CENTER)  # координаты текстового поля

ButFind = Button(root, text="Найти", font=("Seymour One", 13, "bold"), command=SearchPass)
ButFind.place(relx=0.7, y=210, anchor=CENTER)

ButClear = Button(root, text="Очистить", font=("Seymour One", 13, "bold"), command=clearField)
ButClear.place(relx=0.87, y=210, anchor=CENTER)



alphabet = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "j", "K", "L", "M", "N", "O", "P", "Q", "R", "T", "U", "V", "W", "X", "Y", "Z",
            "!", "@", "$", "&", "*", "#", "?"
            ] # словарь

# Генератор паролей
def randomize():
    PassL = passwordEntry.get()  # получаем длину пароля
    MaxLength = 19
    MinLength = 6

    try:
        PassL = int(PassL)  # преобразуем строку в целое число
        if PassL > MaxLength:
            passwordEntry.delete(0, END)
            passwordEntry.insert(0, "Превышен Лимит")
            notification.notify(message="Превышен лимит на длину пароля", app_icon="logo.ico")
            return  # выходим из функции, чтобы не продолжать генерацию пароля
        if PassL < MinLength:
            passwordEntry.delete(0, END)
            passwordEntry.insert(0, "Недостаточная Длина Пароля")
            notification.notify(message="Недостаточная Длина Пароля", app_icon="logo.ico")
            return  # выходим из функции, чтобы не продолжать генерацию пароля
    except ValueError:  # если не удается преобразовать в целое число
        passwordEntry.delete(0, END)
        passwordEntry.insert(0, "Некорректный ввод")
        notification.notify(message="Некорректный ввод длины пароля", app_icon="logo.ico")
        return  # выходим из функции, чтобы не продолжать генерацию пароля

    passwordEntry.delete(0, END)  # очищаем текстовое поле
    for i in range(int(PassL)):
        passwordEntry.insert(0, choice(alphabet))  # добавляем символы в текстовое поле

RandomizePass = Label(root,
                      text="Генератор Паролей",
                      font=("Comic Sans MS", 17, "bold"),
                      )
RandomizePass.place(relx=0.5, y=380, anchor=CENTER)

lengthPass = Label(root,
                   text="Длина Пароля",
                   font=("Comic Sans MS", 13, "bold"),
                   )
lengthPass.place(relx=0.22, y=430, anchor=CENTER)

passwordEntry = Entry(root, font="Ariel 13")
passwordEntry.place(relx=0.55, y=430, anchor=CENTER)

PassWord1 = Label(root,
                 text="Пароль",
                 font=("Comic Sans MS", 13, "bold"),
                 )
PassWord1.place(relx=0.3, y=480, anchor=CENTER)

PassRandom = Entry(root, font="Ariel 13")
PassRandom.place(relx=0.55, y=480, anchor=CENTER)

ButtonRandomize = Button(root, text="Генерировать", font=("Seymour One", 13, "bold"), command=randomize)
ButtonRandomize.place(relx=0.5, y=520, anchor=CENTER)

root.mainloop()