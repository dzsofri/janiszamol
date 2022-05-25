from tkinter import *
def teglalapterulet():
    def szamit():
        A = eval(mezo1.get())
        B = eval(mezo2.get())
        if A <= 0 or B <= 0:
            mezo3.delete(0, END)
            mezo3.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terulet = A * B
            mezo3.delete(0,END)
            mezo3.insert(0,str(terulet))

    def habaromvagy():
        try:
            szamit()

        except:
            mezo3.delete(0, END)
            mezo3.insert(0, 'Hibás karakter')

    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)
        mezo3.delete(0, END)

    teglalapteruletablak = Tk()


    teglalapteruletablak.title("Téglalap területe")
    teglalapteruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(teglalapteruletablak, text = "A (cm):")
    szoveg2 = Label(teglalapteruletablak, text = "B (cm):")
    szoveg3 = Label(teglalapteruletablak, text = "Területe (cm2):")

    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 6)
        
    szamitasgomb = Button(teglalapteruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 5, column = 2, sticky = W)

    mezo1 = Entry(teglalapteruletablak)
    mezo2 = Entry(teglalapteruletablak)
    mezo3 = Entry(teglalapteruletablak)

    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 6, column = 2, sticky = W)

    teglalapkilep = Button(teglalapteruletablak, text = "Kilépés", command = teglalapteruletablak.destroy)
    teglalapkilep.grid(row = 7, column = 3, sticky = W)

    teglalap_adattorles = Button(teglalapteruletablak, text = "Törlés", command = torles)
    teglalap_adattorles.grid(row = 7, column = 2, sticky = W)

    teglalapteruletcanvas = Canvas(teglalapteruletablak, width = 200, height = 200, bg = "white")
    teglalapteruletcanvas.create_polygon(25, 40, 180, 40, 180, 150, 25, 150, fill = "#A8C989", outline = "black")
    teglalapteruletcanvas.create_line(25, 40, 180, 40, fill="red", width = 4)
    teglalapteruletcanvas.create_line(180, 40, 180, 150, fill = "red", width = 4)
    teglalapteruletcanvas.grid(column = 4, row = 1, rowspan = 8)



def teglalapkerulet():

    def szamit():
        A = eval(mezo1.get())
        B = eval(mezo2.get())
        if A <= 0 or B <= 0:
            mezo3.delete(0, END)
            mezo3.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            kerulet = 2 * (A + B)
            mezo3.delete(0,END)
            mezo3.insert(0,str(kerulet))

    def habaromvagy():
        try:
            szamit()

        except:
            mezo3.delete(0, END)
            mezo3.insert(0, 'Hibás karakter')

    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)
        mezo3.delete(0, END)

    teglalapkeruletablak = Tk()

    teglalapkeruletablak.title("Téglalap kerülete")
    teglalapkeruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(teglalapkeruletablak, text = "A (cm):")
    szoveg2 = Label(teglalapkeruletablak, text = "B (cm):")
    szoveg3 = Label(teglalapkeruletablak, text = "Kerülete (cm):")

    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 6)
        
    szamitasgomb = Button(teglalapkeruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 5, column = 2, sticky = W)

    mezo1 = Entry(teglalapkeruletablak)
    mezo2 = Entry(teglalapkeruletablak)
    mezo3 = Entry(teglalapkeruletablak)

    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 6, column = 2, sticky = W)

    teglalapkilep = Button(teglalapkeruletablak, text = "Kilépés", command = teglalapkeruletablak.destroy)
    teglalapkilep.grid(row = 7, column = 3, sticky = W)

    teglalap_adattorles = Button(teglalapkeruletablak, text = "Törlés", command = torles)
    teglalap_adattorles.grid(row = 7, column = 2, sticky = W)

    teglalapkeruletcanvas = Canvas(teglalapkeruletablak, width = 200, height = 200, bg = "white")
    teglalapkeruletcanvas.create_polygon(25, 40, 180, 40, 180, 150, 25, 150, fill = "#A8C989", outline = "black")
    teglalapkeruletcanvas.create_line(25, 40, 180, 40, fill="red", width = 4)
    teglalapkeruletcanvas.create_line(180, 40, 180, 150, fill = "red", width = 4)
    teglalapkeruletcanvas.grid(column = 4, row = 1, rowspan = 7)
        


