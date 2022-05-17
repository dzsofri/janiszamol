from tkinter import *
import math


def paralelogrammakerulet():
    def szamit():
        a = eval(m1.get())
        b = eval(m2.get())
        if a<=0 or b<=0:
            m3.delete(0, END)
            m3.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            kerület=2*(a + b)
            m3.delete(0,END)
            m3.insert(0,str(kerület))

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

    paralelogramma = Toplevel(fooldal)
    paralelogramma.title("A paralelogramma kerülete")
    paralelogramma.minsize(width=200, height=50)
    gomb1=Button(paralelogramma, text="Számítás", command=habaromvagy)
    gomb2=Button(paralelogramma, text="Kilép", command=paralelogramma.destroy)
    sz1=Label(paralelogramma, text="a:")
    sz2=Label(paralelogramma, text="b:")
    sz3=Label(paralelogramma, text="Eredmény:")
    m1= Entry(paralelogramma, width=30)
    m2= Entry(paralelogramma, width=30)
    m3= Entry(paralelogramma, width=30)

    adattorles = Button(paralelogramma, text = "Törlés", command = torles)
    adattorles.grid(row = 7, column = 2, sticky = W)

    sz1.grid(row=1)
    sz2.grid(row=2)
    sz3.grid(row=3)
    gomb1.grid(row=4, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m3.grid(row=3, column=2, sticky=W)
    gomb2.grid(row=4, column=2, sticky=E)

    c = Canvas(paralelogramma, width=150, height=150, bg="white")
    c.create_polygon(65, 55, 37.5, 110, 110, 110, 135, 55, outline = "blue", fill = "#A8C989")
    c.create_line(65, 55, 37.5, 110, fill='red', width=4)
    c.create_line(65, 55, 135, 55, fill='red', width=4)    
    c.grid(row=1, column=4, rowspan=7)

def paralelogrammaterulet():
    def szamit():
        a = eval(m1.get())
        m = eval(m2.get())
        if a<=0 or m<=0:
            m3.delete(0, END)
            m3.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terulet= a*m
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
 
    paralelogramma = Toplevel(fooldal)
    paralelogramma.title("A paralelogramma területe")
    paralelogramma.minsize(width=300, height=100)
    gomb1=Button(paralelogramma, text="Számítás", command=habaromvagy)
    gomb2=Button(paralelogramma, text="Kilép", command=paralelogramma.destroy)
    sz1=Label(paralelogramma, text="a:")
    sz2=Label(paralelogramma, text="m:")
    sz3=Label(paralelogramma, text="Eredmény:")
    m1= Entry(paralelogramma, width=30)
    m2= Entry(paralelogramma, width=30)
    m3= Entry(paralelogramma, width=30)

    adattorles = Button(paralelogramma, text = "Törlés", command = torles)
    adattorles.grid(row = 7, column = 2, sticky = W)
    
    sz1.grid(row=1)
    sz2.grid(row=2)
    sz3.grid(row=3)
    gomb1.grid(row=4, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m3.grid(row=3, column=2, sticky=W)
    gomb2.grid(row=4, column=2, sticky=E)

    c = Canvas(paralelogramma, width=150, height=150, bg="white")
    c.create_polygon(65, 55, 37.5, 110, 110, 110, 135, 55, outline = "blue", fill = "#A8C989")
    c.create_line(65, 55, 37.5, 110, fill='red', width=4)
    c.create_line(65, 55, 65, 110, fill='red', width=4)        
    c.grid(row=1, column=4, rowspan=7)

fooldal = Tk()

gomb1= Button(fooldal, text="Kerület", command=paralelogrammakerulet)
gomb1.pack()
gomb2= Button(fooldal, text="Terület", command=paralelogrammaterulet)
gomb2.pack()
fooldal.mainloop()

