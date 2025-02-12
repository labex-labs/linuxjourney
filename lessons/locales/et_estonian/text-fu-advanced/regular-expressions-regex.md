# regex (Regulaaravaldis)

## Tunni sisu

Regulaaravaldised on võimsad tööriistad mustril põhineva valiku teostamiseks. See kasutab erilist kirjapilti, mis sarnaneb natuke sellele, millega oleme juba kokku puutunud, näiteks metamärk *.

Võtame läbi mõned kõige tavalisemad regulaaravaldised, mis on peaaegu universaalsed ükskõik millises programmeerimiskeeles.

Kasutame järgmist fraasi testsõnena:
<pre>
sally sells seashells 
by the seashore
</pre>

<b>1. Rea alustamine märgiga ^</b>
<pre>
<b>^by</b>
saaks vasteks rea "by the seashore"
</pre>

<b>2. Rea lõpetamine märgiga $</b>

<pre>
seashore<b>$</b>
saaks vasteks "by the seashore"
</pre>

<b>3. Ühe märgi sidumine sümboliga .</b>

<pre>
b<b>.</b>
saaks vasteks by
</pre>

<b>4. Sulgude [] ja () kasutamine</b>

See võib olla natuke keerulisem, sulud lubavad meil täpsustada, mis häälikuid nende seest võib leida.

<pre>
d<b>[iou]</b>g
saaks vasteks: dig, dog, dug
</pre>

Kui kasutada ankursilti ^ sulgude sees, tähendab see, et peetakse silmas kõiki tähemärke, peale nende mis sulgudes on.

<pre>
d<b>[^i]</b>g
saaks vasteks: dog ja dug aga mitte dig
</pre>

Sulgudes saab kasutada ka vahemikku, et suurendada soovitud tähemärkide hulka.

<pre>
d<b>[a-c]</b>g
leiab vasteks dag, dbg, ja dcg
</pre>

Ole ettevaatlik, sulud on tõstutundlikud.

<pre>
d<b>[A-C]</b>g
vasteks on dAg, dBg ja dCg kuid mitte dag, dbg ja dcg
</pre>

Ja need ongi mõned põhilised regulaaravaldised.

## Harjutus

Proovi kombineerida regulaaravaldisi grep'iga ja vaata läbi mõned failid.

<pre>
grep [siia regulaaravaldis] [fail]
</pre>

## Küsimus

Millise regulaaravaldise vasteks on üksik tähemärk?

## Vastus

.
