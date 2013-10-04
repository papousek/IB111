30 vězňů má být následujícího dne popraveno. Popravčí jim ale chce dát
příležitost, aby se mohli někteří z nich zachránit. V den popravy budou stát v
zástupu tak, že první uvidí zbylých 29, druhý zbylých 28,... Všichni budou mít
na hlavě náhodně rozdělené bílé a černé klobouky, na které si neuvidí. Popravčí
přistoupí postupně ke každému a zeptá se ho: "Máš na hlavě bílý kobouk?" Vězeň
odpoví kývnutím hlavy a popravčí jeho odpověď zopakuje nahlas. Když odpoví
správně, je zachráněn, jinak je zastřelen. Potom se přechází k dalšímu. Jakou
nejlepší strategii mohou vězni zvolit, pokud mají možnost se na ní dopředu
domluvit?

Pozn.: Kývnutí hlavy je tam proto, aby
nemohli dávat signál intenzitou hlasu. Ostatní vězňové vždy uslyší otázku,
odpověď ano/ne a případně výstřel.


# Opakování

## Největší společný dělitel

Porovnejte rychlost naivního řešení a Euklidova algoritmu na větších číslech pomocí funkce `time.time()`.

    def NSD(a, b):...

    >>> NSD(504, 180)

    36

## Nejmenší společný násobek

    def nsn(a,b):...

    >>> nsn(504, 180)

    2520

## Faktoriál

    def faktorial(n):...

    >>> faktorial(10)

    3628800

# Prvočísla

## Test prvočísla

    def je_prvocislo(n):...

    >>> je_prvocislo(17)

    True

## Výpis prvočísel

    def prvocisla(kolik):...

    >>> prvocisla(10)

    2 3 5 7 11 13 17 19 23 29

# [Palindrom](http://cs.wikipedia.org/wiki/Palindrom)

## Otočení slova/čísla

    def otoc(x):...

    >>> otoc(12345)

    '54321'

## Kontrola palindromu

    def je_palindrom(x):...

    >>> je_palindrom(123454321)

    True

# Pokročilé

## [Aproximace sinu Tylerovou řadou](http://cs.wikipedia.org/wiki/Taylorova_%C5%99ada)

    def sinus(x, presnost):...

    >>> sinus(pi/4, 20)

    0.707106781187

## Převod z desítkové do dvojkové soustavy

    def dec2bin(n):...

    >>> dec2bin(10)

    '1010'

## Převod z desítkové do jiné soustavy obecně

    def konvertuj(n, znaky):...

    >>> konvertuj(200, "0123456789ABCDEF")

    'C8'

