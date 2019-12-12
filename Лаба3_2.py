from graph import *
import math as m
import antigravity
c = canvas()

def background(h, d):
    penColor('#000000')
    brushColor('#a1f5ff')
    rectangle(0, 0, d, 7 / 15 * h)
    brushColor('#4423df')
    rectangle(0, 7 / 15 * h, d, 10 / 15 * h)
    brushColor('#eef60c')
    rectangle(0, 10 / 15 * h, d, h)
def sin():
     a=[]
     
     for i in range(1000):
        a.append((d*i/1000, 10/15.1 *h + m.fabs(1/15 * h * m.sin(7*m.pi*i/1000))))
     brushColor('#4423df')
     penColor('#4423df')
     polygon(a)
	   
def clouds():
    b_c = 0.7 * 30 #between_clouds
    r_c = 30 #radius of cloud
    brushColor('#ffffff')
    circle(1 / 6 * d, 1 / 6 * h, r_c)
    circle(1 / 6 * d + b_c, 1 / 6 * h + b_c, r_c)
    circle(1 / 6 * d + 2 * b_c, 1 / 6 * h, r_c)
    circle(1 / 6 * d + 3 * b_c, 1 / 6 * h + b_c, r_c)
    circle(1 / 6 * d + 4 * b_c, 1 / 6 * h, r_c)
    circle(1 / 6 * d + 5 * b_c, 1 / 6 * h + b_c, r_c)
    circle(1 / 6 * d + 6 * b_c, 1 / 6 * h, r_c)


def clouds1():
    b_c = 0.7 * 20 #between_clouds
    r_c = 20 #radius of cloud
    brushColor('#ffffff')
    circle(1 / 2 * d, 1 / 6 * h, r_c)
    circle(1 / 2 * d + b_c, 1 / 6 * h + b_c, r_c)
    circle(1 / 2 * d + 2 * b_c, 1 / 6 * h, r_c)
    circle(1 / 2 * d + 3 * b_c, 1 / 6 * h + b_c, r_c)
    circle(1 / 2 * d + 4 * b_c, 1 / 6 * h, r_c)
    circle(1 / 2 * d + 5 * b_c, 1 / 6 * h + b_c, r_c)
    circle(1 / 2 * d + 6 * b_c, 1 / 6 * h, r_c)

def clouds2():
    b_c = 0.7 * 20 #between_clouds
    r_c = 20 #radius of cloud
    brushColor('#ffffff')
    circle(1 / 2 * d, 1 / 3 * h, r_c)
    circle(1 / 2 * d + b_c, 1 / 3 * h + b_c, r_c)
    circle(1 / 2 * d + 2 * b_c, 1 / 3 * h, r_c)
    circle(1 / 2 * d + 3 * b_c, 1 / 3 * h + b_c, r_c)
    circle(1 / 2 * d + 4 * b_c, 1 / 3 * h, r_c)
    circle(1 / 2 * d + 5 * b_c, 1 / 3 * h + b_c, r_c)
    circle(1 / 2 * d + 6 * b_c, 1 / 3 * h, r_c)

def clouds3():
    b_c = 0.7 * 15 #between_clouds
    r_c = 15 #radius of cloud
    brushColor('#ffffff')
    circle(1 / 6 * d, 1 / 3 * h, r_c)
    circle(1 / 6 * d + b_c, 1 / 3 * h + b_c, r_c)
    circle(1 / 6 * d + 2 * b_c, 1 / 3 * h, r_c)
    circle(1 / 6 * d + 3 * b_c, 1 / 3 * h + b_c, r_c)
    circle(1 / 6 * d + 4 * b_c, 1 / 3 * h, r_c)
    circle(1 / 6 * d + 5 * b_c, 1 / 3 * h + b_c, r_c)
    circle(1 / 6 * d + 6 * b_c, 1 / 3 * h, r_c)

def Sun():
    x = 6/7 *d
    y=  1/6 *h
    r_s = 50 # radius of sun
    penColor('#fff71d')
    brushColor('#fff71d')
    a=[]
    n = 80
    for i in range(n):
      x = 600
      y=100
      if i%2 == 0:
            a.append((x+r_s*m.cos(2*m.pi*i/n), y+r_s*m.sin(2*m.pi*i/n)))
      else:
            a.append((x+(r_s+10)*m.cos(2*m.pi*i/n), y+(r_s+10)*m.sin(2*m.pi*i/n)))
    brushColor(255, 247, 0) 
    polygon(a)
    


def umbrella():
    penColor('#e38219')
    brushColor('#e38219')
    rectangle(1 / 5 * d, 8.5 / 15 * h, 1 / 5 * d + 0.01 * d, 14 / 15 * h)
    l = d / 10
    penColor('#f45151')
    brushColor('#f45151')
    polygon([(1 / 5 * d, 8.5 / 15 * h), (1 / 5 * d - l, 9.5 / 15 * h), (1 / 5 * d, 9.5 / 15 * h), (1 / 5 * d, 8.5 / 15 * h)])
    rectangle(1 / 5 * d, 8.5 / 15 * h, 1 / 5 * d + 0.01 * d, 9.5 / 15 * h)
    polygon([(1 / 5 * d + 0.01 * d, 8.5 / 15 * h), (1 / 5 * d + 0.01 * d + l, 9.5 / 15 * h), (1 / 5 * d + 0.01 * d, 9.5 / 15 * h), (1 / 5 * d + 0.01 * d, 8.5 / 15 * h)])
    penColor('#000000')
    line(1 / 5 * d, 8.5 / 15 * h, 1 / 5 * d - ( 2 / 4 *l), 9.5 / 15 * h)
    line(1 / 5 * d, 8.5 / 15 * h, 1 / 5 * d - ( 1 / 4 *l), 9.5 / 15 * h)
    line(1 / 5 * d, 8.5 / 15 * h, 1 / 5 * d - ( 3 / 4 *l), 9.5 / 15 * h)
    line(1 / 5 * d + 0.01 * d, 8.5 / 15 * h, 1 / 5 * d + 0.01 * d + ( 1 / 4 *l), 9.5 / 15 * h)
    line(1 / 5 * d + 0.01 * d, 8.5 / 15 * h, 1 / 5 * d + 0.01 * d + ( 2 / 4 *l), 9.5 / 15 * h)
    line(1 / 5 * d + 0.01 * d, 8.5 / 15 * h, 1 / 5 * d + 0.01 * d + ( 3 / 4 *l), 9.5 / 15 * h)

def umbrella1():
    penColor('#e38219')
    brushColor('#e38219')
    rectangle(1 / 2 * d, 8.5 / 15 * h, 1 / 2 * d + 0.01 * d, 12 / 15 * h)
    l = d / 30
    penColor('#f45151')
    brushColor('#f45151')
    polygon([(1 / 2 * d, 8.5 / 15 * h), (1 / 2 * d - l, 9.5 / 15 * h), (1 / 2 * d, 9.5 / 15 * h), (1 / 2 * d, 8.5 / 15 * h)])
    rectangle(1 / 2 * d, 8.5 / 15 * h, 1 / 2* d + 0.01 * d, 9.5 / 15 * h)
    polygon([(1 / 2* d + 0.01 * d, 8.5 / 15 * h), (1 / 2 * d + 0.01 * d + l, 9.5 / 15 * h), (1 / 2 * d + 0.01 * d, 9.5 / 15 * h), (1 / 2 * d + 0.01 * d, 8.5 / 15 * h)])
    penColor('#000000')
    line(1 / 2 * d, 8.5 / 15 * h, 1 / 2 * d - ( 2 / 4 *l), 9.5 / 15 * h)
    line(1 / 2 * d, 8.5 / 15 * h, 1 / 2 * d - ( 1 / 4 *l), 9.5 / 15 * h)
    line(1 / 2 * d, 8.5 / 15 * h, 1 / 2 * d - ( 3 / 4 *l), 9.5 / 15 * h)
    line(1 / 2 * d + 0.01 * d, 8.5 / 15 * h, 1 / 2 * d + 0.01 * d + ( 1 / 4 *l), 9.5 / 15 * h)
    line(1 / 2 * d + 0.01 * d, 8.5 / 15 * h, 1 / 2 * d + 0.01 * d + ( 2 / 4 *l), 9.5 / 15 * h)
    line(1 / 2 * d + 0.01 * d, 8.5 / 15 * h, 1 / 2 * d + 0.01 * d + ( 3 / 4 *l), 9.5 / 15 * h)

def ship():
    d_s = h / 15
    dl = d - 100
    c.create_arc(dl * 0.6, h / 2 - d_s, dl * 0.6 + 2 * d_s, h / 2 + d_s, start = 180, extent = 90, fill = '#ba5005')
    penColor('#000000')
    brushColor('#ba5005')
    rectangle(dl * 0.6 + d_s, h / 2, dl * 0.6 + 5 * d_s, h / 2 + d_s)
    polygon([(dl * 0.6 + 5 * d_s, h / 2 + d_s), (dl * 0.6 + 7 * d_s, h / 2), (dl * 0.6 + 5 * d_s, h / 2), (dl * 0.6 + 5 * d_s, h / 2 + d_s)])
    brushColor('#000000')
    rectangle(dl * 0.6 + 2.5 * d_s, h / 2, dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2 - (h / 5))
    brushColor('#ded599')
    polygon([(dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2 - (h / 5)), (dl * 0.6 + 3.5 * d_s, h / 2 - 0.1 * h), (dl * 0.6 + 5 * d_s, h / 2 - 0.1 * h), (dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2 - (h / 5))])
    polygon([(dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2), (dl * 0.6 + 3.5 * d_s, h / 2 - 0.1 * h), (dl * 0.6 + 5 * d_s, h / 2 - 0.1 * h), (dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2)])
    brushColor('#000000')
    circle(dl * 0.6 + 5.4 * d_s, h / 2 + 0.4 * d_s, 10)
    brushColor('#ffffff')
    circle(dl * 0.6 + 5.4 * d_s, h / 2 + 0.4 * d_s, 8)

def ship1():
    d_s = h / 25
    dl = d - 600
    c.create_arc(dl * 0.6, h / 2 - d_s, dl * 0.6 + 2 * d_s, h / 2 + d_s, start = 180, extent = 90, fill = '#ba5005')
    penColor('#000000')
    brushColor('#ba5005')
    rectangle(dl * 0.6 + d_s, h / 2, dl * 0.6 + 5 * d_s, h / 2 + d_s)
    polygon([(dl * 0.6 + 5 * d_s, h / 2 + d_s), (dl * 0.6 + 7 * d_s, h / 2), (dl * 0.6 + 5 * d_s, h / 2), (dl * 0.6 + 5 * d_s, h / 2 + d_s)])
    brushColor('#000000')
    rectangle(dl * 0.6 + 2.5 * d_s, h / 2, dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2 - (h / 5))
    brushColor('#ded599')
    polygon([(dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2 - (h / 5)), (dl * 0.6 + 3.5 * d_s, h / 2 - 0.1 * h), (dl * 0.6 + 5 * d_s, h / 2 - 0.1 * h), (dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2 - (h / 5))])
    polygon([(dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2), (dl * 0.6 + 3.5 * d_s, h / 2 - 0.1 * h), (dl * 0.6 + 5 * d_s, h / 2 - 0.1 * h), (dl * 0.6 + 2.5 * d_s + 0.01 * d, h / 2)])
    brushColor('#000000')
    circle(dl * 0.6 + 5.4 * d_s, h / 2 + 0.4 * d_s, 10)
    brushColor('#ffffff')
    circle(dl * 0.6 + 5.4 * d_s, h / 2 + 0.4 * d_s, 8)
        
d = 700
h = 600
windowSize(d, h)
canvasSize(d, h)
background(h, d)
sin()
clouds()
clouds1()
clouds2()
clouds3()
Sun()

ship()
ship1()
umbrella()
umbrella1()
run()
