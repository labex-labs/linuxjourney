# ps (Protsessid)

## Tunni sisu

Protsessid on arvutis töötavad programmid. Neid haldab tuum ja neil kőigil on oma ID, mida nimetatakse <b>protsessi ID'ks (PID)</b>. Need ID'd jagatakse välja protsessside loomise järjekorras.

*ps* käsku sisestades saab näha nimekirja töötavatest protsessidest:

<pre>$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
</pre>

Kiire ülesvőte protsesside kohta annab järgmist infot:

<ul>
<li><i>PID</i>: Protsessi ID</li>
<li><i>TTY</i>: Protsessiga seotud terminal (sellest pikemalt veidi hiljem)</li>
<li><i>STAT</i>: Protsessioleku kood</li>
<li><i>TIME</i>: Summaarne protsessori kasutamise aeg</li>
<li><i>CMD</i>: Käsu/käivitatud rakenduse nimi</li>
</ul>

*Ps*i *man* lehet vőib leida palju erinevaid vőimalusi selle käsu sisestamiseks. Need erinevad veidi sőltuvalt millist variant soovitatakse kasutada - BSD, GNU vői Unix. Tőenäoliselt on BSD stiil teistest natuke populaarsem, seega kasutatakse sellel kursusel seda. Uudishimu rahuldamiseks vőib öelda, et erinevus seisneb selles, mitut kriipsu kasutatakse ja lippudes.
 
<pre>$ ps aux</pre>

<b>a</b> kuvab kőik töötavad protsessid, kaasaarvatud need, mis töötavad teiste kasutajate all. <b>u</b> kuvab protsesside kohta rohkem detaile ja viimaks, <b>x</b> kuvab kőik protsessid, millega ei ole TTY'd seostatud. Nendel protsessidel on ? kuvatud TTY veerus. Selline asi on väga levinud deemonite (teenuste) puhul, mis seotud süsteemi käivitumisega.

Selle käsuga on näha oluliselt rohkem välju. Neid pole vaja kőiki meelde jätta kuna järgmises, protsesside peatükis räägitakse neist täpsemalt:

<ul>
<li><i>USER</i>: Kehtiv kasutaja (see kelle ligipääsuőigusi kasutatakse)</li>
<li><i>PID</i>: Protsessi ID</li>
<li><i>%CPU</i>: Kasutatud protsessoriaja suhe aega, mille jooksul protsess on töötanud</li>
<li><i>%MEM</i>: Protsessi püsimahuosa kogu füüsilise mälu suhtes</li>
<li><i>VSZ</i>: Protsessi virtuaalmälu kasutus</li>
<li><i>RSS</i>: Tegumi püsimahuosa saalimata füüsilisest mälust</li>
<li><i>TTY</i>: Protsessiga seostatud terminal</li>
<li><i>STAT</i>: Protsessioleku kood</li>
<li><i>START</i>: Protsessi käivitumise aeg</li>
<li><i>TIME</i>: Summaarne protsessori kasutamise aeg</li>
<li><i>COMMAND</i>: Käsu/käivitatud rakenduse nimi</li>
</ul> 

*ps* käsu kogu väljundi vaatamine vőib muutuda tülikaks, kőige rohkem tasub vaadata PID, STAT ja COMMAND veerge.

Teine väga kasulik käsk on *top*. See kuvab töötavate protsesside kohta juba mitte enam hetke ülesvőtet vaid jooksvat informatsiooni. Vaikimisi uuendatakse kuva iga 10 sekundi järel. *Top* on äärmisel kasulik vahend kui on vajalik teada, millised protsessid kasutavad suuremal määral arvuti ressursse.

<pre>$ top</pre>

## Harjutus

Kasutada *ps* erinevate lippudega ja pöörata tähelepanu sellele, kuidas muutub kuvatav info.

## Küsimus

Millise *ps*'i lipuga kuvatakse protsesside kohta detailset infot?

## Vastus

*u*
