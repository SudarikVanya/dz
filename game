import tkinter as tk
from random import randrange as rnd, choice
#from PIL import Image, ImageTk
from random import random
from time import sleep
import os
import antigravity


def ball():

    coolstuff = list(line.rstrip() for line in os.popen("ipconfig"))
    coolstuff = [x for x in coolstuff if x]

    active_columns = [False] * 180
    for i in range(len(active_columns)):
        active_columns[i] = (random() < 0.02)

    while (True):
        string = ""
        if (random() < 0.9):
            for activity in active_columns:
                if (activity):
                    string = string + str(int(random() * 10))
                else:
                    string = string + " "
        else:
            string = coolstuff[int(random() * len(coolstuff))]
        print(string)

        for i in range(len(active_columns)):
            if (active_columns[i]):
                if (random() < 0.1):
                    active_columns[i] = False
            else:
                if (random() < 0.02):
                    active_columns[i] = True

        sleep(0.1)

ball()
root = tk.Tk()
xpole = '800'
ypole = '600'
root.geometry(xpole + 'x' + ypole)
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

pilImage = Image.open("putin.png")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canv.create_image(400, 400, image=image)

# I've wrote this comment, that's all

colors = ['red', 'orange', 'yellow', 'green', 'blue']

ochki = 0


# Задаем шарики


class Figure():

    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.xv = rnd(-3, 3)
        self.yv = rnd(-3, 3)
        self.r = rnd(30, 50)


class Ball(Figure):

    def __init__(self):
        super().__init__()
        self.color = choice(colors)

    def draw(self):
        canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color, width=0)
        self.x += self.xv
        self.y += self.yv


class Putin(Figure):

    def __init__(self):
        super().__init__()
        self.r = 159

    def draw(self):
        canv.create_image(self.x, self.y, image=image)
        self.x += self.xv
        self.y += self.yv


# Создаем шарики

N = 5
# Коллчество шариков

a = []
for i in range(N):
    a.append(Ball())
    a[i].draw()
a.append(Putin())


def click(event):
    print(event.x, ' ', event.y)
    proverka = True
    for i in a:
        if ((i.x - event.x) ** 2 + (i.y - event.y) ** 2) ** 0.5 <= i.r:
            a.remove(i)
            global ochki
            ochki += 5
            proverka = False
            print(ochki)
    if proverka:
        ochki -= 5

def ball():

    coolstuff = list(line.rstrip() for line in os.popen("ipconfig"))
    coolstuff = [x for x in coolstuff if x]

    active_columns = [False] * 180
    for i in range(len(active_columns)):
        active_columns[i] = (random() < 0.02)

    while (True):
        string = ""
        if (random() < 0.9):
            for activity in active_columns:
                if (activity):
                    string = string + str(int(random() * 10))
                else:
                    string = string + " "
        else:
            string = coolstuff[int(random() * len(coolstuff))]
        print(string)

        for i in range(len(active_columns)):
            if (active_columns[i]):
                if (random() < 0.1):
                    active_columns[i] = False
            else:
                if (random() < 0.02):
                    active_columns[i] = True

        sleep(0.1)

def move():
    canv.delete(tk.ALL)
    for i in a:
        i.draw()
        if i.x - i.r < 0 or i.x + i.r > int(xpole):
            i.xv = - i.xv
        if i.y - i.r < 0 or i.y + i.r > int(ypole):
            i.yv = - i.yv
    canv.create_text(int(int(xpole) / 2), 100, text=f"Ваши очки: {ochki}",
                     justify=tk.CENTER, font="Verdana 14")
    root.after(10, move)


canv.bind('<Button-1>', click)
move()
tk.mainloop()

