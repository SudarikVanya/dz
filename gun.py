from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class relief():
    def __init__(self):
        self.cord = []
        for i in range(150):
            self.cord.append( + i*10 )
            self.cord.append( 600 - (50 - ((i-50)**2)/50))
        self.id = canv.create_polygon(self.cord, outline='red', 
                                                      fill='green', width=2)
        
        print(self.cord)
    def draw(self, vx):
        if vx !=0:
            for i in range(300):
                if i%2 ==0:
                    self.cord[i] -= vx

            canv.coords(self.id, self.cord)
        

class points():
    def __init__(self):
        self.points = 0
        self.item = canv.create_text(30,30,text = self.points,font = '28')
    def draw(self):
        canv.itemconfig(self.item, text = self.points)


class ball():
    def __init__(self, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.gy = 1
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30
        self.time = time.time()

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self, vxgun):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += (self.vx - vxgun)
        self.y -= self.vy
        self.set_coords()
##        if self.x - self.r < 0:          скрипт блокирует движение шариков за пределы карты
##            self.vx = -0.75*self.vx
##            self.vy =  0.75*self.vy
##            self.x  = self.r
##        if self.x + self.r  > 800:
##            self.vx = -0.75*self.vx
##            self.vy =  0.75*self.vy
##            self.x  = 800 - self.r
 
        if self.y  > 600 - self.r:
            self.vy = -0.75*self.vy
            self.vx =  0.75*self.vx
            self.y  = 600 - self.r
        if self.y !=0:
            self.vy -= self.gy
    def hittest(self, obj):
        if (((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5) < self.r + obj.r:
            print(True)
            return True
        else:
            
            return False

    def delete(self, balls):
        canv.delete(self.id)
        balls.remove(self)
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """


class gun():
    def __init__(self):
        self.x = 400
        self.y = 450
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(self.x, self.y, self.x+30,self.y - 30,width=7) # FIXME: don't know how to set it...
        self.body = canv.create_polygon((self.x-30, self.y), (self.x+30, self.y), (self.x+30, self.y+30), (self.x-30, self.y+30) ,)
        self.koleso1 = canv.create_oval(self.x + 15 ,self.y + 30,self.x + 30,self.y + 45)
        self.koleso2  = canv.create_oval(self.x - 15 ,self.y + 30,self.x - 30,self.y + 45)
        self.bullet = 0
        self.balls = []
        self.vx = 0
        self.vy = 0
        self.gy = 1
        self.alfa = 0
        self.delta_alfa = 0*math.pi/36

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.bullet += 1
        new_ball = ball(self.x, self.y)
        new_ball.r += 5
        try:
            new_ball.vx = self.f2_power * (event.x-self.x)/((event.x-self.x)**2 + (event.y-self.y)**2)**0.5
            new_ball.vy = - self.f2_power * (event.y-self.y)/((event.x-self.x)**2 + (event.y-self.y)**2)**0.5
        except:
            pass
        self.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
    def setbody(self):
        canv.coords(self.body, self.x + (-30) *math.cos(self.alfa) + 0*math.sin(self.alfa), self.y+ 0*math.cos(self.alfa) - (-30)*math.sin(self.alfa),
                                            self.x+(30) *math.cos(self.alfa) + 0*math.sin(self.alfa), self.y + 0*math.cos(self.alfa) - (30)*math.sin(self.alfa),
                                            self.x+(30) *math.cos(self.alfa) + 30*math.sin(self.alfa), self.y+30*math.cos(self.alfa) - (30)*math.sin(self.alfa),
                                            self.x+(-30) *math.cos(self.alfa) + 30*math.sin(self.alfa), self.y+30*math.cos(self.alfa) - (-30)*math.sin(self.alfa))
    def setkoleso1(self):
        canv.coords(self.koleso1, self.x + (22) *math.cos(self.alfa) + 38*math.sin(self.alfa) - 8,
                                                self.y + 38*math.cos(self.alfa) - (22)*math.sin(self.alfa) - 8,
                                                self.x + (22) *math.cos(self.alfa) + 38*math.sin(self.alfa) + 8,
                                                self.y + 38*math.cos(self.alfa) - (22)*math.sin(self.alfa) + 8,
                                                )
    def setkoleso2(self):
        canv.coords(self.koleso2,  self.x + (-22) *math.cos(self.alfa) + 38*math.sin(self.alfa) - 8,
                                                self.y + 38*math.cos(self.alfa) - (-22)*math.sin(self.alfa) - 8,
                                                self.x + (-22) *math.cos(self.alfa) + 38*math.sin(self.alfa) + 8,
                                                self.y + 38*math.cos(self.alfa) - (-22)*math.sin(self.alfa) + 8,
                                                )   
    def setcord(self, event):
        #print(type(event))
        #print(event.x)
        try:
            canv.coords(self.id, self.x, self.y,
                        self.x + max(self.f2_power, 20) *  (event.x-self.x)/((event.x-self.x)**2 + (event.y-self.y)**2)**0.5,
                        self.y + max(self.f2_power, 20) *  (event.y-self.y)/((event.x-self.x)**2 + (event.y-self.y)**2)**0.5
                        )
        except:
            pass
    def targetting(self , event  =0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = event
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        self.setcord(self.an)

        
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
            
    def movex(self, event):
        self.vx += 1
        

        #self.setcord(event)
        #self.setbody()
        #self.setkoleso1()
        #self.setkoleso2()
    def movexm(self, event):
        self.vx -= 1
##        self.setcord(event)
##        self.setbody()
##        self.setkoleso1()
##        self.setkoleso2()
    def movey(self, event):
        self.y += 4
##        self.setcord(event)
##        self.setbody()
##        self.setkoleso1()
##        self.setkoleso2()
    def moveym(self, event):
        self.y -= 10
##        self.setcord(event)
##        self.setbody()
##        self.setkoleso1()
##        self.setkoleso2()

    def move(self, relief):
        
        #self.x += self.vx
        self.y -= self.vy
        self.setcord(self.an)
        self.setbody()
        self.setkoleso1()
        self.setkoleso2()
        self.alfa +=self.delta_alfa
##        try:
##            
##            print(relief[relief.index(self.x)]) #походу нужно самому прописывать эту ебаную функцию( (по поиску self.x в массиве с дробными значениями
##        except:
##            pass
        value  = self.search_x_in_relief(relief)
        #print(value)
        if self.y  > value - 45:
            self.vy = -0.75*self.vy
            self.vx =  0.9*self.vx
            self.y  = value - 45
            
        if self.y !=0:
              self.vy -= self.gy
        
    def search_x_in_relief(self, relief):

            for i, a in enumerate(relief):
                if i%2 == 0:
                    if a<self.x+5 and a>self.x-5:
                        self.alfa = -math.atan((relief[i+1] - relief[i-1])/5)
                        print(self.alfa)
                        return relief[i+1]
                    
            self.alfa = 0
            return 600
        

class target():
    def __init__(self):
        self.live = 1

        self.id = canv.create_oval(0,0,0,0)

        self.new_target()


    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        points.points += 1
    def move(self, vx):
        self.x -= vx
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)


def new_game(event=''):
    g1 = gun()
    screen1 = canv.create_text(400, 300, text='', font='28')
    t1 = target()
    t1.new_target()
    r1 = relief()
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    root.bind('<KeyPress-d>', g1.movex)
    root.bind('<KeyPress-s>', g1.movey)
    root.bind('<KeyPress-w>', g1.moveym)
    root.bind('<KeyPress-a>', g1.movexm)
    proverka = False
    z = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in g1.balls:
            b.move(g1.vx)
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(g1.bullet) + ' выстрелов')
                points.draw()
                proverka = True
            if (time.time() - b.time) > 5:
                b.delete(g1.balls)
        g1.move(r1.cord)
        t1.move(g1.vx)
        r1.draw(g1.vx)
        canv.update()
        time.sleep(0.03)
        
        g1.targetting()
        g1.power_up()
        if proverka:
                break

    for i in g1.balls:
        canv.delete(i.id)
    canv.itemconfig(screen1, text='')
    time.sleep(0.5)
    canv.delete(g1.id)
    canv.delete(t1.id)
    canv.delete(g1.koleso1, g1.koleso2, g1.body, r1.id) 
    
    root.after(750, new_game)

points = points()

new_game()

root.mainloop()
