import random
from tkinter import*
root=Tk()
root.geometry("700x600")
frame=Frame()
canvas=Canvas()
frame.master.title("EATING CAKE")
## import image-----------------------------------
pic=PhotoImage(file="images/robot.png")
cake=PhotoImage(file="images/cupcake.png")
##create image-------------------------------------------------
cakes=canvas.create_image(40,20,image=cake)
duck=canvas.create_image(100,400,image=pic,tags="bird")
## move robort ------------------------------------------------
positon=0
def move_left(event):
    global positon ,posiduck
    posiduck=canvas.coords(duck)
    canvas.move(duck,-10,0)
def move_right(event):
    global posiduck
    print(canvas.coords(duck))
    posiduck=canvas.coords(duck)
    if posiduck[0]<600:
        canvas.move(duck,10,0)   
def dropCake():
    global cakes ,posiduck
    canvas.move(cakes,0,10)
    cake=canvas.coords(cakes)
    print(posiduck,cake)
    chack(posiduck,cake)
    canvas.after(1000,lambda:dropCake())
## if robot meet cake  game win----------------------------------
posiduck=[0,0]
def chack(duckPosi,cakePosi):
    if cakePosi[1]==duckPosi[1] and cakePosi[0]==duckPosi[0]:
        canvas.delete("all")
dropCake()
root.bind('<Left>',move_left)
root.bind('<Right>',move_right)
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()