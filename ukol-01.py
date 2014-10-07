def druhe_mocniny(n):
    # Projdeme vsechna cisla od 1 do n (vcetne) a v kazdem pruchodu vypiseme
    # druhou mocninu aktualniho cisla.
    for i in range(1, n + 1):
        print i**2,
    print


def liche_a_dvojky(n):
    # Projdeme vsechna cisla od 1 do n (vcetne) a v kazdem pruchodu
    # zkontrolujeme, zda je aktualni cislo delitelne dvema. Pokud ano, vypiseme
    # 2, jinak aktualni cislo.
    for i in range(1, n + 1):
        if i % 2 == 0:
            print 2,
        else:
            print i,
    print


def specialni(n):
    #   1   1   2   4   7   13 ...
    #   |   |   \
    #   |    \   \
    #   |     \   dalsi_dalsi
    # aktualni \
    #          dalsi
    #
    # V kazde iteraci vypisu obsah promenne 'aktualni' a upravim obsah vsech
    # promennych pro dalsi iteraci.
    aktualni = 1
    dalsi = 1
    dalsi_dalsi = 2
    for i in range(n):
        print aktualni,
        stare_aktualni = aktualni
        aktualni = dalsi
        dalsi = dalsi_dalsi
        dalsi_dalsi = dalsi + aktualni + stare_aktualni
    print


def kriz(n):
    # Prochazim souradnice ctverce o strane (2 * n - 1) a pro kazdou souradnici
    # se rozhoduji, jestli vypsat mezeru nebo krizek. Krizek vypisu tehdy,
    # pokud se zrovna nachazim na uhlopricce.
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            if i == j or (2 * n - 2) - i == j:
                print '#',
            else:
                print ' ',
        print


def diamant(n):
    # Prochazim souradnice ctverce o strane (2 * n - 1) a pro kazdou souradnici
    # se rozhoduji, jestli vypsat mezeru nebo krizek. Pominka pro vypis krizku
    # se lisi, jestli se nachazim v dolni nebo horni polovine diamantu.
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            if i < n and j >= n - 1 - i and j <= n - 1 + i:
                print '#',
            elif i >= n and j > i - n and j < (2 * n - 2) - (i - n):
                print '#',
            else:
                print ' ',
        print
