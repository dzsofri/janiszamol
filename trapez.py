from tkinter import *
def trapezterulet():
    def szamit():
        if mezo1.get() == "" or mezo2.get() == "" or mezo3.get() == "":
            mezo4.delete(0, END)
            mezo4.insert(0, "Írd be az adatokat!")
        else:
            A = eval(mezo1.get())
            C = eval(mezo2.get())
            M = eval(mezo3.get())

        if A > 0 and C > 0 and M > 0:
            terulet = (A + C) * M / 2 
            mezo4.delete(0, END)
            mezo4.insert(0,str(terulet))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, "Nem jó adat! (x <= 0)")

    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)
        mezo3.delete(0, END)
        mezo4.delete(0, END)

    trapezteruletablak = Toplevel(fooldal)
    trapezteruletablak.title("Trapéz területe")
    trapezteruletablak.minsize(width = 300, height = 100)
    szoveg1 = Label(trapezteruletablak, text = "A:")
    szoveg2 = Label(trapezteruletablak, text = "C:")
    szoveg3 = Label(trapezteruletablak, text = "Magasság:")
    szoveg4 = Label(trapezteruletablak, text = "Eredmény:")

    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 6)
        
    szamitasgomb = Button(trapezteruletablak, text = "Számítás", command= szamit)
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
        
    trapezteruletablak.mainloop()



#kerület



def trapezkerulet():
    def szamit():
        if mezo1.get() == "" or mezo2.get() == "" or mezo3.get() == "" or mezo4.get() == "":
            mezo4.delete(0, END)
            mezo4.insert(0, "Írd be az adatokat!")
        else:
            A = eval(mezo1.get())
            B = eval(mezo2.get())
            C = eval(mezo3.get())
            D = eval(mezo4.get())

        if A > 0 and B > 0 and C > 0 and D > 0:
            terulet = A + B + C + D
            mezo5.delete(0, END)
            mezo5.insert(0,str(terulet))
        else:
            mezo5.delete(0, END)
            mezo5.insert(0, "Nem jó adat! (x <= 0)")

    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)
        mezo3.delete(0, END)
        mezo4.delete(0, END)
        mezo5.delete(0, END)

    trapezkeruletablak = Toplevel(fooldal)
    trapezkeruletablak.title("Trapéz területe")
    trapezkeruletablak.minsize(width = 300, height = 100)
    szoveg1 = Label(trapezkeruletablak, text = "A:")
    szoveg2 = Label(trapezkeruletablak, text = "B:")
    szoveg3 = Label(trapezkeruletablak, text = "C:")
    szoveg4 = Label(trapezkeruletablak, text = "D:")

    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 4)
        
    szamitasgomb = Button(trapezkeruletablak, text = "Számítás", command= szamit)
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
        
    trapezkeruletablak.mainloop()



fooldal = Tk()

fooldal.minsize(100,100)
terulet = Button(fooldal, text = "Terület", command = trapezterulet)
terulet.pack()

kerulet = Button(fooldal, text = "Kerület", command = trapezkerulet)
kerulet.pack()

fooldal.mainloop()
