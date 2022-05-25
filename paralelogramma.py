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

    paralelogrammaker = Tk()

    paralelogrammaker.title("A paralelogramma kerülete")
    paralelogrammaker.minsize(width=200, height=50)
    gomb1=Button(paralelogrammaker, text="Számítás", command=habaromvagy)
    gomb2=Button(paralelogrammaker, text="Kilép", command=paralelogrammaker.destroy)
    sz1=Label(paralelogrammaker, text="A(cm):")
    sz2=Label(paralelogrammaker, text="B(cm):")
    sz3=Label(paralelogrammaker, text="Eredmény (cm):")
    m1= Entry(paralelogrammaker, width=30)
    m2= Entry(paralelogrammaker, width=30)
    m3= Entry(paralelogrammaker, width=30)

    adattorles = Button(paralelogrammaker, text = "Törlés", command = torles)
    adattorles.grid(row = 7, column = 2, sticky = W)

    sz1.grid(row=1)
    sz2.grid(row=2)
    sz3.grid(row=4)
    gomb1.grid(row=3, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m3.grid(row=4, column=2, sticky=W)
    gomb2.grid(row=7, column=2, sticky=E)

    c = Canvas(paralelogrammaker, width=150, height=150, bg="white")
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
 
    paralelogramma = Tk()
    
    paralelogramma.title("A paralelogramma területe")
    paralelogramma.minsize(width=300, height=100)
    gomb1=Button(paralelogramma, text="Számítás", command=habaromvagy)
    gomb2=Button(paralelogramma, text="Kilép", command=paralelogramma.destroy)
    sz1=Label(paralelogramma, text="A (cm):")
    sz2=Label(paralelogramma, text="M (cm):")
    sz3=Label(paralelogramma, text="Eredmény (cm2):")
    m1= Entry(paralelogramma, width=30)
    m2= Entry(paralelogramma, width=30)
    m3= Entry(paralelogramma, width=30)

    adattorles = Button(paralelogramma, text = "Törlés", command = torles)
    adattorles.grid(row = 7, column = 2, sticky = W)
    
    sz1.grid(row=1)
    sz2.grid(row=2)
    sz3.grid(row=4)
    gomb1.grid(row=3, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m3.grid(row=4, column=2, sticky=W)
    gomb2.grid(row=7, column=2, sticky=E)

    c = Canvas(paralelogramma, width=150, height=150, bg="white")
    c.create_polygon(65, 55, 37.5, 110, 110, 110, 135, 55, outline = "blue", fill = "#A8C989")
    c.create_line(65, 55, 37.5, 110, fill='red', width=4)
    c.create_line(65, 55, 65, 110, fill='red', width=4)        
    c.grid(row=1, column=4, rowspan=7)



