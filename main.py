from tkinter import*
import tkinter as tk
root=tk.Tk()
root.geometry("700x600")
frame=tk.Frame()
frame.master.title("EATING CAKE")
canvas=tk.Canvas(frame)
robot=tk.PhotoImage(file="images/welcome.png")
## create background
image=PhotoImage(file="images/welcome.png")
images=PhotoImage(file="images/background.png")
picture=canvas.create_image(0,0,image=image,anchor="nw",tags="remove")

## dispayGrid
def toDispley():
    canvas.delete("remove")
    canvas.delete("weldelete")
    btn.place_forget()
    picture=canvas.create_image(0,0,image=images,anchor="nw",tags="remove")
    drawGrid()

## text welcome
canvas.create_text(350, 100, text="Welcome", fill="red", font=("Helvetica 40 bold"),tags="weldelete")

## create button start
btn = Button(root, text="Start Game", width=20, height=3, bd="5", command=toDispley, background="green")
btn.place(x=250, y=450)

## display game
grid=[0,0,0,0,0,0,1,0,0,0,0,0,0,0]
def drawGrid():
    x1=0
    x2=50
    y1=550
    y2=y1 + 60
    for val in grid:
        if val==0:
            canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline="")
        else:
            canvas.create_rectangle(x1,y1,x2,y2,fill="green",outline="")
        x1+=50
        x2=x1+50 

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
