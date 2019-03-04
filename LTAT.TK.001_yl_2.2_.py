bingoTabel = [[10, 16, 31, 46, 75],
              [11, 17, 32, 55, 68],
              [12, 18, 33, 49, 64],
              [13, 20, 34, 48, 65],
              [15, 30, 45, 60, 75]]

def on_bingo_tabel(list):
    x = 0
    for veerg in range(len(list[0])):
        for rida in range(len(list)):
            bingoarv = list[rida][veerg]
            if veerg == 0 and bingoarv in range(1,16):
                x += 0
            elif veerg == 1 and bingoarv in range(16,31):
                x += 0
            elif veerg == 2 and bingoarv in range(31,46):
                x += 0
            elif veerg == 3 and bingoarv in range(46,61):
                x += 0
            elif veerg == 4 and bingoarv in range(61,76):
                x += 0
            else:
                x += 1
                return False
    if x == 0:
        return True
on_bingo_tabel(bingoTabel)
print(on_bingo_tabel(bingoTabel))