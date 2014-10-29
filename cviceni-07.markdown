# Project Euler

[Project Euler](http://projecteuler.net) je stránka obsahující mnoho zajímavých
úkolů, pro jejichž vyřešení je potřeba něco naprogramovat. Zkuste si vyřešit
například následující úlohu.

## Problem 12: Highly divisible triangular number

Sekvence trigangulárních čísel je generovaná postupným sčítáním přirozených
čísel. Sedmé triangulární číslo je tedy `1 + 2 + 3 + 4 + 5 + 6 + 7 = 28`.
Prvních deset takových čísel by bylo:

```
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
```

Podívejme se na prvočíselný rozklad prvních sedmi triangulárních čísel:

```
 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
```

Je vidět, že `28` je první triangulární číslo, které má pět prvočinitelů.

Dokážete najít první triangulární číslo, jehož prvočíselný rozklad obsahuje 500
prvočinitelů?

# Pascalův trojúhelník

Až budete mít naimplemntované funkce pro výpočet Pascalova trojúhelníka, můžete použít následující funkci pro jeho výpis:

```python
# >>> pascal_vypis([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
#
#      1
#     1  1
#   1  2  1
#  1  3  3  1
def pascal_vypis(patra):
    size = len(str(patra[len(patra)-1][len(patra)/2]))+2
    for radek in patra:
        line = ""
        for x in radek:
            line += ("{0: ^" + str(size) + "}").format(x)
        print ("{0: ^" + str(size * n) + "}").format(line)
```

## Kombinační čísla

Napište funkci, která vrátí `n` pater Pascalova trojúhelníka za využití výpočtu
kombinačního čísla v podobě seznamu pater, kde každé patro je seznam celých
čísel

```
>>> pascal_kombinacne(4)

[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
```

Kostra řešení:

```python
# Vrati n!
def faktorial(n):
    pass

# Vrati hodnotu kombinacniho cisla 'n nad k'.
def kombinacni_cislo(n, k):
    pass

# Vrati dany pocet radku Pascalova trojuhelnika za vyuziti vypoctu
# kombinacniho cisla
def pascal_kombinacne(n):
    pass
```

## Iterační přístup

Napište opět funkci pro výpočet řádků Pascalova trojuhelnika, tentokrát ale za
použití iterativního přístupu, kde se pro výpočet čísla na řádku používají
hodnoty z řádku předchozího.

```python
# Vrati dany pocet radku Pascalova trojuhelnika za vyuziti
# iterativniho pristupu.
def pascal_iteracne(n):
    pass
```

# Řadící algoritmy

V praxi se používají zabudované funkce `list.sort` a `sorted`, viz. [referenční
manuál](http://docs.python.org/2/howto/sorting.html#key-functions).

Pro snazší testování správnosti řadících algoritmů si napište funkci, která
vygeneruje seznam dané délky obsahující náhodná čísla z daného rozsahu.

```python
>>> nahodny_seznam(delka, rozsah)

[2, 8, 14, 7, 13, 7, 4, 20]
```

Naimplementujte sami funkce pro řazení podle následujících algoritmů:

  * řazení výběrem (selection sort)
  * řazení vkládáním (insertion sort)
  * řazení výměnou (bubble sort)

```
def razeni_vyberem(seznam): ...

>>> s = [5, 4, 3, 2, 1]
>>> razeni_vyberem(s)
>>> print s
>>> [1, 2, 3, 4, 5]
```

## Řazení podle klíče

Přečtěte si část referenčního manuálu o [řazení podle vlastního
klíče](https://docs.python.org/2/howto/sorting.html#key-functions)
a napište funkce pro řazení seznamu slov podle následujících kriteríí:

  * vzestupně podle jejich délky
  * sestupně podle jejich délky
  * abecedně, ale pouze podle písmen na lichých pozicích

## Rychlé řadící algoritmy

Implementujte některé rychlé řadící algoritmy, např. Quick sort (řazení
rozdělováním) nebo Merge sort (řazení slučováním).

### Analýza rychlosti řadících algoritmů

Proveďte analýzu všech naimplementovaných řadících algoritmů &ndash; jak
výpočtem, tak experimentálně. Buď můžete vaše funkce doplnit o počítání
provedených elementárních operací (porovnávání a přiřazení) nebo prostě měřit
čas nutný k seřazení velkých polí pomocí `time.time()`. Napište si pomocné
funkce pro generování polí zadané délky (a s různými vlastnostmi: úplně
náhodné, téměř seřazené, obrácená posloupnost) a zkoušejte, u kterých
algoritmů se tyto vlastnosti seznamu projeví. Porovnejte svoje algoritmy i
s vestavěnou metodou `list.sort()`.

