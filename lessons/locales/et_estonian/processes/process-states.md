# Protsesside olekud

## Tunni sisu

Vaatame uuesti *ps aux* käsku:

<pre>$ ps aux</pre>

STAT tulbas võib näha palju väärtusi. Linuxi protsess võib olla üsna paljudes erinevates olekutes.

<ul>
<li>R: <i>running</i> ehk <i>töötav</i>, ootab, et protsessor temaga tegeleks</li>
<li>D: <i>uninterruptible sleep</i> ehk siis protsess on <i>katkematus unes</i> - ootab, et mingi sündmus oma tööga valmis saaks, näiteks terminali sisend</li>
<li>Z: <i>zombi</i>, eelmises peatükis räägiti, et <i>zombid</i> on töö lõpetanud protsessid, mis ootavad, et nende oleku kohta info ära korjataks</li>
<li>T: peatunud, protsess on ajutiselt peatatud</li>
</ul>

## Harjutus

Tutvuda süsteemis töötavate protsesside ja nende olekutega.

## Küsimus

Millise STAT koodiga on esindatud <i>katkematus unes</i> protsessid?

## Vastus

D
