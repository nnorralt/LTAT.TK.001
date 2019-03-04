sona = "arvamusliider"

def symbolite_sagedus (sona):
    sonastik = {}
    for mark in sona:
        sonastik[mark] = sona.count(mark)
    return sonastik
symbolite_sagedus(sona)