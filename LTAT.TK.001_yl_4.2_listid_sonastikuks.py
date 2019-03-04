
def listid_sonastikuks(jarjend1, jarjend2):
    sonastik = {} #loon sõnastiku funktsiooni tarbeks
    sonastikujarjend = [] #loon jarjendi millest hiljem loon sonastiku
    for voti in range(len(jarjend1)): #võtmejärjendi väärtustest liigun läbi
        paarjarjend = [] #teen järjendi paaride jaoks iga for-tsükliga
        paarjarjend.append(jarjend1[voti]) #lisan paari järjendisse võtme
        paarjarjend.append(jarjend2[voti]) #lisan paari järjendisse väärtuse
        ennik = tuple(paarjarjend) #annan uuele ennikule väärtuse mis on võtme-väärtus paar
        sonastikujarjend.append(ennik) #lisan sonastikujarjendile ennikuid iga tsükliga
    sonastik = dict(sonastikujarjend)
    return sonastik

        
