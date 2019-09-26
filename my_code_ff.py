from graph import *
import math as m

def house_and_tree (a, x, y):
    brushColor(111,64,10)
    rectangle(50*a+x, 175*a+y, 175*a+x, 257*a+y) #house
    
    brushColor(243,67,14)
    polygon([(50*a+x,175*a+y), (112*a+x,115*a+y), (175*a+x,175*a+y), (50*a+x,175*a+y)]) #roof
    
    penColor(243,121,14)
    brushColor(19, 152, 201)
    rectangle(94*a+x,201*a+y, 133*a+x, 235*a+y) #window
    
    penColor(0,0,0)
    brushColor(53, 25, 6)
    rectangle(215*a+x, 170*a+y, 228*a+x, 250*a+y) #tree
    brushColor(12, 80, 12)
    
    #then are leaves
    
    circle(221.5*a+x, 130*a+y, 20*a)
    circle(245*a+x, 150*a+y, 20*a)
    circle(200*a+x, 150*a+y, 20*a)    
    circle(221.5*a+x, 167*a+y, 20*a)
    circle(242*a+x, 180*a+y, 20*a)
    circle(200*a+x, 180*a+y, 20*a)

def cloud(a, x, y):
    circle(94*a+x, 53*a+y, 20*a)
    circle(113*a+x, 53*a+y, 20*a)
    circle(131*a+x, 53*a+y, 20*a)
    circle(150*a+x, 53*a+y, 20*a)
    circle(134*a+x, 40*a+y, 20*a)
    circle(112*a+x, 40*a+y, 20*a)
    
penSize(1)
penColor(0,0,0)
brushColor(16,191,62)
rectangle(0, 200, 1600, 400) #grass

brushColor(160, 240, 232) #sky
rectangle(0, 0, 1600, 200)

house_and_tree(1, 0, 0)
house_and_tree(0.632, 253,65)
brushColor(255, 255, 255)
cloud(1,50,0)
cloud(0.7, 180, 60)
cloud(1, 250, 10)

a=[]
n = 30
for i in range(n):
      x = 50
      y=50
      if i%2 == 0:
            a.append((x+30*m.cos(2*m.pi*i/n), y+30*m.sin(2*m.pi*i/n)))
      else:
            a.append((x+35*m.cos(2*m.pi*i/n), y+35*m.sin(2*m.pi*i/n)))
brushColor(249,194,194)
polygon(a)




run()



