from tkinter import *
window = Tk()

e1 = Entry(window)
e1.grid(row=0,column=1)

e2 = Entry(window)
e2.grid(row=1,column=1)

resultfield = Text(window,height=1,width=20)
resultfield.grid(row=2,column=1)

b1=Button(window,text='mul')
b1.grid(row=3,column=1)

b2=Button(window,text='add')
b2.grid(row=3,column=2)

b3=Button(window,text='div')
b3.grid(row=4,column=1)

b4=Button(window,text='sub')
b4.grid(row=4,column=2)

b5=Button(window,text='all')
b5.grid(row=5,column=1)

b6=Button(window,text='exit')
b6.grid(row=5,column=2)

window.mainloop()
