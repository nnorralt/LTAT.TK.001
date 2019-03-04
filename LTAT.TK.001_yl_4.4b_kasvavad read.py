

def on_kasvav(rida):
    if len(rida) <= 0:
        return 0
    if len(rida) > 0:
        kasvav = True
        eelmine = rida[0]
        for ridaelement in rida[1:]:
            if ridaelement <= eelmine:
                return 0
            eelmine = ridaelement
        if kasvav:
            return 1


#muuda alljärgnevale funktsioon juurde
jarjend_ruudus = [[4, 3, 2], [-1, 0], [-2,0,4,5,6],[2,5,2,5]]

kasvavaid = 0
for rida in jarjend_ruudus:
    kasvavaid += on_kasvav(rida)
    
print("Kasvavaid ridu on " + str(kasvavaid))