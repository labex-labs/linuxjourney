# Protsesside jälgimine: top

## Tunni sisu

Sellel kursusel tutvustatakse, kuidas lugeda ja analüüsida süsteemi ressursside kasutust. Selles peatükis näidatakse häid tööriistu, millega on hea teostada protsesside seiret.

<b>top</b>

*Top*'ist on ka varem juttu olnud kuid seekord süveneme natuke spetsiifilisemalt sellesse, mida täpselt tegelikult kuvatakse. Meenutame, et *top* on tööriist, mis võimaldab kuvada protsesside poolt kasutatavaid ressursse reaalajas:

<pre>
top - 18:06:26 up 6 days,  4:07,  2 users,  load average: 0.92, 0.62, 0.59
Tasks: 389 total,   1 running, 387 sleeping,   0 stopped,   1 zombie
%Cpu(s):  1.8 us,  0.4 sy,  0.0 ni, 97.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  32870888 total, 27467976 used,  5402912 free,   518808 buffers
KiB Swap: 33480700 total,    39892 used, 33440808 free. 19454152 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                             
 6675 patty    20   0 1731472 520960  30876 S   8.3  1.6 160:24.79 chrome                             
 6926 patty    20   0  935888 163456  25576 S   4.3  0.5   5:28.13 chrome 
</pre>

Kohe räägime, mida see väljund tähendab. Seda infot ei pea kõike meelde jätma, kui on tarvis võib meenutamiseks siia peatüki juurde hiljem tagasi tulla.

<b>1. rida: See on informatsioon, mida võib näha kui sisestada *uptime* käsk (hiljem rohkem)</b>

Väljad vasakult paremale:
<ol>
<li>Hetke aeg</li>
<li>Süsteemi töötamise aeg</li>
<li>Sisse logitud kasutajate arv</li>
<li>Süsteemi keskmine koormus (hiljem rohkem)</li>
</ol>

<b>2. rida: tegumid, mis töötavad, magavad, on peatatud ja zombid</b><br>
Lisainfo *zombie* protsesside kohta:
* http://askubuntu.com/questions/48624/what-are-zombie-processes
* http://stackoverflow.com/questions/16944886/how-to-kill-zombie-process
* https://www.cyberciti.biz/tips/killing-zombie-process.html

<b>3. rida: protsessori informatsioon</b>

<ol>
<li><i>us</i>: kasutaja protsessori aeg  - Protsent protsessori kasutamise ajast, mis on kulunud mittekenadele protsessidele.</li>
<li><i>sy</i>: süsteemi protsessori aeg - Protsent protsessori kasutamise ajast, mis on kulunud tuumale ja selle protsessidele.</li>
<li><i>ni</i>: kena protsessori aeg - Protsent protsessori kasutamise ajast, mis on kulunud kenadele protsessidele.</li>
<li><i>id</i>: protsessori tegevusetu aeg - Protsent, mille jooksul protsessor on olnud tegevusetu.</li>
<li><i>wa</i>: sisend/väljund ooteaeg - Protsent protsessori kasutamise ajast, mis on kulunud sisendi/väljundi järgi ootamiseks. Kui see väärtus on väike, ei ole probleem ilmselt kettas või võrgu sisendis/väljundis</li>
<li><i>hi</i>: riistvara katkestused - Protsent protsessori kasutamise ajast, mis on kulunud riistvara poolt saadetud katkestuste teenindamisele.</li>
<li><i>si</i>: tarkvara katkestused - Protsent protsessori kasutamise ajast, mis on kulunud tarkvara poolt saadetud katkestuste teenindamisele.</li>
<li><i>st</i>: varastatud aeg - Kui arvutis töötavad virtuaalmasinad, on see protsent protsessori ajast, mis on varastatud teiste tegumite jaoks</li>
</ol>

<b>4. ja 5. rida: Mälu ja saaleala kasutus</b>

<b>Hetkel töötavate protsesside nimekiri</b>

<ol>
<li><i>PID</i>: protsessi id</li>
<li><i>USER</i>: kasutaja, kes on protsessi omanik</li>
<li><i>PR</i>: protsessi prioriteet</li>
<li><i>NI</i>: kenaduse väärtus</li>
<li><i>VIRT</i>: protsessori poolt kasutatav virtuaalmälu</li>
<li><i>RES</i>: protsessi kasutatav füüsiline mälu</li>
<li><i>SHR</i>: protsessi jagatud mälu</li>
<li><i>S</i>: Protsessi oleku indikaator: S=magab, R=töötab, Z=zombi,D=ei saa katkestada,T=peatatud</li>
<li><i>%CPU</i> - protsessori kasutamise protsent </li>
<li><i>%MEM</i> - muutmälu (RAM) kasutamise protsent</li>
<li><i>TIME+</i> - protsessi summaarne tööaeg</li>
<li><i>COMMAND</i> - protsessi nimi</li>
</ol>

Võib ka täpsustada protsessi ID kui on huvi mingi kindla protsessi vastu:

<pre>$ top -p 1</pre>

## Harjutus

Uurida *top* käsku. Uurida, millised protsessid kasutavad kõige rohkem ressursse.

## Küsimus

Milline käsk kuvab sama väljundi, kui on *top*'i esimene rida?

## Vastus

*uptime*
