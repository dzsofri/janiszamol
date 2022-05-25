from tkinter import *
def trapezterulet():
    def szamit():
        A = eval(mezo1.get())
        C = eval(mezo2.get())
        M = eval(mezo3.get())
        if A <= 0 or C <= 0 or M <= 0:
            mezo4.delete(0, END)
            mezo4.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terulet = (A + C) * M / 2 
            mezo4.delete(0,END)
            mezo4.insert(0,str(terulet))

    def habaromvagy():
        try:
            szamit()

        except:
            mezo4.delete(0, END)
            mezo4.insert(0, 'Hibás karakter')

    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)
        mezo3.delete(0, END)
        mezo4.delete(0, END)

    trapezteruletablak = Tk()
    trapezteruletablak.title("Trapéz területe")
    trapezteruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(trapezteruletablak, text = "A (cm):")
    szoveg2 = Label(trapezteruletablak, text = "C (cm):")
    szoveg3 = Label(trapezteruletablak, text = "Magasság (cm): ")
    szoveg4 = Label(trapezteruletablak, text = "Területe (cm2):")

    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 6)
        
    szamitasgomb = Button(trapezteruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 5, column = 2, sticky = W)

    mezo1 = Entry(trapezteruletablak)
    mezo2 = Entry(trapezteruletablak)
    mezo3 = Entry(trapezteruletablak)
    mezo4 = Entry(trapezteruletablak)

    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 6, column = 2, sticky = W)

    trapezkilep = Button(trapezteruletablak, text = "Kilépés", command = trapezteruletablak.destroy)
    trapezkilep.grid(row = 7, column = 3, sticky = W)

    trapez_adattorles = Button(trapezteruletablak, text = "Törlés", command = torles)
    trapez_adattorles.grid(row = 7, column = 2, sticky = W)

    trapezteruletcanvas = Canvas(trapezteruletablak, width = 200, height = 200, bg = "white")
    trapezteruletcanvas.create_line(15, 125, 185, 125, fill="red", width = 4)
    trapezteruletcanvas.create_line(140, 50, 60, 50, fill = "red", width = 4)
    trapezteruletcanvas.create_line(15, 125, 60, 50, fill = "black", width= 2)
    trapezteruletcanvas.create_line(185, 125, 140, 50, fill = "black", width= 2)
    trapezteruletcanvas.create_line(100, 125, 100, 50, fill = "red", width = 4)
    trapezteruletcanvas.grid(column = 4, row = 1, rowspan = 8)





def trapezkerulet():

    def szamit():
        A = eval(mezo1.get())
        B = eval(mezo2.get())
        C = eval(mezo3.get())
        D = eval(mezo4.get())

        if A <= 0 or B <= 0 or C <= 0 or D <= 0:
            mezo5.delete(0, END)
            mezo5.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            kerulet = A + B + C + D
            mezo5.delete(0,END)
            mezo5.insert(0,str(kerulet))

    def habaromvagy():
        try:
            szamit()

        except:
            mezo5.delete(0, END)
            mezo5.insert(0, 'Hibás karakter')

    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)
        mezo3.delete(0, END)
        mezo4.delete(0, END)
        mezo5.delete(0, END)

    trapezkeruletablak = Tk()
    trapezkeruletablak.title("Trapéz kerülete")
    trapezkeruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(trapezkeruletablak, text = "A (cm):")
    szoveg2 = Label(trapezkeruletablak, text = "B (cm):")
    szoveg3 = Label(trapezkeruletablak, text = "C (cm):")
    szoveg4 = Label(trapezkeruletablak, text = "D (cm):")
    szoveg5 = Label(trapezkeruletablak, text = "Kerülete (cm):")

    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 4)
    szoveg5.grid(row = 6)
        
    szamitasgomb = Button(trapezkeruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 5, column = 2, sticky = W)

    mezo1 = Entry(trapezkeruletablak)
    mezo2 = Entry(trapezkeruletablak)
    mezo3 = Entry(trapezkeruletablak)
    mezo4 = Entry(trapezkeruletablak)
    mezo5 = Entry(trapezkeruletablak)

    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 4, column = 2, sticky = W)
    mezo5.grid(row = 6, column = 2, sticky = W)

    trapezkilep = Button(trapezkeruletablak, text = "Kilépés", command = trapezkeruletablak.destroy)
    trapezkilep.grid(row = 7, column = 3, sticky = W)

    trapez_adattorles = Button(trapezkeruletablak, text = "Törlés", command = torles)
    trapez_adattorles.grid(row = 7, column = 2, sticky = W)

    trapezkeruletcanvas = Canvas(trapezkeruletablak, width = 200, height = 200, bg = "white")
    trapezkeruletcanvas.create_line(15, 125, 185, 125, fill="red", width = 4)
    trapezkeruletcanvas.create_line(140, 50, 60, 50, fill = "red", width = 4)
    trapezkeruletcanvas.create_line(15, 125, 60, 50, fill = "red", width = 4)
    trapezkeruletcanvas.create_line(185, 125, 140, 50, fill = "red", width = 4)
    trapezkeruletcanvas.grid(column = 4, row = 1, rowspan = 7)
        
