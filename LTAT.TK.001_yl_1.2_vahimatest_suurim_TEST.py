
a = [[1, 2],
     [1, 0]]
vaikseimad = []
suurim = True
def vahimatest_suurim(nimekiri):
    for element in nimekiri:


        vaikseimad.append(min(element))
        if min(element) == max(vaikseimad):
            suurim = min(element)
    return suurim
print (str(vahimatest_suurim(a)))
    
            
        
        
    