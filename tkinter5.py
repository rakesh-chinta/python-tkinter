from tkinter import*
import tkinter.messagebox

root=Tk()

answer=tkinter.messagebox.askquestion("question 1","Are you diligent?")

if answer=="yes":
    tkinter.messagebox.showinfo("congrats","your quite persistent!")

    
if answer=="no":
    tkinter.messagebox.showinfo("lazy","you may not attain your goal")

root.mainloop()
