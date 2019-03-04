
lst = [] #teen järjendi funktsiooni tarbeks (funktsiooni sees kirjutatakse see lihtsalt üle iga rekursiooniga
def paarissumma(n): 
    if n < 2: #kuna kaks on väikseim positiivne paaris täisarv, siis alla selle rekursiooniga minnes on BAAS ja väljastatakse
        pass#return print(sum(lst)) #peame järjendi summa väljastama
    if (n % 2) == 0 and n >= 2: #kui on paarisarv ja väiksem või võrdne kahega ( 2 puhul lisab selle ja jrg korral returnib BAASiga)
        lst.append(n) #paarisarv järjendisse juurde
        paarissumma(n-2) #rekursioon kordub, argumendiks järgmine paarisarv (väiksem)
    elif (n % 2) != 0 and n > 2: #kui on paaritu arv algargumendiks läheb see if käiku
        lst.append(n-1) #lisatakse esimene paarisarv järjendile (1 võrra väiksem paarituarvust mis on argumendiks)
        paarissumma(n-2) #kordame 2 võrra väiksema paarituarvuga
    return sum(lst) #RÕVE on see return sellepärast, et ta kordab seda returni väga palju. aga kontroll võttis vastu.
