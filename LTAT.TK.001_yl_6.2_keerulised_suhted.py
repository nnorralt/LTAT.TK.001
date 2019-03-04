def seosta_lapsed_ja_vanemad(laps,nimi):
    lapsefail = open('lapsefail.txt', encoding="UTF-8")
    nimefail = open('nimedefail.txt', encoding="UTF-8")
    lapsjrj = []
    nimedjrj = []
    seosedjrj = []
    for rida in lapsefail:
        lapsjrj.append(rida.rstrip().split(" "))
        #print(lapsjrj)
        #print(len(lapsjrj))
    for rida in nimefail:
        nimedjrj.append(rida.rstrip().split(None,1)) #teen endale kena sõnastiku 
    nimed = dict(nimedjrj) #nimed on mu isikukood-nimi tuvastuse sõnastik nüüd
    seosed = dict()
    uusjrj = []
    uusjrj2 = []
    for el in range(len(lapsjrj)):
        lapsjrj[el][0] = nimed[lapsjrj[el][0]] #vanemate isikukoodid muudan sõnastiku järgi nende väärtusteks ehk nimeks
        lapsjrj[el][1] = nimed[lapsjrj[el][1]] #nüüd on meil vanemate ja nende laste järjendid kahemõõtmelises järjendis
    for xel in range(len(lapsjrj)): #itereerin läbi uuendatud listi
        for zel in range((xel+1),len(lapsjrj)):  #kontrollin neid uuesti
            if lapsjrj[xel][0] == lapsjrj[zel][0]:
                lapsjrj[xel].append(lapsjrj[zel].pop(1))
    for jrj in range(len(lapsjrj)):
        if len(lapsjrj[jrj]) != 1:
            uusjrj.append(lapsjrj[jrj])
    for i in range(len(uusjrj)):
        ajlist = [[uusjrj[i][0],set(uusjrj[i][1:])]]
        uusjrj2.extend(ajlist)
        
        #uusjrj2[i][0].extend(uusjrj[i][0])
        #uusjrj2[i][1].extend({uusjrj[i][1:]})
    uusjrj2 = dict(uusjrj2)
    print("-----")
    print(uusjrj2)       
        #if JÄTKATA HOMME
    #for el in range(len(lapsjrj)):
        #vanemanimi = lapsjrj[el][0]
        #lapsnimi = {lapsjrj[el][1]}
        #if vanemanimi not in seosed:
            #seosed[vanemanimi] = lapsnimi
        #elif vanemanimi in seosed:
            #seosed[vanemanimi] = lapsnimi


    #print(seosed)
    #for vanem in range(len(lapsjrj)):
        
        
        
#vanused = {"Kersti": 46, "Jüri": 38, "Jevgeni": 30, "Mart": 67}
#kolmikud = ("Sofia", "Maria", "Kersti")
#for nimi in kolmikud:
    #if nimi not in vanused:
        #vanused[nimi] = 13
        
seosta_lapsed_ja_vanemad('lapsefail.txt', 'nimedefail.txt')
  #ÜLESANNE on koostada funktsioon seosta_lapsed_ja_vanemad, mis võtab esimeseks argumendiks laste faili nime ja teiseks argumendiks nimede faili nime, ning tagastab sõnastiku,
  #kus iga kirje võtmeks on lapsevanema nimi ja väärtuseks tema laste nimede hulk. Tagastatavas sõnastikus peavad esindatud olema kõik laste failis toodud suhted.
  #.split(None, 1)
  #for key, value in d.items():
  #set([3, 4]) → {3, 4}

  #loe järjendina sisse lapsed
  #loe sõnastikuna sisse nimed
  #for el in lapsed, lapsed[el][0] == nimed[lapsed[el][0]], lapsed_el_1 == nimed_lapsed_el_1 <- vanemad ja lapsed on nimed jrjndis
  #for el in lapsed, 
  #loo sonastik "seosed"

