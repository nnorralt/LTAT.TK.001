def seosta_lapsed_ja_vanemad(laps,nimi):
    lapsefail = open(laps, encoding="UTF-8")
    nimefail = open(nimi, encoding="UTF-8")
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
    uusjrj2 = dict(uusjrj2)
    return uusjrj2
