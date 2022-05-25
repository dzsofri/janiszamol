
from tkinter import *
from tkinter.font import BOLD
import paralelogramma
import teglalap
import rombusz
import deltoid
import kor
import haromszog
import trapez
import negyzet
fooldal=Tk()
gyoker="C:\\Users\\beretizsofia\\Desktop\\janiszamol\\"

#-------------importalas-------------
def paralelogrammaT():
    paralelogramma.paralelogrammaterulet()

def paralelogrammaK():
    paralelogramma.paralelogrammakerulet()

def korT():
    kor.korterulet()

def korK():
    kor.korkerulet()

def haromszogT():
    haromszog.haromszogterulet()

def haromszogK():
    haromszog.haromszogkerulet()

def trapezT():
    trapez.trapezterulet()

def trapezK():
    trapez.trapezkerulet()

def negyzetT():
    negyzet.negyzetterulet()

def negyzetK():
    negyzet.negyzetkerulet()

def teglalapT():
    teglalap.teglalapterulet()

def teglalapK():
    teglalap.teglalapkerulet()

def rombuszT():
    rombusz.rombuszterulet()

def rombuszK():
    rombusz.rombuszkerulet()

def deltoidT():
    deltoid.deltoidterulet()

def deltoidK():
    deltoid.deltoidkerulet()
#-------------------------------------
menusor=Frame()
menusor.pack(side=TOP, fill=X)

menu1=Menubutton(menusor, text="Névjegy", bg = "#A8C989", fg='white', font=20)
menu1.pack(side=LEFT)
fajl=Menu(menu1, bg = "#769955", fg='white', font=10)
fajl.add_command(label="Készítők")
menu1.config(menu=fajl)

menu2=Menubutton(menusor, text="Kör", bg = "#A8C989", fg='white', font=20)
menu2.pack(side=LEFT)
kor1=Menu(menu2, bg = "#769955", fg='white', font=10)
kor1.add_command(label="Terület", command=korT, underline=0)
kor1.add_command(label="Kerület", command=korK, underline=0)
menu2.config(menu=kor1)

menu3=Menubutton(menusor, text="Négyzet", bg = "#A8C989", fg='white', font=20)
menu3.pack(side=LEFT)
negyzet1=Menu(menu3, bg = "#769955", fg='white', font=10)
negyzet1.add_command(label="Terület", command=negyzetT, underline=0)
negyzet1.add_command(label="Kerület", command=negyzetK, underline=0)
menu3.config(menu=negyzet1)

menu4=Menubutton(menusor, text="Téglalap", bg = "#A8C989", fg='white', font=20)
menu4.pack(side=LEFT)
teglalap1=Menu(menu4, bg = "#769955", fg='white', font=10)
teglalap1.add_command(label="Terület", command=teglalapT, underline=0)
teglalap1.add_command(label="Kerület", command=teglalapK, underline=0)
menu4.config(menu=teglalap1)


menu5=Menubutton(menusor, text="Paralelogramma", bg = "#A8C989", fg='white', font=20)
menu5.pack(side=LEFT)
paralelogramma1=Menu(menu5, bg = "#769955", fg='white', font=10)
paralelogramma1.add_command(label="Terület", command=paralelogrammaT, underline=0)
paralelogramma1.add_command(label="Kerület", command=paralelogrammaK, underline=0)
menu5.config(menu=paralelogramma1)

menu6=Menubutton(menusor, text="Rombusz", bg = "#A8C989", fg='white', font=20)
menu6.pack(side=LEFT)
rombusz1=Menu(menu6, bg = "#769955", fg='white', font=10)
rombusz1.add_command(label="Terület", command=rombuszT, underline=0)
rombusz1.add_command(label="Kerület", command=rombuszK, underline=0)
menu6.config(menu=rombusz1)


menu7=Menubutton(menusor, text="Trapéz", bg = "#A8C989", fg='white', font=20)
menu7.pack(side=LEFT)
trapez1=Menu(menu7, bg = "#769955", fg='white', font=10)
trapez1.add_command(label="Terület", command=trapezT, underline=0)
trapez1.add_command(label="Kerület", command=trapezK, underline=0)
menu7.config(menu=trapez1)

menu8=Menubutton(menusor, text="Háromszög", bg = "#A8C989", fg='white', font=20)
menu8.pack(side=LEFT)
haromszog1=Menu(menu8, bg = "#769955", fg='white', font=10)
haromszog1.add_command(label="Terület", command=haromszogT, underline=0)
haromszog1.add_command(label="Kerület", command=haromszogK, underline=0)
menu8.config(menu=haromszog1)

menu9=Menubutton(menusor, text="Deltoid", bg = "#A8C989", fg='white', font=20)
menu9.pack(side=LEFT)
deltoid1=Menu(menu9, bg = "#769955", fg='white', font=10)
deltoid1.add_command(label="Terület", command=deltoidT, underline=0) 
deltoid1.add_command(label="Kerület", command=deltoidK, underline=0)
menu9.config(menu=deltoid1)
kép = PhotoImage(file = "menukep.png")
Label(fooldal, image = kép).pack(side = LEFT)


fooldal.title("Síkidom számítás")
fooldal.minsize(width=600, height=400)
fooldal.mainloop()