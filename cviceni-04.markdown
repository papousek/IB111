Vě vězení se nachází 100 samotek a na každé z nich je "ubytován" jeden vězeň.
Každá cela je bez oken a nepronikne tam žádný hluk zvenčí. Uprostřed mezi všemi
celami se nachází centrální kruhový obývací pokoj. Na stopě visí dvě žárovky,
jejichž stav je na začátku neznámý. Žádný z vězňů nemůže světlo z těchto
žárovek ze své cely spatřit.  Čas od času (ne nutně každý den) vybere dozorce
jednoho vězně (náhodně s rovnoměrným rozložením) a pustí ho na celý den do
centrální místnosti. Na konci dne se zase musí vrátit do své cely. Mezitím si
může hrát s vypínači na stěně a zapínat a vypínat žárovky.  Navíc má na konci
dne možnost prohlásit, že už se v centrální místnosti vystřídalo všech 100
vězňů. Když bude mít pravdu, všechny je propustí, ale když se bude mýlit,
všechny je popraví. Proto si musí být 100% jistý.

Ještě než tato procedůra začne, mají se možnost vězňové mezi sebou domluvit
venku na nádvoří (ne v té centrální místnosti).  Za kolik dnů nejméně se mohou
všichni vězňové osvobodit?


# Náhodná čísla

Budeme pracovat s modulem `random`, jehož podrobný popis najdete v [referenčím manuálu](http://docs.python.org/2/library/random.html).

## Průměr / Maximum / Minimum

Napiště funkci, která vygeneruje `n` čísel z daného rozsahu `[a,b]` a zjistí:

 - průměr čísel
 - největší číslo
 - nejmenší číslo

### Řešení
```python
from random import randint

def nahodna_cisla(kolik, spodni_mez = 0, horni_mez = 100):
    minimum = horni_mez + 1
    maximum = spodni_mez - 1
    soucet = 0
    for i in range(kolik):
        x = randint(spodni_mez, horni_mez)
        print x,
        if x < minimum: minimum = x
        if x > maximum: maximum = x
        soucet += x
    print
    print "Minimum:", minimum
    print "Maximum:", maximum
    print "Prumer:", float(soucet) / kolik
```
## Opilec

Opilec je na půl cesty mezi domovem a hospodou, každý krok udělá náhodně jedním směrem.

1. Napiště funkci, která bude simulovat opilcův pohyb a v parametrech bere vzdálenost mezi domovem a hospodou a délku simulace (počet sledovaných kroků). Funkce skončí, pokud opilec dojde domů nebo do hospody.

2. Napiště funkci, která provede daný počet simulací opilcovi procházky a vrátí úspěšnost dojití domů.

### Kostra řešení

```python
from random import randint

# Vypise stav simulace, napriklad
# >>> vypis_radek(10, 6)
#
# doma . . . . . * . . . . hospoda
def vypis_radek(delka, poloha):
    pass

# Provede simulaci opilcova pohybu, napriklad
# >>> opilec(10, 100)
#
# doma . . . . . * . . . . hospoda
# doma . . . . * . . . . . hospoda
# doma . . . * . . . . . . hospoda
# doma . . . . * . . . . . hospoda
# doma . . . * . . . . . . hospoda
# doma . . . . * . . . . . hospoda
# doma . . . * . . . . . . hospoda
# doma . . * . . . . . . . hospoda
# doma . * . . . . . . . . hospoda
# doma . . * . . . . . . . hospoda
# doma . . . * . . . . . . hospoda
# doma . . * . . . . . . . hospoda
# doma . . . * . . . . . . hospoda
# doma . . * . . . . . . . hospoda
# doma . . . * . . . . . . hospoda
# doma . . . . * . . . . . hospoda
# doma . . . . . * . . . . hospoda
# doma . . . . * . . . . . hospoda
# doma . . . . . * . . . . hospoda
# doma . . . . * . . . . . hospoda
# doma . . . . . * . . . . hospoda
# doma . . . . . . * . . . hospoda
# doma . . . . . * . . . . hospoda
# doma . . . . . . * . . . hospoda
# doma . . . . . . . * . . hospoda
# doma . . . . . . . . * . hospoda
# doma . . . . . . . . . * hospoda
# doma . . . . . . . . * . hospoda
# doma . . . . . . . . . * hospoda
# doma . . . . . . . . . . hospoda
# Dosel do hospody.
def opilec(delka, pocet_kroku):
    pass

# Provede simulaci opilcova pohybu (nevypisuje nic na obrazovku)
# a vrati True, pokud se opilcovi podarilo dojit domu.
def opilec_dosel_domu(delka, pocet_kroku):
    pass

# Provede dany pocet simulaci opilcova pohybu a vypise
# procentualni uspesnost dojiti domu, napriklad:
# >>> analyza_opilce(100, 10, 100)
#
# Procento dojiti domu: 45.9
def analyza_opilce(n, delka, pocet_kroku):
    pass
```

## Průměrná vzdálenost dvou bodů ve čtverci

Napište funkci, která náhodně zvolí dva body ze čtverce dané velikosti a vrátí jejich vzdálenost. Následně
napište funkci, která tento výběr bude opakovat a vypíše průměrnou vzdálenost.

## Odhad čísla PI

Naprogramujte funkci využívající náhodná čísla pro odhad čísla PI, inspirovat se můžete [zde](http://math.fullerton.edu/mathews/n2003/montecarlopimod.html).

Shrnutí algoritmu:
- vygenerujte `n` náhodných bodů ze čtverce o straně `a`
- z vygenerovaných `n` bodů leží `m` v kruhu, který je vepsán do čtverce
- obsah čtverce je `a^2`
- obsah kruhu je `PI * (a/2)^2`
- odhad `PI`: `PI = 4 * (m/n)`
