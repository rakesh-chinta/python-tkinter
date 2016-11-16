from tkinter import*

root=Tk()

def printName(event):
    print("Hi! I am rakesh chinta")
    
button1=Button(root,text="Click me!")
button1.bind("<Button-1>",printName)
button1.pack()
root.mainloop()

