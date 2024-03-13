tabla = [
    ["=","=","="],
    ["=","=","="],
    ["=","=","="]
]

j_szam = 1


#Sor, oszlop koordináták bekérése
def bekeres(jel):
    print(f"Az {jel.upper()} következik!")
    while True:
        try:
            sor = int(input("Sor: "))-1
            oszlop = int(input("Oszlop: "))-1
            
            if tabla[sor][oszlop] == "=":
                tabla[sor][oszlop] = jel
                return
            else:
                print("Ez a hely már foglalt!")
        except:
            print("Hiba")
        
        
#Sor, oszlop, átló ellenőrzése        
        
def ellenorzes():
    #Vízszintes ellenőrzés
    for sor in tabla:
        if (sor[0] == sor[1] == sor[2]) and sor[0] != "=":
            return True

    #Függőleges ellenőrzés
    for oszlop in range(3):
        if (tabla[0][oszlop] == tabla[1][oszlop] == tabla[2][oszlop]) and tabla[0][oszlop] != "=":
            return True
    
    #Átlós ellenőrzés
    if (tabla[0][0] == tabla[1][1] == tabla[2][2]) and tabla[0][0] != "=":
        return True
    elif (tabla[0][2] == tabla[1][1] == tabla[2][0]) and tabla[0][2]!= "=":
        return True
        
        
#Játék vége        
        
def vege(szama):
    if szama == 1:
        print(f"Játékos 1 (X) nyert!")
    else:
        print(f"Játékos 2 (O) nyert!")
    
#Kezdő ábra    
    
for sor in tabla:
        for oszlop in range(3):
            if oszlop != 2:
                print(sor[oszlop] + "\t",end="")
            else:
                print(sor[oszlop])

#Főciklus

while True:
    if j_szam == 1:
        bekeres("x")
    else:
        bekeres("o")
    
    for sor in tabla:
        for oszlop in range(3):
            if oszlop != 2:
                print(sor[oszlop] + "\t",end="")
            else:
                print(sor[oszlop])
            
            
    if ellenorzes():
        vege(j_szam)
        break
        
    if j_szam == 1:
        j_szam = 2
    else:
        j_szam = 1