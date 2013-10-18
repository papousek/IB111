Pirátské lodi se podařilo ukořistit poklad čítající 1000 zlatých mincí. Poklad
má být rozdělen mezi 5 pirátů s ohledem na jejich šarži (1, 2, 3, 4, 5). Piráty
můžeme charakterizovat jako nekonečně prohnané, krvelačné a chamtivé.  Začínáme
od piráta 5 a jdeme k 1. Každý z nich může učinit nabídku, jak rozdělit poklad
mezi ostatní piráty. Buď je tento návrh přijat nebo je navrhovatel vyhozen přes
palubu do moře plného žraloků. Za přijatý návrh se považuje právě ten, na
kterém se shodne většina z těch pěti pirátů.  Jakou nabídku by tedy měl pirát 5
předložit?

# Seznamy

Napište ekvivalenty následujících standardních operací:
- `min(seznam)`,
- `max(seznam)`,
- `sum(seznam)`,
- `prvek in seznam`

# Řetězce

Nejprve si vyzkoušejte, jak se vyhodnotí v konzoli následující výrazy:

```python
"kos" * 3
"petr" + "klic"

s = "velbloud"
s[0]
s[2]
s[-1]
len(s)
s[:3]
s[3] = "k"

s = s[:3] + "k" + s[3:]

ord('a')
ord('b')
chr(99)
```

## Vycpávky

Napište funkci, která mezi písmena daného textu vloží libovolný text.

### Kostra řešení

```python
# Vlozi mezi pismena daneho textu vycpavku, napriklad:
# >>> vycpavky("pampeliska", "XX")
#
# >>> "pXXaXXmXXpXXeXXlXXiXXsXXkXXa"
def vycpavky(text, vycpavka):
    pass
```

## Caesarova šifra

Napište funkci, která zašifruje text tak, že posune všechna jeho písmena v abecedě o 3 dopředu
(cyklicky), můžete se inspirovat [popisem Caesarovy šifry](http://cs.wikipedia.org/wiki/Caesarova_%C5%A1ifra).

### Kostra řešení

```python
# Posune text o 3 pismena v abecede dopredu, napriklad:
# >>> caesar("zirafa")
#
# >>> "cludid"
def caesar(text):
    pass
```

## Vigenèrova šifra

Napište funkci, která zašifruje text podle předem daného klíče. Pro posun písmen zdrojového textu
se postupně používají písmena z klíče. Pokud je klíč kratší než zdrojový text, jsou použita písmena
z klíče opět od začátku. Můžete se inspirovat [Vigenèrovy šifry](http://cs.wikipedia.org/wiki/Vigen%C3%A8rova_%C5%A1ifra).

### Kostra řešení

```python
# Posune pismena v textu o tolik, kolik udava klic
# ('a' posouva o 0, 'b' o 1, ..., 'z' o 25), napriklad
# >>> vigener("pampeliska", "klic")
#
# >>> "zlurowquul"
def vigenere(text, klic):
    pass
```

## Prohazovací šifra

Napište funkci, která zašifruje text tak, že prohází jeho písmana ob daný počet.

```python
# Prohazi pismena danehe textu tak, ze se da cist ob 'n', napriklad
# >>> prohazej("heslojeprase", 3)
#
# >>> "horejaseslpe"
def prohazej(text, n):
    pass
```

## Dešifrovací funkce

Napište k předchozím šifrám i funkce, které daný zašifrovaný text dešifrují.

## Vyhledávání

Napište funkci, která vrátí počet výskytu daného slova v textu.

```python
# Vrati pocet vyskytu daneho slova v textu, napriklad:
# >>> hledej("ahoj svete, ahoj, ahoj, ahoj", "ahoj")
#
# >>> 4
def hledej(text, co):
    pass
```
