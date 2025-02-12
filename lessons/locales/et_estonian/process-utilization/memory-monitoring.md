# Mälu seire

## Tunni sisu

Lisaks protsessori ja sisendi/väljundi seirele saab teostada ka mälukasutuse seiret, seda käsuga <b>vmstat</b>.

<pre>
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
</pre>

Väljad on järgmised:

<b>procs</b>
<ul>
<li><i>r</i> - protsesside arv töötamise jooksul</li>
<li><i>b</i> - protsesside arv katkematus unes</li>
</ul>

<b>memory</b>
<ul>
<li><i>swpd</i> - virtuaalmälu kasutamise kogus</li>
<li><i>free</i> - vaba mälu kogus</li>
<li><i>buff</i> - puhvrina kasutatava mälu kogus</li>
<li><i>cache</i> - vahemäluna kasutatava mälu kogus</li>
</ul>

<b>swap</b>
<ul>
<li><i>si</i> - sisse saalitud mälu kogus</li>
<li><i>so</i> - välja saalitud mälu kogus</li>
</ul>

<b>io</b>
<ul>
<li><i>bi</i> - plokkseadmelt vastu võetud plokkide kogus</li>
<li><i>bo</i> - plokkseadmele saadetud plokkide kogus</li>
</ul>

<b>system</b>
<ul>
<li><i>in</i> - katkestuste kogus sekundi kohta</li>
<li><i>cs</i> - kontekstkommutatsioonide kogus sekundi kohta</li>
</ul>
Sõnaseletus<br>
**kontekstkommutatsioon** Arvuti keskprotsessori olekut (konteksti) salvestav ja taastav protsess, mis võimaldab mitmel protsessil ühiselt kasutada üht ja sama protsessorit. Kontekstkommutatsioon täidab olulist rolli multitegumtöötluses. Kuna see protsess nõuab suhteliselt palju arvutusressurssi, siis operatsioonisüsteemide projekteerimisel pööratakse selle optimeerimisele suurt tähelepanu.

<b>cpu</b>
<ul>
<li><i>us</i> - kasutaja ajas veedetud aeg</li>
<li><i>sy</i> - tuuma ajas veedetud aeg</li>
<li><i>id</i> - Kasutamata veedetud aeg</li>
<li><i>wa</i> - sisendi/väljundi järgi ootamise aeg</li>
</ul>

## Harjutus

Uurida mälukasutust *vmstat*'iga.

## Küsimus

Millise tööriistaga kuvatakse mälu kasutust puudutav info?

## Vastus

*vmstat*
