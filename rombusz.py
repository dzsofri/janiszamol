from tkinter import *
def terulet():
    def szamit():
        a = eval(mezo1.get())
        m = eval(m2.get())
        if a <= 0 or m <=0:
            mezo4.delete(0, END)
            mezo4.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terulet = a*m 
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
        mezo4.delete(0, END)

    teruletablak = Toplevel(fooldal)
    teruletablak.title("Négyzet területe")
    teruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(teruletablak, text = "a (cm):")
    szoveg2 = Label(teruletablak, text = "m (cm):")
    szoveg4 = Label(teruletablak, text = "Területe (cm2):")

    szoveg1.grid(row = 1, column = 1, sticky = W)
    szoveg4.grid(row = 4, column = 1, sticky = W)
    szoveg2.grid(row = 3, column = 1, sticky = W) 
    
    szamitasgomb = Button(teruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 2, column = 2, sticky = W)

    mezo1 = Entry(teruletablak)
    mezo4 = Entry(teruletablak)
    mezo2 = Entry(teruletablak)

    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo4.grid(row = 4, column = 2, sticky = W)
    mezo2.grid(row = 3, column = 2, sticky = W)

    kilep = Button(teruletablak, text = "Kilépés", command = teruletablak.destroy)
    kilep.grid(row = 5, column = 2, sticky = E)

    adattorles = Button(teruletablak, text = "Törlés", command = torles)
    adattorles.grid(row = 5, column = 2, sticky = W)
    
    w = Canvas(teruletablak, width=220, height=200)
    #w.create_polygon(50,85,125,10,200,85,125,160, fill="#A8C989", outline = 'black')
    #w.create_line(4,100,4,0, fill="red", width=4)
    w.grid(row = 2, column = 4, rowspan=7, sticky = E)
     
    teruletablak.mainloop()



def kerulet():

    def szamit():
        a = eval(mezo1.get())
        

        if a <= 0:
            mezo5.delete(0, END)
            mezo5.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            kerulet = 4*a
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

    keruletablak = Toplevel(fooldal)
    keruletablak.title("Négyzet kerülete")
    keruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(keruletablak, text = "A (cm):")
    szoveg5 = Label(keruletablak, text = "Kerülete (cm):")
    szoveg1.grid(row = 2, column = 1, sticky = W)
    szoveg5.grid(row = 4, column = 1, sticky = W)    
    szamitasgomb = Button(keruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 3, column = 2, sticky = W)

    mezo1 = Entry(keruletablak)
    mezo5 = Entry(keruletablak)

    mezo1.grid(row = 2, column = 2, sticky = W)
    mezo5.grid(row = 4, column = 2, sticky = W)

    kilep = Button(keruletablak, text = "Kilépés", command = keruletablak.destroy)
    kilep.grid(row = 5, column = 2, sticky = E)

    adattorles = Button(keruletablak, text = "Törlés", command = torles)
    adattorles.grid(row = 5, column = 2, sticky = W)
       
    w = Canvas(keruletablak, width=150, height=125)
    #w.create_rectangle(0, 0, 100, 100, fill="#A8C989", outline = 'black')
    #w.create_line(4,100,4,0, fill="red", width=4)
    w.grid(row = 3, column = 4, rowspan=7, sticky = E)
    
 
    keruletablak.mainloop()



#ideiglenes
fooldal = Tk()

fooldal.minsize(100,100)
terulet = Button(fooldal, text = "Terület", command = terulet)
terulet.pack()

kerulet = Button(fooldal, text = "Kerület", command = kerulet)
kerulet.pack()

fooldal.mainloop()