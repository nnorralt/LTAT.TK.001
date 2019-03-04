fail = open(input("sisesta fail:"), encoding="UTF-8")
summad = []
reaarv = 0
for rida in fail:
    osad = rida.split()
    for osa in osad:
        reaarv += int(osa)
        #reaSumma.append(osa)
    #rida_sum = sum(reaSummad)
    summad.append(reaarv)
    reaarv = 0
suurim = max(summad)
suurim_index = int(summad.index(suurim)) + 1
print("Suurim summa on failis " + str(suurim_index) + ". real ja see on " + str(suurim) +".")
    
fail.close()