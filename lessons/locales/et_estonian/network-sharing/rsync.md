# rsync

## Tunni sisu

Veel üks vahend, millega kopeerida andmeid arvutite vahel on rsync (*remote synchronization*), mis tõlkes tähendab kaugsünkroniseerimist. *Rsync* ja *scp* on väga sarnased kuid leidub ka suuri erinevusi. *Rsync* kasutab spetsiaalset algoritmi kontrollimaks kas andmed, mida soovitakse kopeerida, eksisteerivad juba sihtkohas ning kopeeritakse vaid see osa mis on erinev. Näiteks ütleme, et kasutaja oli kopeerimas faili kui parasjagu võrguühendus katkes. Kopeerimine katkes seega olles poole peal. Selle asemel, et kõike algusest peale uuesti kopeerida, kopeerib *rsync* ainult need osad, mis jäid kopeerimata.

Lisaks kontrollitakse kopeeritavate failide terviklust kontrollsummade abil. Sellised väikesed optimeerimised pakuvad failide ülekandmisel suuremat paindlikkust ja teevad *rsync*'ist ideaalse vahendi just kataloogide sünkroniseerimiseks nii eemalasuvatest masinatest kui ka kohalikult. Hea on teha andmete tagavarakoopiaid, suurte andmekoguste ülekandeid ja palju muud.

Mõned rohkem kasutatavad võimalused:

<ul>
<li>v - kirjeldav väljund</li>
<li>r - rekursiivne</li>
<li>h -inimloetav väljund</li>
<li>z - failide ülekandmine tihendatult, suurepärane aeglase ühenduse korral</li>
</ul>

<b>Failide kopeerimine/sünkroniseerimine sama arvuti piires</b>

<pre>$ rsync -zvr /minu/kohalik/kataloog/esimene /minu/kohalik/kataloog/teine</pre>

<b>Failide kopeerimiseks/sünkroniseerimiseks kohalikust arvutist eemalasuvasse</b>

<pre>$ rsync /kohalik/kataloog kasutajanimi@kaugarvuti.com:/eemalasuv/kataloog</pre>

<b>Failide kopeerimiseks/sünkroniseerimiseks eemalasuvast arvutis kohalikku</b>

<pre>$ rsync kasutajanimi@kaugarvuti.com:/eemalasuv/kataloog /kohalik/kataloog</pre>

## Harjutus

Kasutada *rsync*'i, et sünkroniseerida ühte kataloogi teisega kuid veenduda, et midagi olulist üle ei kirjutata!

## Küsimus

Milline käsk oleks kasulik andeme varukoopiate tegemiseks?

## Vastus

*rsync*
