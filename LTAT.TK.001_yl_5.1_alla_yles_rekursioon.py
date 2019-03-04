lst1 = []
lst2 = []
def alla_ules(n):
    if n <= 0:
        print("Põhi!")
    if (n % 2) == 0 and n != 0:
        lst1.append(n)
        print(n)
        alla_ules(n - 2)
        if (n-2) == 0:
            lst2.append(1)
            print(lst2[0])
        if len(lst1) != len(lst2): #mul on siin vaja leida: kuidas mitte näidata viimast paaritut arvu, mis on suurem argumendist (8+1=9)
            print(n + 1)
            lst2.append(n+1)
    elif (n % 2) != 0 and n >= 0:
        lst1.append(n)
        print(n)
        alla_ules(n - 2)
        if (n-2) < 0:
            lst2.append(0)
            print(lst2[0])
        if len(lst1) != len(lst2):
            print(n+1) #mul on siin vaja leida: kuidas mitte näidata viimast paaris arvu, mis on suurem argumendist ()
            lst2.append(n+1)
