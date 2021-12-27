import random
from tkinter import*
import tkinter as tk
# import winsound
root=tk.Tk()
root.geometry("700x600")
frame=tk.Frame()
frame.master.title("EATING CAKE")
canvas=tk.Canvas(frame)

## Array of Cake 
arrayOfCake = []
varrayOfDiamon = []

## speedDuration
speedDuration = 50

## create background
image=PhotoImage(file="images/welcome.png")
images=PhotoImage(file="images/background.png")
pic=PhotoImage(file="images/robot.png")
cake = PhotoImage(file="images/cupcake.png")
coin = PhotoImage(file="images/coin.png")
diamon = PhotoImage(file="images/diamon.png")
boom = PhotoImage(file="images/boom.png")
picture=canvas.create_image(0,0,image=image,anchor="nw",tags="remove")

## dispay game
def toDispley():
    canvas.delete("remove")
    canvas.delete("weldelete")
    btn.place_forget()
    picture=canvas.create_image(0,0,image=images,anchor="nw",tags="remove")
    drawGrid()
    # print("todisplay")
    addCake ()
    canvas.after(30000,lambda:addDiamon())
    
def addCake ():
    global arrayOfCake
    cakeX = random.randrange(50,650)
    arrayOfCake.append(canvas.create_image(cakeX,-25,image=cake,tags="item"))
    canvas.after(600,lambda:addCake())
    moveitems()
def addDiamon ():
    global arrayOfDiamon
    diamonX = random.randrange(50,650)
    arrayOfCake.append(canvas.create_image(diamonX,-25,image=diamon,tags="item"))
    canvas.after(32000,lambda:addDiamon())
    

## text welcome
canvas.create_text(350, 100, text="Welcome", fill="red", font=("Helvetica 40 bold"),tags="weldelete")

## create button start
btn = Button(root, text="Start Game", width=20, height=3, bd="5", command=toDispley, background="green")
btn.place(x=250, y=450)

## display grid
grid=[0,0,0,0,0,0,1,0,0,0,0,0,0,0]
def drawGrid():
    ## create text of score
    canvas.create_text(600,50,text="Score : 0",font=("Purisa",16),fill="white")
    ## create sound
    # winsound.PlaySound("sound\mixkit.wav",winsound.SND_FILENAME)
    x1=0
    x2=50
    y1=550
    y2=y1 + 60
    for val in grid:
        if val==0:
            canvas.create_rectangle(x1,y1,x2,y2,fill="",outline="")
        else:
            canvas.create_rectangle(x1,y1,x2,y2,fill="",outline="")
            canvas.create_image(x1+25,y2-30,image=pic)
        x1+=50
        x2=x1+50 

## count score

## move animation
def moveitems():
    global speedDuration
    speedDuration += 20
    canvas.move("item",0,10)
    canvas.after(speedDuration,lambda:moveitems())

## move
def moveLeft(event):
    global grid
    istrue=False
    for i in range(1,len(grid)):
        if grid[i]==1:
            istrue=True
            grid[i]=0
            grid[i-1]=1
    drawGrid()
root.bind("<l>", moveLeft)
root.bind("<Left>", moveLeft)
def moveRight(event):
    global grid
    istrue=True
    for i in range(len(grid)-1):
        if grid[i]==1 and istrue:
            istrue=False
            grid[i]=0
            grid[i+1]=1
    drawGrid()
root.bind("<r>", moveRight)
root.bind("<Right>", moveRight)

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()