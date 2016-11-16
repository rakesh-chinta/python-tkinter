from tkinter import*

root=Tk()

def printName():
    print("Hi! I am rakesh chinta")
    
button1=Button(root,text="Click me!",command=printName)
button1.pack()
root.mainloop()
