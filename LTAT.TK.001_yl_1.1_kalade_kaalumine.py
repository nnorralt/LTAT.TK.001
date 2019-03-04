def kala_kaal(rida, kalaTysedus):
    kalaKaal = ((round(rida)**3)*float(kalaTysedus))/100
    return round(kalaKaal)


fail = input('sisesta kala fail')

f = open(fail, encoding="UTF-8")
eestifail = pd.read_csv(andmed.strip(""), sep=';')

alamMoot = round(float(input('sisesta alammõõt')))
kalaTysedus = float(input('sisesta kala tüsedusindeks'))

heaKala = []
for rida in f:
    rida = float(rida)
    if rida < alamMoot:
        print("Kala lasti vette tagasi")
    else:
        print(kala_kaal(rida, kalaTysedus))
        heaKala.append(kala_kaal(rida, kalaTysedus))
f.close()
print(round(max(heaKala)/1000,3))