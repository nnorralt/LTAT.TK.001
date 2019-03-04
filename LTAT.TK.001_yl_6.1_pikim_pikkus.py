pikimArv = 0 #muutuja millesse akumuleerida
def pikim_pikkus(struktuur):
    global pikimArv #deklareerime
    if pikimArv <= len(struktuur): #kui struktuur on väiksem siis ei muuda, kui on suurem siis ta saab uueks pikimaks arvuks
        pikimArv = len(struktuur)
    for element in struktuur: #itereerime läbi listi
        if isinstance(element, list): #kui element on list siis,
            if len(element) > pikimArv: #vaatame kas listi pikkus on suurem kui hetkel arvukaim järjend
                pikimArv = len(element) #kui on siis muudame ära uueks pikimArvuks
            pikim_pikkus(element) #ja otsime järjekordsest järjendist ülesse selle pikkuse ning võrdleme seni olnuga
        else:
           pass
    return pikimArv