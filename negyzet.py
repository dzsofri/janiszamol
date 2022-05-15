from tkinter import *
def negyzetterulet():
    def szamit():
        A = eval(mezo1.get())
        if A <= 0:
            mezo4.delete(0, END)
            mezo4.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terulet = A**2 
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
        mezo4.delete(0, END)

    negyzetteruletablak = Toplevel(fooldal)
    negyzetteruletablak.title("Négyzet területe")
    negyzetteruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(negyzetteruletablak, text = "A (cm):")
    szoveg4 = Label(negyzetteruletablak, text = "Területe (cm2):")

    szoveg1.grid(row = 1)
    szoveg4.grid(row = 6)
        
    szamitasgomb = Button(negyzetteruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 5, column = 2, sticky = W)

    mezo1 = Entry(negyzetteruletablak)
    mezo4 = Entry(negyzetteruletablak)

    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo4.grid(row = 6, column = 2, sticky = W)

    negyzetkilep = Button(negyzetteruletablak, text = "Kilépés", command = negyzetteruletablak.destroy)
    negyzetkilep.grid(row = 7, column = 3, sticky = W)

    negyzet_adattorles = Button(negyzetteruletablak, text = "Törlés", command = torles)
    negyzet_adattorles.grid(row = 7, column = 2, sticky = W)
        
    negyzetteruletablak.mainloop()



def negyzetkerulet():

    def szamit():
        A = eval(mezo1.get())
        

        if A <= 0:
            mezo5.delete(0, END)
            mezo5.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            kerulet = 4*A
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
        mezo5.delete(0, END)

    negyzetkeruletablak = Toplevel(fooldal)
    negyzetkeruletablak.title("Trapéz kerülete")
    negyzetkeruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(negyzetkeruletablak, text = "A (cm):")
    szoveg5 = Label(negyzetkeruletablak, text = "Kerülete (cm):")
    szoveg2 = Label(negyzetkeruletablak, text = "A")
    szoveg1.grid(row = 1, column = 1, sticky = W)
    szoveg5.grid(row = 3, column = 1, sticky = W)
    szoveg2.grid(row = 3, column = 3, sticky = E,padx = 5)    
    szamitasgomb = Button(negyzetkeruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 2, column = 2, sticky = W)

    mezo1 = Entry(negyzetkeruletablak)
    mezo5 = Entry(negyzetkeruletablak)

    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo5.grid(row = 3, column = 2, sticky = W)

    kilep = Button(negyzetkeruletablak, text = "Kilépés", command = negyzetkeruletablak.destroy)
    kilep.grid(row = 4, column = 2, sticky = E)

    adattorles = Button(negyzetkeruletablak, text = "Törlés", command = torles)
    adattorles.grid(row = 4, column = 2, sticky = W)
       
    w = Canvas(negyzetkeruletablak, width=200, height=200)
    w.create_rectangle(0, 0, 150, 150, fill="#A8C989", outline = 'black')
    w.create_line(4,150,4,0, fill="red", width=4)
    w.grid(row = 2, column = 4, rowspan=7, sticky = E)
    
 
    negyzetkeruletablak.mainloop()



#ideiglenes
fooldal = Tk()

fooldal.minsize(100,100)
terulet = Button(fooldal, text = "Terület", command = negyzetterulet)
terulet.pack()

kerulet = Button(fooldal, text = "Kerület", command = negyzetkerulet)
kerulet.pack()

fooldal.mainloop()