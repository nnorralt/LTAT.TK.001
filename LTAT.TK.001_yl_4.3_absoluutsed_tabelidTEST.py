

def absolutiseeri_tabel(kahendjarjend):
    absoluutjarjend = [] #loon jarjendi millega asendan
    for moode1 in range(len(kahendjarjend)): #loon jarjendi elemente läbiva tsükli
        absoluutalljarjend = [] #nullin alltsüklijarjendi ära nüüd kui returnitavale järjendile on element lisatud
        for moode2 in range(len(kahendjarjend[moode1])): #loon jarjendi elementide elemente läbiva tsükli
            absoluutalljarjend.append(abs(kahendjarjend[moode1][moode2])) #lisan järjest elemente alltsüklitele
        absoluutjarjend.append(absoluutalljarjend) #lisan return järjendile oma alljärjendi elemendina
    kahendjarjend = absoluutjarjend
    print(kahendjarjend)
absolutiseeri_tabel([[-42]])
