# find

## Tunni sisu

Meil on süsteemis palju faile ning nendest ühe konkreetse leidmine võib muutuda veidi keeruliseks. Saame selle jaoks kasutada käsku find!

<pre>$ find /home -name kutsikad.jpg</pre>

Kui kasutada find käsku, peab täpsustama, millisest kataloogist tuleb faili otsida. Praegusel juhul otsime faili nime (*name*) kutsikad.jpg järgi.

Võib ka täpsustada, millist tüüpi faili leida püütakse.

<pre>$ find /home -type d -name MinuKaust</pre>

Nagu märkata võis siis pandi failitüübiks d (kataloogi jaoks) ning samal ajal otsiti endiselt nime järgi MinuKaust.

Lahe asi mida silmas pidada on see, et *find* ei piirdu otsimisega täpsustatud kataloogist, see otsib ka kõikvõimalikest alamkataloogidest.

## Harjutus

<ol>
<li>Leia juurkataloogist fail, mille nimes on sõna <i>net</i>.</li>
</ol>

## Küsimus

Kuidas peab *find* käsku täpsustama, kui tahta otsida failinime järgi?

## Vastus

-name
