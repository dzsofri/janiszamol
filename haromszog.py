from tkinter import *
import math


def haromszogkerulet():
    def szamit():
        a = eval(m1.get())
        b = eval(m2.get())
        c = eval(m3.get())
        if a<=0 or b<=0 or c<=0:
            m4.delete(0, END)
            m4.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            kerület=a + b + c
            m4.delete(0,END)
            m4.insert(0,str(kerület))

    def habaromvagy():
        try:
            szamit()

        except:
            m4.delete(0, END)
            m4.insert(0, 'Hibás karakter')

    def torles():
        m1.delete(0, END)
        m2.delete(0, END)
        m3.delete(0, END)
        m4.delete(0, END)

    haromszog = Toplevel(fooldal)
    haromszog.title("A háromszög kerülete")
    haromszog.minsize(width=200, height=50)
    gomb1=Button(haromszog, text="Számítás", command=habaromvagy)
    gomb2=Button(haromszog, text="Kilép", command=haromszog.destroy)
    sz1=Label(haromszog, text="a:")
    sz2=Label(haromszog, text="b:")
    sz3=Label(haromszog, text="c:")
    sz4=Label(haromszog, text="Eredmény:")
    m1= Entry(haromszog, width=30)
    m2= Entry(haromszog, width=30)
    m3= Entry(haromszog, width=30)
    m4= Entry(haromszog, width=30)

    adattorles = Button(haromszog, text = "Törlés", command = torles)
    adattorles.grid(row = 7, column = 2, sticky = W)

    sz1.grid(row=1)
    sz2.grid(row=2)
    sz3.grid(row=3)
    sz4.grid(row=4)
    gomb1.grid(row=5, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m3.grid(row=3, column=2, sticky=W)
    m4.grid(row=4, column=2, sticky=W)
    gomb2.grid(row=5, column=2, sticky=E)

    c = Canvas(haromszog, width=150, height=125, bg="white")
    c.create_polygon(65, 35, 45, 90, 100, 90, outline = "red", width=4 , fill = "#A8C989")
    #c.create_line(65, 55, 37.5, 110, fill='red', width=4)
    #c.create_line(65, 55, 135, 55, fill='red', width=4)    
    c.grid(row=1, column=4, rowspan=7)

def haromszogterulet():
    def szamit():
        a = eval(m1.get())
        m = eval(m2.get())
        if a<=0 or m<=0:
            m3.delete(0, END)
            m3.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terulet= round((a*m)/2)
            m3.delete(0,END)
            m3.insert(0,str(terulet))

    def habaromvagy():
        try:
            szamit()

        except:
            m3.delete(0, END)
            m3.insert(0, 'Hibás karakter')

    def torles():
        m1.delete(0, END)
        m2.delete(0, END)
        m3.delete(0, END)
 
    haromszog = Toplevel(fooldal)
    haromszog.title("A háromszög területe")
    haromszog.minsize(width=300, height=100)
    gomb1=Button(haromszog, text="Számítás", command=habaromvagy)
    gomb2=Button(haromszog, text="Kilép", command=haromszog.destroy)
    sz1=Label(haromszog, text="a:")
    sz2=Label(haromszog, text="m:")
    sz3=Label(haromszog, text="Eredmény:")
    m1= Entry(haromszog, width=30)
    m2= Entry(haromszog, width=30)
    m3= Entry(haromszog, width=30)
    
    adattorles = Button(haromszog, text = "Törlés", command = torles)
    adattorles.grid(row = 7, column = 2, sticky = W)

    sz1.grid(row=1)
    sz2.grid(row=2)
    sz3.grid(row=3)
    gomb1.grid(row=4, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m3.grid(row=3, column=2, sticky=W)
    gomb2.grid(row=4, column=2, sticky=E)

    c = Canvas(haromszog, width=150, height=125, bg="white")
    c.create_polygon(65, 35, 45, 90, 100, 90, outline = "blue", fill = "#A8C989")
    c.create_line(45, 90, 100, 90, fill='red', width=4)
    c.create_line(66, 36, 65, 88, fill='red', width=4)    
    c.grid(row=1, column=4, rowspan=7)

fooldal = Tk()

gomb1= Button(fooldal, text="Kerület", command=haromszogkerulet)
gomb1.pack()
gomb2= Button(fooldal, text="Terület", command=haromszogterulet)
gomb2.pack()
fooldal.mainloop()


