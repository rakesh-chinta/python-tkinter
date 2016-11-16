from tkinter import *
root=Tk()

topFrame=Frame(root)
topFrame.pack()

botFrame=Frame(root)
botFrame.pack(side=BOTTOM)

Button1=Button(topFrame,text="click me!",fg="Blue")
Button1.pack(side=LEFT)

Button2=Button(topFrame,text="Hi rakesh!",fg="Yellow")
Button2.pack(side=LEFT)

Button3=Button(botFrame,text="Hi chinta!",fg="Green")
Button3.pack(side=LEFT)


Button4=Button(botFrame,text="Hi naga!",fg="Red")
Button4.pack(side=LEFT)

root.mainloop()
