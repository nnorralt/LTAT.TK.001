fail = input('sisesta failinimi')
f = open(fail, encoding="UTF-8")
riigitahised = list((input("sisesta maade tähised")).split(" "))
def failist_sonastik(f):
    sonastik = {}
    CSVflist = []
    for rida in f:
        CSVflist.append(rida.rstrip().split(" "))
    print(CSVflist)
    for CSVrida in range(len(CSVflist)):
        if (len(CSVflist[CSVrida])) == 2: #tingimuslause selleks et ainult üherealisi riigitähiseid ignoreerida!!!
            key = str(CSVflist[CSVrida][0])
            value = str(CSVflist[CSVrida][1])
            sonastik[key] = value
        else:
            pass
    return sonastik
    
#vanused = {"Kersti": 46, "Jüri": 38, "Jevgeni": 30, "Mart": 67}
#kolmikud = ("Sofia", "Maria", "Kersti")
#for nimi in kolmikud:
    #if nimi not in vanused:
       # vanused[nimi] = 13

def tahised_nimedeks(riigitahised, failist_sonastik):
    riiginimed = []
    for tahis in riigitahised: #käib läbi kõik inputiga sisestatud riigitähised

        if tahis in failist_sonastik: #True
            riiginimed.append(failist_sonastik[tahis]) #lisab riiginimede järjendisse sonastikust key'ga "tahis" - KeyError
        if tahis not in failist_sonastik:
            riiginimed.append(None)     #kui mõni tähis argument järjendis on tundmatu läheb selle riiginimeks None väärtus

    return riiginimed

for maad in tahised_nimedeks(riigitahised, failist_sonastik(f)):
    if maad == None:
        print("Tundmatu maa")
    else:
        print(maad)