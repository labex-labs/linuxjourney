# expand ja unexpand

## Tunni sisu

Cut käsu peatükis oli meil näide.txt fail, milles oli kasutatud tabulaatorit. Tavaliselt peaks selle kasutamine olema märgatavalt näha, kuid mõned tekstifailid ei näita seda väga selgelt. Tabulaator ei pruugi olla parim eraldaja, mida tekstifailis kasutada.
Kõikide tabulaatorite muutmiseks tühikuteks kasutada expand käsku.

<pre>$ expand näide.txt</pre>

See käsk trükib väljundi, kus kõik tabulaatorid on muudetud grupiks tühikuteks. Väljundfaili salvestamiseks kasutada ümbersuunamist nagu all näidatud.

<pre>$ expand näide.txt > tulemus.txt</pre>

Vastandina *expand* käsule, saame muuta ka grupi tühikuid tabulaatoriks. Kasutame selleks käsku *unexpand*:

<pre>$ unexpand -a tulemus.txt</pre>

## Harjutus

Mis juhtub kui sisestad lihtsalt *expand* ilma failisisendita?

## Küsimus

Millise käsuga muudetakse tabulaatorid tühikuteks?

## Vastus

*expand*
