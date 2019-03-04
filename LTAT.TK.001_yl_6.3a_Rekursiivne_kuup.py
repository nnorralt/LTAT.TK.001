
kuup_jarj = [] #võtan välja et akumuleerida
def kuup(jarj):
    if len(jarj) == 0: #kui  on algne list lõppenud siis väljastan uue listi
        return kuup_jarj
    kuup_jarj.append(jarj.pop(0)** 3) #iga korraga võtan esimese, lükkan kuupi, eemaldan järjendist ja lisan akusse
    return kuup(jarj) #kui algne list pole lõppenud siis järjest kordan rekursiooni