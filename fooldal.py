from email.iterators import body_line_iterator
from tkinter import *
from tkinter.font import BOLD
fooldal=Tk()
 
menusor=Frame()
menusor.pack(side=TOP, fill=X)

menu1=Menubutton(menusor, text="Névjegy", bg = "#A8C989", fg='white', font=20)
menu1.pack(side=LEFT)
fajl=Menu(menu1, bg = "#769955", fg='white', font=10)
fajl.add_command(label="Készítők")
menu1.config(menu=fajl)

menu2=Menubutton(menusor, text="Kör", bg = "#A8C989", fg='white', font=20)
menu2.pack(side=LEFT)
kor=Menu(menu2, bg = "#769955", fg='white', font=10)
kor.add_command(label="Terület")
kor.add_command(label="Kerület")
menu2.config(menu=kor)

menu3=Menubutton(menusor, text="Négyzet", bg = "#A8C989", fg='white', font=20)
menu3.pack(side=LEFT)
negyzet=Menu(menu3, bg = "#769955", fg='white', font=10)
negyzet.add_command(label="Terület")
negyzet.add_command(label="Kerület")
menu3.config(menu=negyzet)

menu4=Menubutton(menusor, text="Téglalap", bg = "#A8C989", fg='white', font=20)
menu4.pack(side=LEFT)
teglalap=Menu(menu3, bg = "#769955", fg='white', font=10)
teglalap.add_command(label="Terület")
teglalap.add_command(label="Kerület")
menu4.config(menu=teglalap)

menu5=Menubutton(menusor, text="Paralelogramma", bg = "#A8C989", fg='white', font=20)
menu5.pack(side=LEFT)
paralelogramma=Menu(menu5, bg = "#769955", fg='white', font=10)
paralelogramma.add_command(label="Terület")
paralelogramma.add_command(label="Kerület")
menu5.config(menu=paralelogramma)

menu6=Menubutton(menusor, text="Rombusz", bg = "#A8C989", fg='white', font=20)
menu6.pack(side=LEFT)
rombusz=Menu(menu6, bg = "#769955", fg='white', font=10)
rombusz.add_command(label="Terület")
rombusz.add_command(label="Kerület")
menu6.config(menu=rombusz)

menu7=Menubutton(menusor, text="Trapéz", bg = "#A8C989", fg='white', font=20)
menu7.pack(side=LEFT)
trapez=Menu(menu7, bg = "#769955", fg='white', font=10)
trapez.add_command(label="Terület")
trapez.add_command(label="Kerület")
menu7.config(menu=trapez)

menu8=Menubutton(menusor, text="Háromszög", bg = "#A8C989", fg='white', font=20)
menu8.pack(side=LEFT)
haromszog=Menu(menu8, bg = "#769955", fg='white', font=10)
haromszog.add_command(label="Terület")
haromszog.add_command(label="Kerület")
menu8.config(menu=haromszog)

menu9=Menubutton(menusor, text="Deltoid", bg = "#A8C989", fg='white', font=20)
menu9.pack(side=LEFT)
deltoid=Menu(menu9, bg = "#769955", fg='white', font=10)
deltoid.add_command(label="Terület")
deltoid.add_command(label="Kerület")
menu9.config(menu=deltoid)
can1= Canvas(fooldal, width=160, height=160, bg="white")

photo = PhotoImage(file="menukep.png")

can1.grid(row=1, column=3, rowspan=5)
item = can1.create_image(70,70, image= photo)
fooldal.title("Síkidom számítás")
fooldal.minsize(width=400, height=400)
fooldal.mainloop()