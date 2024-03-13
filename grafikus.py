import tkinter

#Az ablak létrehozása, beállítása

ablak = tkinter.Tk()
ablak.resizable(False, False)
ablak.title("Amőba By KR")

#Az X és O képek importálása, beállítása (illetve a helytartó "kép nélküli kép" beállítása)

x = tkinter.PhotoImage(file="X.png").subsample(3, 3)
o = tkinter.PhotoImage(file="O.png").subsample(3, 3)
helytarto = tkinter.PhotoImage(width=1, height=1)

#Gombok létrehozása

gomb1 = tkinter.Button(ablak, width=200, height=200, image=helytarto, compound="center", command=lambda: kattintva(1))
gomb2 = tkinter.Button(ablak, width=200, height=200, image=helytarto, compound="center", command=lambda: kattintva(2))
gomb3 = tkinter.Button(ablak, width=200, height=200, image=helytarto, compound="center", command=lambda: kattintva(3))

gomb4 = tkinter.Button(ablak, width=200, height=200, image=helytarto, compound="center", command=lambda: kattintva(4))
gomb5 = tkinter.Button(ablak, width=200, height=200, image=helytarto, compound="center", command=lambda: kattintva(5))
gomb6 = tkinter.Button(ablak, width=200, height=200, image=helytarto, compound="center", command=lambda: kattintva(6))

gomb7 = tkinter.Button(ablak, width=200, height=200, image=helytarto, compound="center", command=lambda: kattintva(7))
gomb8 = tkinter.Button(ablak, width=200, height=200, image=helytarto, compound="center", command=lambda: kattintva(8))
gomb9 = tkinter.Button(ablak, width=200, height=200, image=helytarto, compound="center", command=lambda: kattintva(9))

#Érték tábla, gomb lista (egyszerű eléréshez), jatekos változó létrehozása

tabla = [
    ["=","=","="],
    ["=","=","="],
    ["=","=","="]
]

gombok = [gomb1, gomb2, gomb3, gomb4, gomb5, gomb6, gomb7, gomb8, gomb9]

jatekos = 1     #jatekos 1 = X, jatekos 2 = O

#Az érték tábla értékeinek módosítása gombra kattintás után
def beallitas(szam, jatekos):
    sor = (szam-1)//3
    oszlop = (szam-1)%3
    if sor == -1:
        sor = 0
    if jatekos == 1:
        tabla[sor][oszlop] = "x"
    else:
        tabla[sor][oszlop] = "o"

#Az érték tábla értékeinek ellenőrzése (nyert-e valaki?)       

def ellenorzes(jatekos):
    
    #Vízszintes ellenőrzés
    
    for sor in tabla:
        #Soronként ellenőrzi, hogy az elemek megegyeznek-e, ha igen, akkor ellenőrzi, hogy a 3 elem nem-e "=" (ami csak helyfoglalás szempontjából szükséges)
        if (sor[0] == sor[1] == sor[2]) and sor[0] != "=":
            vege(jatekos)

    #Függőleges ellenőrzés
    
    for oszlop in range(3):
        #Ugyanaz mint az előző, csak vertikálisan ellenőriz
        if (tabla[0][oszlop] == tabla[1][oszlop] == tabla[2][oszlop]) and tabla[0][oszlop] != "=":
            vege(jatekos)
    
    #Átlós ellenőrzés
    #Nevéből adódóan átlósan ellenőriz hasonlóan az első kettő ellenőrzéshez
    if (tabla[0][0] == tabla[1][1] == tabla[2][2]) and tabla[0][0] != "=":
        vege(jatekos)
    elif (tabla[0][2] == tabla[1][1] == tabla[2][0]) and tabla[0][2]!= "=":
        vege(jatekos)
        
    #"Döntetlen" ellenőzés
    #Ha nem talál helyfoglalót (placeholder) a mátrixban, akkor döntetlennek nyilvánítja a meccset
    for sor in tabla:
        for oszlop in sor:
            if oszlop == "=":
                return
    vege(3)     #A 3-as a döntetlen meccs jele
    
    
#Új játék indításakor történő érték visszaállítás az alapra
    
def ujra():   
    global tabla
    tabla = [["=","=","="],["=","=","="],["=","=","="]]
    for gomb in gombok:
        gomb["image"] = "pyimage5"
        gomb["state"] = "normal"  


#Játék végén felugró ablak beállítása, elhelyezése

def vege(j):
    for gomb in gombok:
        gomb["state"] = "disabled"
    
    felugro = tkinter.Toplevel(ablak, padx=20, pady=20)
    felugro.resizable(False, False)
    felugro.geometry(f"+{ablak.winfo_rootx()+190}+{ablak.winfo_rooty()+200}")
    felugro.title("Játék vége")
    
    if j == 3:
        szoveg = tkinter.StringVar(felugro, value="Döntetlen!")
    else:
        szoveg = tkinter.StringVar(felugro, value=f"Játékos {j} nyert!")
        
    felirat = tkinter.Label(felugro, textvariable=szoveg).grid(row=0, column=1)
    uj = tkinter.Button(felugro, text="Új játék", command=lambda: [ujra(), felugro.destroy()]).grid(row=1, column=0)
    kilep = tkinter.Button(felugro, text="Kilépés", command=lambda: ablak.quit()).grid(row=1, column=2)
    


#Gombra kattintás után történő ellenőrzések, beállítások (fő függvény)

def kattintva(szama):
    global jatekos
    #pyimage2 = x, pyimage4 = o, pyimage5 = helytarto (a tkinter magától generálja ezeket)
    
    if gombok[szama-1]["image"] == "pyimage5":
        
        if jatekos == 1:
            gombok[szama-1]["image"] = "pyimage2"
            beallitas(szama, jatekos)
        else:
            gombok[szama-1]["image"] = "pyimage4"
            beallitas(szama, jatekos)
            
        gombok[szama-1]["state"] = "disabled"
        
        ellenorzes(jatekos)
            
        if jatekos == 1:
            jatekos = 2
        else:
            jatekos = 1
        
#Gombok elhelyezése az ablakban

gomb1.grid(row=0, column=0)
gomb2.grid(row=0, column=1)
gomb3.grid(row=0, column=2)
gomb4.grid(row=1, column=0)
gomb5.grid(row=1, column=1)
gomb6.grid(row=1, column=2)
gomb7.grid(row=2, column=0)
gomb8.grid(row=2, column=1)
gomb9.grid(row=2, column=2)

#Ablak indítása

ablak.mainloop()