from random import sample

def juhuslik_bingo():
    veerg1 = list(sample(range(1, 16), 5))
    veerg2 = list(sample(range(16, 31), 5))
    veerg3 = list(sample(range(31, 46), 5))
    veerg4 = list(sample(range(46, 61), 5))
    veerg5 = list(sample(range(61, 76), 5))
    bingotabel = []
    bingorida1 = []
    bingorida2 = []
    bingorida3 = []
    bingorida4 = []
    bingorida5 = []
    
    for rida in range(5):
        for veerg in range(5):
            if veerg == 0:
                if rida == 0:
                    bingorida1.append(veerg1[rida])
                elif rida == 1:
                    bingorida2.append(veerg1[rida]) 
                elif rida == 2:
                    bingorida3.append(veerg1[rida])
                elif rida == 3:
                    bingorida4.append(veerg1[rida])
                elif rida == 4:
                    bingorida5.append(veerg1[rida])
            elif veerg == 1:
                if rida == 0:
                    bingorida1.append(veerg2[rida])
                elif rida == 1:
                    bingorida2.append(veerg2[rida]) 
                elif rida == 2:
                    bingorida3.append(veerg2[rida])
                elif rida == 3:
                    bingorida4.append(veerg2[rida])
                elif rida == 4:
                    bingorida5.append(veerg2[rida])
            elif veerg == 2:
                if rida == 0:
                    bingorida1.append(veerg3[rida])
                elif rida == 1:
                    bingorida2.append(veerg3[rida]) 
                elif rida == 2:
                    bingorida3.append(veerg3[rida])
                elif rida == 3:
                    bingorida4.append(veerg3[rida])
                elif rida == 4:
                    bingorida5.append(veerg3[rida])
            elif veerg == 3:
                if rida == 0:
                    bingorida1.append(veerg4[rida])
                elif rida == 1:
                    bingorida2.append(veerg4[rida]) 
                elif rida == 2:
                    bingorida3.append(veerg4[rida])
                elif rida == 3:
                    bingorida4.append(veerg4[rida])
                elif rida == 4:
                    bingorida5.append(veerg4[rida])
            elif veerg == 4:
                if rida == 0:
                    bingorida1.append(veerg5[rida])
                elif rida == 1:
                    bingorida2.append(veerg5[rida]) 
                elif rida == 2:
                    bingorida3.append(veerg5[rida])
                elif rida == 3:
                    bingorida4.append(veerg5[rida])
                elif rida == 4:
                    bingorida5.append(veerg5[rida])
    bingotabel.append(bingorida1)
    bingotabel.append(bingorida2)
    bingotabel.append(bingorida3)
    bingotabel.append(bingorida4)
    bingotabel.append(bingorida5)
    return bingotabel