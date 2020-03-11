from tkinter import *			#importer tkinter

def test():				#Pour tester les boutons
    print("blabla")

def test2():				#Pour tester les boutons
    print("wouhou")


def Resize_Image(image, maxsize):
    r1 = image.size[0]/maxsize[0] # rapport largeur
    r2 = image.size[1]/maxsize[1] # rapport hauteur
    ratio = max(r1, r2)
    newsize = (int(image.size[0]/ratio), int(image.size[1]/ratio)) # conserver le rapport hauteur / largeur de l'image
    image = image.resize(newsize, Image.ANTIALIAS)
    return image


window = Tk()				#Création de la fenetre

window.title("My Application")		#mettre un titre a la pages

window.geometry("1080x720")		#mettre une dimention par default 
window.minsize(480, 360)		#mettre une dimention minimale
window.iconbitmap("image/stats.ico")
window.config(background='#FFFFE0')

photo1 = PhotoImage(file='lasagne.gif')
photo2 = PhotoImage(file='curry.gif')



frame=Frame(window, bg='#AAEBCD', bd=1, relief=SUNKEN)


buttonA = Button(frame, image = photo1, command=test).pack(side = RIGHT) 
buttonB = Button(frame, image = photo2, command=test2).pack(side = LEFT) 



frame.pack(expand=YES)

buttonA.grid(row=0, column=0, sticky=W)
buttonB.grid(row=0, column=1, sticky=W)


window.mainloop()
