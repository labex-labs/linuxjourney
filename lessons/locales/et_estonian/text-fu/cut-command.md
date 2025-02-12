# cut

## Tunni sisu

Õpime mõned kasulikud tekstitöötlemise käsud. Alustuseks loome faili, millega hakkame tegelema. Kopeerida ja kleepida järgmine käsk. Lisada tabulaator laisa ja koera vahele (hoia all Ctrl-v + TAB).

<pre>$ echo 'Kiire pruun; rebane hüppas üle laisa  koera' > näide.txt</pre>

Esimesena õpime lõikamise käsu kohta. See eraldab faili tekstist mingisuguse osa.

Et eraldada sisu tähemärkide nimekirja põhjal:

<pre>$ cut -c 7 näide.txt</pre>

See annab väljundiks faili iga rea seitsmenda tähemärgi. Praegusel juhul on see "p". NB! Ka tühikud loevad tähemärkidena.

Et eraldada sisu failipõhiselt, tuleb natuke muudatusi sisse viia:

<pre>$ cut -f 2 näide.txt</pre>

-f või siis väljalipp, lõikab teksti põhinedes väljadele. Vaikimisi kasutab see eraldajana tabulaatorit, mis tähendab, et kõik, mida eraldab tabulaator, peetakse omaette väljaks. Väljundina peaks nägema "koera".

<pre>$ cut -f 1 -d ";" sample.txt</pre>

See muudab eraldaja tabulaatorist hoopis semikooloniks ";" ja kuna me lõikame esimest välja, peaks tulemus olema hoopis "kiire pruun".


## Harjutus

Mida järgmine käsk teeb? Miks?

<pre>$ cut -c 5-10 näide.txt
$ cut -c 5- näide.txt
$ cut -c -5 näide.txt
</pre>

## Küsimus

Millist käsku sa kasutaksid, et saada iga rea esimene tähemärk?

## Vastus

*cut -c 1*
