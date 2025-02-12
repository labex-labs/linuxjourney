# Kleepuv bitt

## Tunni sisu

Veel viimane eriline õiguse bitt millest räägime on kleepuv bitt.

See bitt ütleb, et ainult faili omanik või juurkasutaja tohib antud faili muuta. See on väga kasulik jagatud kataloogide puhul. Vaatame näidet:

<pre>
$ ls -ld /tmp

drwxrwxrwxt 6 root root 4096 Dec 15 11:45 /tmp
</pre>

Õiguste lõpus võib näha erilist bitti <b>t</b>. See tähendab, et kõik võivad faile /tmp kataloogis lisada, neisse kirjutada ja neid muuta kuid ainult juurkasutaja tohib seda kataloogi kustutada.

<b>Kleepuva biti muutmine</b>

<pre>
$ sudo chmod +t mydir


$ sudo chmod 1755 mydir
</pre>

Kleepuva biti numbriline esitus on <b>1</b>

Õiguste arvutamiseks on loodud ka mitmeid veebipõhiseid vahendeid, üks näide on <a target="_blank" href="http://permissions-calculator.org/">http://permissions-calculator.org/</a>

## Harjutus

Millistel failidel võiks veel olla kleepuv bitt lubatud?

## Küsimus

Milline sümbol esindab kleepuvat bitti?

## Vastus

t
