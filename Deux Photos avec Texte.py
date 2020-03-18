from tkinter import *

window = Tk()

frame = Frame(window)
frame.pack()

window.title("My Application")

window.geometry("1080x1080") 
window.minsize(480, 360)
window.config(background='#FFFFE0')


photo1 = PhotoImage(file='lasagne.gif')
photo2 = PhotoImage(file='curry.gif')


frame=Frame(window, bg='#AAEBCD', bd=1, relief=SUNKEN)


buttonA = Button(window,image = photo1, width=800, height=500).pack(side = RIGHT)

buttonB = Button(window, image = photo2, width=800, height=500).pack(side = LEFT)

lbl = Label(window, text="Lasagne", font=30, width=30, height=5, bg= '#FFFFE0')
kbl = Label(window, text="Curry", font=30, width=30, height=5, bg= '#FFFFE0')
lbl.place(y=655)
kbl.place(x=730, y=655)

frame.pack(expand=YES)


window.mainloop()
