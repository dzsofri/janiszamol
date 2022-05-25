from tkinter import *
def deltoidterulet():
    def szamit():
        f = eval(mezo1.get())
        m = eval(mezo2.get())
        if e <= 0 or f <=0:
            mezo4.delete(0, END)
            mezo4.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terulet = (e*f)//2
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

    teruletablak = Tk()
    teruletablak.title("Deltoid területe")
    teruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(teruletablak, text = "E (cm):")
    szoveg2 = Label(teruletablak, text = "F (cm):")
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
    kilep.grid(row = 6, column = 2, sticky = E)

    adattorles = Button(teruletablak, text = "Törlés", command = torles)
    adattorles.grid(row = 6, column = 2, sticky = W)
    
    w = Canvas(teruletablak, width=220, height=200)
    w.create_polygon(50,85,125,10,200,85,125,175, fill="#A8C989", outline = 'black')
    w.create_line(125,175,125,10, fill="red", width=4)
    w.create_line(50, 85, 200, 85, fill="red", width=4)
    w.grid(row = 2, column = 4, rowspan=7, sticky = E)




def deltoidkerulet():

    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        

        if a <= 0 or b <= 0:
            mezo5.delete(0, END)
            mezo5.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            kerulet=2*a+2*b
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
        mezo5.delete(0, END)

    keruletablak = Tk()
    keruletablak.title("DEltoid kerülete")
    keruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(keruletablak, text = "A (cm):")
    szoveg2 = Label(keruletablak, text = "B (cm):")
    szoveg5 = Label(keruletablak, text = "Kerülete (cm):")
    szoveg1.grid(row = 2, column = 1, sticky = W)
    szoveg2.grid(row = 3, column = 1, sticky = W)
    szoveg5.grid(row = 5, column = 1, sticky = W)    
    szamitasgomb = Button(keruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 4, column = 2, sticky = W)

    mezo1 = Entry(keruletablak)
    mezo2 = Entry(keruletablak)
    mezo5 = Entry(keruletablak)

    mezo1.grid(row = 2, column = 2, sticky = W)
    mezo2.grid(row = 3, column = 2, sticky = W)
    mezo5.grid(row = 5, column = 2, sticky = W)

    kilep = Button(keruletablak, text = "Kilépés", command = keruletablak.destroy)
    kilep.grid(row = 6, column = 2, sticky = E)

    adattorles = Button(keruletablak, text = "Törlés", command = torles)
    adattorles.grid(row = 6, column = 2, sticky = W)
       
    w = Canvas(keruletablak, width=220, height=200)
    w.create_polygon(50,85,125,10,200,85,125,175, fill="#A8C989", outline = 'black')
    w.create_line(50,85,125,10, fill="red", width=4)
    w.create_line(50,85,125,175, fill="red", width=4)
    w.grid(row = 3, column = 4, rowspan=7, sticky = E)
    
 
