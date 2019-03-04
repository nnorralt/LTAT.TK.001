
def on_rahulik(arvamus1, arvamus2, erinevus): #määrab ära kas kaks inimest on rahulikud
    if abs(arvamus1 - arvamus2) <= erinevus or arvamus1 * arvamus2 >= 0: #kui arvamuste erinevus on absoluutarvuna sama suur
        #või väiksem kui lubatud erinevus argument või need erinevused on positiivsed siis on rahulik vestlus
        return True
    return False #kui ei vasta nõuetele on hoopis mitterahulik

def dissonantside_arv(arvamused, lubatud_erinevus): #kogub dissonantsvestlusi
    dissonantsid = 0 #algselt on muutuja 0
    for i in range(len(arvamused)): #liigume läbi järjendi
        if i != (len(arvamused)-1) : #läheb käiku, kui ei ole kasutuses viimane arvamus järjendis
            if not on_rahulik(arvamused[i], arvamused[i+1], lubatud_erinevus): #kui pole funktsiooni järgi rahulik vestlus
                #siis lisandub 1 dissonantsile ja algab uuesti tsükkel
                dissonantsid += 1
    return dissonantsid
