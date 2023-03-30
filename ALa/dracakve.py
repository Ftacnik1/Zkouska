import random
pva=50
pvb=50
pvc=50
pvd=50
planek = []
reka = []
polex = []
polex.append(0)
polex.append(14)
bplanek = []
cplanek = []
dplanek = []
mplanek = []
poleLokaci = []
poleLokacib = []
poleLokaciNaVyb = []
def prisera():
    polePriser = []
    add = open('priseraob.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
            polePriser.append(allla)
            allla = str()
        else:
            allla += i
    return(polePriser)
def silapris():
    SiList = []
    add = open('sila.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
                allla=int(allla)
                SiList.append(allla)
                allla = str()
        else:
             allla += i
    return(SiList)
polePriser=prisera()
IndexyPriseryDelka=len(polePriser)-1
PoleSilPriser=silapris()
"""add = open('lokace.txt', 'r')
kkk = add.readlines()
kkk = str(kkk)
allla = str()
z = len(kkk)
z = int(z)
for i in kkk:
    if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
        z = int(z)
    elif ord(i)== 44:
        poleLokaci.append(allla)
        poleLokacib.append(allla)
        poleLokaciNaVyb.append(allla)
        allla = str()
    else:
        allla += i
del poleLokaciNaVyb[5]
del poleLokaciNaVyb[4]
del poleLokaciNaVyb[3]
del poleLokaciNaVyb[2]
del poleLokaciNaVyb[1]
del poleLokaciNaVyb[0]
allla = random.choice(poleLokaciNaVyb)
Lokace = allla
DataOLok = (poleLokaci.index(Lokace,0,len(poleLokaci)))"""
for i in range(10000):
    if (i%100)<50:
        if (i//100)<50:
            a=1
        else: a=2
    else:
        if (i//100)<50:
            a=3 
        else: a=4
    b=0
    c=random.randint(0,IndexyPriseryDelka)
    d=PoleSilPriser[c]
    stat = [a,b,b,c,d]
    planek.append(stat)
c=0  
def mestazaklad(citah):
    if citah==1:
        a=0
        b=random.randint(0,49)+random.randint(0,4)*100 
    elif citah==2:
        a=0
        b=random.randint(50,99)+random.randint(0,4)*100
    elif citah==3:
        a=0
        b=random.randint(0,49)+random.randint(5,9)*100 
    elif citah==4:
        a=0
        b=random.randint(50,99)+random.randint(5,9)*100 
    for i in range (25):
        c=0
        while c==0:
            potlokme=random.randint(a,b)
            if (planek[potlokme][1])==0:
                planek[potlokme][1]=3
                planek[potlokme][2]=2

                c=1
                print(potlokme)
citah=0
for i in range(4):
    citah+=1
    mestazaklad(citah)
while c==0:
    potlokme=random.randint(0,9999)
    if (planek [potlokme] [1])==0:
        planek [potlokme] [1]=4
        c=1
print(planek)
def pen(citah):
    penize=0
    for i in range(10000):
        if planek[i][0]==citah and planek[i][1]>1:
            penize+= planek[i][2]
    print(penize)
    return(penize)
def nabor(citah):
    print("n")
    global pva
    global pvb
    global pvc
    global pvd
    vojaci=0
    for i in range(10000):
        if planek[i][0]==citah and planek[i][1]>1:
            vojaci+= (planek[i][2])//2
    if citah==1:
        pva=pva+vojaci
    elif citah==2:
        pvb=pvb+vojaci
    elif citah==3:
        pvc= pvc +vojaci
    elif citah==4:
        pvd=pvd +vojaci
def tvorbamest(citah,penize):
    c=0
    print("tm")
    while c==0:
        if penize>0:
            prozprom=random.randint(0,9999)
            if planek[prozprom][0]==citah and planek[prozprom][1]>1:
                penize=penize-(int(planek[prozprom][2]))*3
                planek[prozprom][1]=int(planek[prozprom][1])+1
                planek[prozprom][2]=(int(planek[prozprom][2]))*2
        else: c=1
def utok(citah):
    print("u")
    global pva
    global pvb
    global pvc
    global pvd
    if citah==1:
        pv=pva
    elif citah==2:
        pv=pvb
    elif citah==3:
        pv=pvc
    elif citah==4:
        pv=pvd
    prozprom=random.randint(0,9999)
    if planek[prozprom][0]==citah and planek[prozprom][1]==0:
        if pv<10:
            prozproma=pv
            pv=0
        else:
            prozproma=pv
            pv=pv-10
        hodprisery=random.randint(1,6)
        hodvojaku=random.randint(1,2)
        if (hodprisery+int(planek[prozprom][4]))<(hodvojaku+prozproma):
            pv+=prozproma
            planek[prozprom][1]=int(planek[prozprom][1])+1
            planek[prozprom][4]=0
    """if citah==1:
        pva=pv
    elif citah==2:
        pvb=pv
    elif citah==3:
        pvc=pv
    elif citah==4:
        pvd=pv"""
def koloni(citah):
    print("k")
    for i in range(10000):
        if planek[i][0]==citah and planek[i][1]==1:
            planek[i][1]=2
            planek[i][2]=1
def tahstaty():
    citah=1
    for i in range(4):
        citah+=i
        penize=pen(citah)
        prozproma=random.randint(1,4)
        if prozproma==1:
            tvorbamest(citah,penize)
        elif prozproma==2:
            utok(citah)
        elif prozproma==3:
            koloni(citah)
        elif prozproma==4:
            nabor(citah)
for i in range(100):
    tahstaty()
    print("h")
    print(i)
print(pva)
print(pvb)
print(pvc)
print(pvd)
with open ("Kontrola.txt","w") as f1:
    f1.write(str(planek))
print ("Vytisteno")
prozproma=0
for i in range(0,9999):
    if planek[i][2]>1:
        prozproma+=1
print(prozproma)

            

    
    

