# Kontrollterminal

## Tunni sisu

Eelmises peatükis sai räägitud TTY väljast *ps*i väljundis. TTY on see terminal, mis käsu käivitas.

Terminale on kahte sorti: tavapärased <b>terminalseade</b> ja <b>pseudoterminalseade</b>. Tavapärane terminalseade on loomulik vahend, millesse saab trükkida ja saata väljund süsteemile. Kõlab kui terminalirakendus, mida oleme seni kasutanud, et käivitada kestprogrammi kuid päris nii see pole.

Liigume siit nüüd sujuvalt edasi, et seda näidata. Kasutada klahvikombinatsiooni Ctrl-Alt-F1, et pääseda ligi virtuaalsele konsoolile TTY1. Kuvatakse ainult terminal, ei mingit graafikat. Seda nimetatakse tavapäraseks terminalseadmeks. Sellest saab väljuda klahvikombinatsiooniga Ctrl-Alt-F7.

Pseudoterminal on aga juba harjumuspäraseks saanud terminal, mis emuleerib terminali kestprogrammi aknaga ja märgistus on PTS. Kui uuest vaadata *ps*i, siis kasutatav kestprogrammi protsess on leitav *pts/* * alt, näiteks:
<pre>
ps -e | grep pts
11477 pts/0    00:00:00 tmux
11510 pts/2    00:00:00 bash
11612 pts/2    00:00:00 sudo
11672 pts/2    00:00:00 bash
11720 pts/1    00:00:00 bash
16012 pts/1    00:00:00 man
16024 pts/1    00:00:00 pager
16750 pts/5    00:00:00 bash
27323 pts/5    00:00:00 ps
27324 pts/5    00:00:00 grep
32565 pts/3    00:00:00 ssh
32598 pts/4    00:00:00 ssh
</pre>

Kui nüüd ringiga kontrollterminalide juurde tagasi tulla, siis protsessid ongi tavaliselt ühega seotud. Kui kestprogrammi aknas mingi protsess töötab, näiteks *find* ja see aken sulgeda siis sulgub koos sellega ka protsess.

On olemas spetsiaalsed protsessid - deemonid, mis hoiavad süsteemi töös. Need käivituad tavaliselt süsteemi alglaadimisel ja peatuvad kui süsteem välja lülitada. Need protsessid töötavad taustal ja kuna me ei taha, et need peatuksid siis ei ole need ka ühegi kontrollterminaliga seotud. *ps*i väljundis on TTY kohal ?, mis tähendabki, et kontrollterminal puudub. 

## Harjutus

Vaadata *ps*i väljundit ja kuva kõik unikaalsed TTY väärtused.

## Küsimus

Milline väärtus antakse protsessile, millel ei ole kontrollterminali?

## Vastus

?
