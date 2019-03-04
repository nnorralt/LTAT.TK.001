#järjendit vaja kasutada
#siin kasutada materjalist välja toodud dokumentatsiooni - hulkade võrdluse meetodeid. ja seejärel
#min-max selle peale kelle lubadused enim kattuvad jne? või siis mingit muud meetodit


erakond_1 = {"lastetoetusi tõsta", "1", "pensione tõsta", "tulumaksu langetada", "kaitsekulutusi tõsta"}
erakond_2 = {"muuta kõike varasemat"}
erakond_3 = {"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"}
erakond_4 = set()
erakond_5 = {"väljarännet piirata", "pensione tõsta", "õpetajate palku tõsta", "kaitsekulutusi tõsta", "alkoholiaktsiisi tõsta"}

def kooslubajad(erakonnad=[{"lastetoetusi tõsta", "pensione tõsta", "tulumaksu langetada", "kaitsekulutusi tõsta", "1","2","3","4","5"},
                           {"muuta kõike varasemat","1","2","3","4","5"},{"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"},
                           {"väljarännet piirata", "pensione tõsta", "õpetajate palku tõsta", "kaitsekulutusi tõsta",
                              "alkoholiaktsiisi tõsta"}]):
    erakonnaindeksid = []
    erakonnaennik = tuple()
    maxyhisosa = 0
    yhisindeks1 = 0
    yhisindeks2 = 0
    for erakond in range(len(erakonnad)):
        for jargmine in range(erakond+1,len(erakonnad)):
            if len(erakonnad[erakond] & erakonnad[jargmine]) > maxyhisosa:
                yhisindeks1 = erakond
                yhisindeks2 = jargmine
                maxyhisosa = len(erakonnad[erakond] & erakonnad[jargmine])
            if len(erakonnad) == 2:
                yhisindeks1 = 1
                yhisindeks2 = 0
                
    erakonnaindeksid.append(yhisindeks1)
    erakonnaindeksid.append(yhisindeks2)
    erakonnaennik = tuple(erakonnaindeksid)
    return erakonnaennik
print(kooslubajad(erakonnad=[{'kuritegevust vähendada', 'rajada spordiväljakud igasse linna', 'kõiki toetusi suurendada', 'algatada koduloometoetus', 'suurendada kõiki palkasid', 'kaotada kõik maksud'},
                             {'edendada maaelu', 'vähendada suremust', 'toetada pensionäre', 'aidata noorperesid', 'suurendada vastsündinute arvu'}]))