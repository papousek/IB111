# Člověče, nezlob se

## Simulátor
Udělejte simulátor jednoduché hry stylu "Člověče, nezlob se":
- Hraje se na hracím plánu velikosti N.
- Háže se kostkou (1-6), když padne 6, tak se háže znova.
- Figurka se posunuje o tolik polí, kolik padlo.
- Hra končí, když dorazíme na poslední pole. Je nutné se trefit přesně na poslední pole (pokud se netrefíme, tak figurka stojí).

## Analýza hry
Napište program, který vypočítá průměrnou délku hry na plánu velikosti N. Pomocí programu určete průměrnou délku hry pro plány o velikosti 1-50 (do řešení přiložte výpis hodnot).

## Kostra řešení

```python
# Simuluje hru "Clovece, nezlob se". Napriklad
# >>> hra_kostky(20)
#
# V 1. kole padlo 6 5
# Jsem na pozici 11
# V 2. kole padlo 6 5
# Jsem na pozici 11
# V 3. kole padlo 4
# Jsem na pozici 15
# V 4. kole padlo 2
# Jsem na pozici 17
# V 5. kole padlo 5
# Jsem na pozici 17
# V 6. kole padlo 4
# Jsem na pozici 17
# V 7. kole padlo 5
# Jsem na pozici 17
# V 8. kole padlo 2
# Jsem na pozici 19
# V 9. kole padlo 4
# Jsem na pozici 19
# V 10. kole padlo 3
# Jsem na pozici 19
# V 11. kole padlo 6 2
# Jsem na pozici 19
# V 12. kole padlo 6 3
# Jsem na pozici 19
# V 13. kole padlo 1
# Jsem na pozici 20
# Hra dokoncena v 13. kole
def simulator(n):
    pass

# Vypocita prumerny pocet kol nutny k dohrani hry na planu
# o velikosti `n`. Napriklad:
# >>> analyza(20, 1000)
#
# Prumerny pocet kol: 10.3
def analyza(n, pocet_opakovani):
    pass
```
