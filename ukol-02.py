from random import randint


def kostka():
    hod = randint(1, 6)
    vysledek = [hod]
    while hod == 6:
        hod = randint(1, 6)
        vysledek.append(hod)
    return vysledek


def simulator(n, vypis=True):
    pozice = 0
    kolo = 0

    while pozice < n:
        kolo += 1
        hod = kostka()
        hod_suma = sum(hod)
        if pozice + hod_suma <= n:
            pozice += hod_suma
        if vypis:
            print 'V ' + str(kolo) + '. kole padlo ' + ' '.join(map(str, hod))
            print 'Jsem na pozici', pozice
            if pozice == n:
                print 'Hra dokoncena v ' + str(kolo) + '. kole'
    return kolo


def analyza(n, pocet_opakovani):
    celkem = 0.0
    for i in range(pocet_opakovani):
        celkem += simulator(n, vypis=False)
    print 'Prumerny pocet kol:', float(celkem) / pocet_opakovani


"""
for i in range(50):
    print 'Plan velikosti ' + str(i + 1) + ':', analyza(i + 1, 1000)

Plan velikosti 1: Prumerny pocet kol: 5.963
Plan velikosti 2: Prumerny pocet kol: 6.155
Plan velikosti 3: Prumerny pocet kol: 5.67
Plan velikosti 4: Prumerny pocet kol: 6.056
Plan velikosti 5: Prumerny pocet kol: 6.032
Plan velikosti 6: Prumerny pocet kol: 7.202
Plan velikosti 7: Prumerny pocet kol: 7.156
Plan velikosti 8: Prumerny pocet kol: 7.515
Plan velikosti 9: Prumerny pocet kol: 7.561
Plan velikosti 10: Prumerny pocet kol: 7.841
Plan velikosti 11: Prumerny pocet kol: 8.028
Plan velikosti 12: Prumerny pocet kol: 8.199
Plan velikosti 13: Prumerny pocet kol: 8.7
Plan velikosti 14: Prumerny pocet kol: 8.847
Plan velikosti 15: Prumerny pocet kol: 9.176
Plan velikosti 16: Prumerny pocet kol: 9.489
Plan velikosti 17: Prumerny pocet kol: 9.784
Plan velikosti 18: Prumerny pocet kol: 9.888
Plan velikosti 19: Prumerny pocet kol: 9.886
Plan velikosti 20: Prumerny pocet kol: 10.429
Plan velikosti 21: Prumerny pocet kol: 10.647
Plan velikosti 22: Prumerny pocet kol: 10.971
Plan velikosti 23: Prumerny pocet kol: 10.977
Plan velikosti 24: Prumerny pocet kol: 11.129
Plan velikosti 25: Prumerny pocet kol: 11.417
Plan velikosti 26: Prumerny pocet kol: 12.132
Plan velikosti 27: Prumerny pocet kol: 11.871
Plan velikosti 28: Prumerny pocet kol: 12.369
Plan velikosti 29: Prumerny pocet kol: 12.673
Plan velikosti 30: Prumerny pocet kol: 12.881
Plan velikosti 31: Prumerny pocet kol: 12.636
Plan velikosti 32: Prumerny pocet kol: 13.371
Plan velikosti 33: Prumerny pocet kol: 13.214
Plan velikosti 34: Prumerny pocet kol: 13.235
Plan velikosti 35: Prumerny pocet kol: 13.788
Plan velikosti 36: Prumerny pocet kol: 14.117
Plan velikosti 37: Prumerny pocet kol: 14.504
Plan velikosti 38: Prumerny pocet kol: 14.866
Plan velikosti 39: Prumerny pocet kol: 14.79
Plan velikosti 40: Prumerny pocet kol: 15.021
Plan velikosti 41: Prumerny pocet kol: 15.328
Plan velikosti 42: Prumerny pocet kol: 15.447
Plan velikosti 43: Prumerny pocet kol: 15.91
Plan velikosti 44: Prumerny pocet kol: 15.805
Plan velikosti 45: Prumerny pocet kol: 16.145
Plan velikosti 46: Prumerny pocet kol: 16.492
Plan velikosti 47: Prumerny pocet kol: 16.682
Plan velikosti 48: Prumerny pocet kol: 17.037
Plan velikosti 49: Prumerny pocet kol: 17.262
Plan velikosti 50: Prumerny pocet kol: 17.326
"""
