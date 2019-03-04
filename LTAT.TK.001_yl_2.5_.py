maatriks = [['ab', "abcd",'cd', 'cd'], ['a', 'bad', 'bd']]

def leidub_anagramm(maatriks):
 for li in range(len(maatriks)): #võtab listist elemendi nr
     for sone in range(len(maatriks[li])): #võtab elemendist sonede nr (4)
         for taht in range(len(maatriks[li][sone])): #võtab sõnest(nt sone[2]) sõnede pikkuse                         
             if 'a' is str(maatriks[li][sone][taht-1]):
                 pass
             elif 'b' is str(maatriks[li][sone][taht-1]):
                pass
             elif 'c' is str(maatriks[li][sone][taht-1]):
                pass
             elif 'd' is str(maatriks[li][sone][taht-1]):
                pass
             else:
                maatriks[li][sone] = ""

 for nimekiri in range(len(maatriks)):
    if len(maatriks[nimekiri]) < 3:
        s = maatriks[nimekiri][nimekiri]
        t = maatriks[nimekiri][nimekiri+1]
        if "".join(sorted(s)) == "".join(sorted(t)):
            return True
        else:
            pass
    if len(maatriks[nimekiri]) >= 3:
        for asonad in range(len(maatriks[nimekiri])):
            if asonad != 0 and asonad != (len(maatriks[nimekiri])-1):
                keskmine = maatriks[nimekiri][asonad]
                sona1 = maatriks[nimekiri][asonad+1]
                sona2 = maatriks[nimekiri][asonad-1]
                if "".join(sorted(keskmine)) == "".join(sorted(str(sona1) + str(sona2))):
                    return True            
            if asonad == 0:
                a = maatriks[nimekiri][asonad]
                b = maatriks[nimekiri][asonad+1]
                if "".join(sorted(a)) == "".join(sorted(b)):
                   return True
            if asonad == (len(maatriks[nimekiri])-1):
                x = maatriks[nimekiri][asonad]
                y = maatriks[nimekiri][asonad-1]
                if "".join(sorted(x)) == "".join(sorted(y)):
                    return True


     #if a b c d not in maatriks 

leidub_anagramm(maatriks)