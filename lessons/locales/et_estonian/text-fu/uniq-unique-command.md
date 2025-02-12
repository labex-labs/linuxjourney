# uniq (Unique)

## Tunni sisu

*Uniq* (unikaalne) käsk on veel üks kasulik tööriist teksti töötlemiseks.

Näiteks on ühest failist mitu koopiat:


<pre>
lugemine.txt
raamat
raamat
ajaleht
ajaleht
artikkel
artikkel
ajakiri
</pre>

... ja soovitakse korduvatest eksemplaridest lahti saada. Selleks saab kasutada uniq käsku:

<pre>$ uniq lugemin.txt
raamat
ajaleht
artikkel
ajakiri</pre>

Kuvame iga rea kohta nende esinemissageduse:

<pre>$ uniq -c lugemine.txt
2 raamat
2 ajaleht
2 artikkel
1 ajakiri</pre>

Vőtame ainult unikaalsed väärtused:

<pre>$ uniq -u lugemine.txt
ajakiri</pre>

Vőtame ainult korduvad väärtused:

<pre>$ uniq -d lugemine.txt
raamat
ajaleht
artikkel
</pre>

<b>Märkus</b> : uniq ei tuvasta korduvaid ridu juhul, kui nad ei asu kőrvuti. Näiteks:

Näiteks on fail, mille korduvad read ei asu kőrvuti:

<pre>
lugemine.txt
raamat
ajaleht
raamat
ajaleht
artikkel
ajakiri
artikkel
</pre>

<pre>$ uniq lugemine.tx
raamat
ajaleht
raamat
ajaleht
artikkel
ajakiri
artikkelt</pre>

Uniq'i tagastatud väljund sisaldab kőiki kirjed, erinevalt esimesest näitest.

Et sellest piirangust vabaneda, vőime kasutada uniq käsku koos sort käsuga:

<pre>
$ sort lugemine.txt | uinq
artikkel
raamat
ajakiri
ajaleht</pre>

## Harjutus

Milline oleks väljund kui proovida sisestada *uniq -uc*?

## Küsimus

Millist käsku kasutada, et vabaneda kordustest failis?

## Vastus

*uniq*
