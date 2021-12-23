from tkinter import*
import tkinter as tk
root=tk.Tk()
root.geometry("700x600")
frame=tk.Frame()
frame.master.title("GAME")
canvas=tk.Canvas(frame)

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

## text welcome
canvas.create_text(350, 100, text="Welcome", fill="red", font=("Helvetica 40 bold"),tags="weldelete")

## create button start
btn = Button(root, text="Start Game", width=20, height=3, bd="5", command=toDispley, background="green")
btn.place(x=250, y=450)

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()
