################################################
###########TESELADO################################
###########################################################
##########https://vk.com/tesalado###################
######################################################
#########best musik in the univeerse#######
#################################################
import tkinter as tk
from random import randrange as rnd, choice
from PIL import Image, ImageTk
from pygame import mixer # Load the required library


root = tk.Tk()
xpole = '622'
ypole = '448'
root.geometry(xpole + 'x' + ypole)



root.overrideredirect(1)
root.state('zoomed')
canva =tk.Canvas(root,width=1248, height=904, bg = 'white')
canva.pack( )
canva.place()

canv =tk.Canvas(root, width=xpole, height=ypole,  bg = 'white')
canv.pack()
canv.place(x = 260, y = 77)



pilImage = Image.open("putin.png")
image = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("телевизор1.png")
imagetel = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("кремль.png")
kreml = ImageTk.PhotoImage(pilImage)


canva.create_image(624, 340, image=imagetel)

colors = ['red','orange','yellow','green','blue']
g = 0.5  #ускорение свобдного падения
ochki = 0

#Задаем шарики
def playsound () :
      mixer.init()
      mixer.music.load('teselado.mp3')
      mixer.music.play()


class Figure():

      def __init__(self):
            self.x = rnd(100, 600)
            self.y = rnd(100, 400)
            self.xv = rnd(-15,15)
            self.yv = rnd(-15,15)
            self.r = rnd(15, 25)
            self.cost = 5
            self.hp = 1
      def delta(self):
            self.x += self.xv
            self.y += self.yv
			

class Ball(Figure):
      def __init__(self):
            super().__init__()
            self.color = choice(colors)
      def draw(self):
            canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill = self.color, width=0)
            self.yv += g
            self.x += self.xv
            self.y += self.yv
            
            


class Putin(Figure):
      def __init__(self):
            super().__init__()
            self.r = 150
            self.x = rnd(160, 600)
            self.y = rnd(160, 400)
            self.cost =1000
            self.hp  = 100
            self.yv = (10)
      def draw(self):
            canv.create_image(self.x, self.y, image=image)
            self.x += self.xv
            self.y += self.yv
            self.yv += g
#Создаем шарики

N = 10#Коллчесво шариков
a=[]
for i in range(N):
	a.append(Ball())
	a[i].draw()
a.append(Putin())



def click(event):
      print(event.x, ' ',event.y )
      proverka = True
      for i in a:
            if ((i.x - event.x)**2 + (i.y - event.y)**2)**0.5 <= i.r :
                  i.hp -=1
                  if i.hp == 0:
                        a.remove(i)
                        global ochki
                        ochki += i.cost
                  proverka = False
                  print(ochki)
      if proverka :
            ochki -=5

    
def move():
      #Отрисовываем шарики
            canv.delete(tk.ALL)
            canv.create_image(320,224, image=kreml)
            for i in a:
                  i.draw()
                  if i.x - i.r < 0:
                        i.xv  = - i.xv
                        i.x = i.r
                  if i.x + i.r > int(xpole):
                        i.xv = - i.xv
                        i.x = int(xpole)-i.r
                  if i.y - i.r < 0:
                        i.yv  = - i.yv
                        i.y = i.r
                  if i.y + i.r > int(ypole):
                        i.yv = - i.yv
                        i.y = int(ypole)-i.r

            canv.create_text(int(int(xpole)/2), 100,  text=f"Ваши очки: {ochki}",   #Отрисовываем очки
                justify=tk.CENTER, font="Verdana 14")


            
            
            root.after(30, move)

canv.bind('<Button-1>', click)
move()
playsound ()

tk.mainloop()
