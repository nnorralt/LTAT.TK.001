
import pandas as pd #impordin pandas andmetöötluslibrary


def taienda_tabelit(andmedfail): #defineerin tabelitäiendusfunktsiooni esimesena, sest teda on vaja kasutada järgmise funktsiooni sees
    eemaldatud = andmedfail.pop('2012') #viskan veeru(kolonni) 2012 minema, tegelikult salvestub argumendina "eemaldatud" alla
    andmedfail['Keskmine'] = andmedfail.mean(axis=1) #kasutan üldist käsklust, et ridade (rows) keskmised võtta mean() funktsiooniga ja panna uue "keskmine" veeru alla
    return andmedfail #tagastan muudetud andmedfaili, et kasutada edasi funktsioonis raamatukogud()
def raamatukogud(andmed): #kasutan argumendiga andmete failinime sisaldavat muutujat, et töödelda andmeid seal sees
    andmedfail = pd.read_csv(andmed, delimiter=';', index_col=' ') #loeme pandasesse sisse andmed, eeldades, et nad on eraldatud semikooloni ";"-ga. indexcol muudab
    #esimese veeru rea pealkirjadeks.
    andmedfail = pd.DataFrame(andmedfail) #muudame need andmed dataFrameks, et töödelda paremini Pandase käsklustega
    taienda_tabelit(andmedfail) #rakendame täiendusfunktsiooni, argumendina dataFrame ("andmeFreim")
    print(andmedfail) #printisime lihtsalt et kontrollida andmeid
    andmedfail.to_csv(andmed.strip('.csv') + '_uus.csv', sep=';', encoding='utf-8') #salvestame faili uuena, kasutades andmete failinime algset kuju ja lisades
    #_uus sinna juurde, endiselt eraldades ";"-ga
    print(andmedfail) #prindime et kontrollida
