from tkinter import *
import math
def korterulet():
    def szamit():
        R = eval(mezo1.get())
        if R <= 0:
            mezo2.delete(0, END)
            mezo2.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terulet = (R * R) * math.pi
            mezo2.delete(0,END)
            mezo2.insert(0,str(terulet))

    def habaromvagy():
        try:
            szamit()

        except:
            mezo2.delete(0, END)
            mezo2.insert(0, 'Hibás karakter')

    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)

    korteruletablak = Tk()
    korteruletablak.title("Kör területe")
    korteruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(korteruletablak, text = "Sugár (cm):")
    szoveg2 = Label(korteruletablak, text = "Területe (cm2):")

    szoveg1.grid(row = 3)
    szoveg2.grid(row = 6)
        
    szamitasgomb = Button(korteruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 5, column = 2, sticky = W)

    mezo1 = Entry(korteruletablak)
    mezo2 = Entry(korteruletablak)

    mezo1.grid(row = 3, column = 2, sticky = W)
    mezo2.grid(row = 6, column = 2, sticky = W)

    korkilep = Button(korteruletablak, text = "Kilépés", command = korteruletablak.destroy)
    korkilep.grid(row = 7, column = 3, sticky = W)

    kor_adattorles = Button(korteruletablak, text = "Törlés", command = torles)
    kor_adattorles.grid(row = 7, column = 2, sticky = W)

    korteruletcanvas = Canvas(korteruletablak, width = 200, height = 200, bg = "white")
    korteruletcanvas.grid(column = 4, row = 1, rowspan = 7)
    korteruletcanvas.create_line(102, 102, 182, 102, fill = "red", width = 4)

    def create_circle(x, y, r, canvasName):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)

    create_circle(102, 102, 80, korteruletcanvas)



def korkerulet():
    def szamit():
        R = eval(mezo1.get())
        if R <= 0:
            mezo2.delete(0, END)
            mezo2.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            kerulet = 2 * R * math.pi
            mezo2.delete(0,END)
            mezo2.insert(0,str(kerulet))

    def habaromvagy():
        try:
            szamit()

        except:
            mezo2.delete(0, END)
            mezo2.insert(0, 'Hibás karakter')

    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)

    korkeruletablak = Tk()
    korkeruletablak.title("Kör kerülete")
    korkeruletablak.minsize(width = 300, height = 100)

    szoveg1 = Label(korkeruletablak, text = "Sugár (cm):")
    szoveg2 = Label(korkeruletablak, text = "Kerülete (cm):")

    szoveg1.grid(row = 3)
    szoveg2.grid(row = 6)
        
    szamitasgomb = Button(korkeruletablak, text = "Számítás", command= habaromvagy)
    szamitasgomb.grid(row = 5, column = 2, sticky = W)

    mezo1 = Entry(korkeruletablak)
    mezo2 = Entry(korkeruletablak)

    mezo1.grid(row = 3, column = 2, sticky = W)
    mezo2.grid(row = 6, column = 2, sticky = W)

    korkilep = Button(korkeruletablak, text = "Kilépés", command = korkeruletablak.destroy)
    korkilep.grid(row = 7, column = 3, sticky = W)

    kor_adattorles = Button(korkeruletablak, text = "Törlés", command = torles)
    kor_adattorles.grid(row = 7, column = 2, sticky = W)

    korkeruletcanvas = Canvas(korkeruletablak, width = 200, height = 200, bg = "white")
    korkeruletcanvas.grid(column = 4, row = 1, rowspan = 7)
    korkeruletcanvas.create_line(102, 102, 182, 102, fill = "red", width = 4)

    def create_circle(x, y, r, canvasName):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)

    create_circle(102, 102, 80, korkeruletcanvas)

