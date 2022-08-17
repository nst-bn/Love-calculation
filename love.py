from cProfile import label
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from random import randint

win = Tk()
win.iconbitmap('heart.ico')
win.title('Любовный калькулятор')

def calculation():
    number = randint(60, 100)
    showinfo('Процент любви', f'Это любовь на {number} %')

open_img = Image.open('Love_main.png')
render_img = ImageTk.PhotoImage(open_img)
main_image = Label(win, image=render_img)
main_image.image = render_img
main_image.grid(row=0, columnspan=2)

label1 = Label(win, text='Введите ваше имя: ', font=('arial', 10, 'bold'))
label1.grid(row=1, column=0, sticky="W")

entry1 = Entry(win, font=('arial', 10, 'bold'))
entry1.grid(row=1, column=1)

label1 = Label(win, text='Введите имя вашего партнёра: ', font=('arial', 10, 'bold'))
label1.grid(row=2, column=0, sticky="W")

entry2 = Entry(win, font=('arial', 10, 'bold'))
entry2.grid(row=2, column=1)

button = Button(win, text='Проверить!', font=('arial', 12, 'bold'), fg='pink', bg='black', command=calculation)

button.grid(row=3, columnspan=2)

win.mainloop()