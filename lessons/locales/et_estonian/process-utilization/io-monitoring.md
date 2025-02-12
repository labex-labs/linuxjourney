# Sisendi/väljundi seire

## Tunni sisu

Sarnaselt protsessori koormusele saab uurida ka ketta kasutamist käepärase tööriistaga <b>iostat</b>.

See programm ei ole vaikimisi kaasas, paigaldamiseks <b>sudo apt update && sudo apt install sysstat && sudo apt clean    </b>

<pre>
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
</pre>

Esimene osa on protsessori informatsioon:

<ul>
<li><i>%user</i> - protsessori kasutamise protsent kasutaja tasemel (rakendused) </li>
<li><i>%nice</i> - protsessori kasutamise protsent kasutaja tasemel ja kenaduse prioriteetidega</li>
<li><i>%system</i> - protsessori kasutamise protsent süsteemi (tuuma) tasemel </li>
<li><i>%iowait</i> - protsent, mille jooksul protsessor oli tegevusetu kuid eksisteerisid sisend/väljund päringud </li>
<li><i>%steal</i> - aeg, mis kulus virtuaalsel protsessoril mittevabatahtlikule ootamisele, kuni teenindati teisi virtuaalseid protsessoreid. </li>
<li><i>%idle</i> - aeg, kui protsessor oli tegevusetu ja puudusid sisend/väljund päringud</li>
</ul>

Teine osa on ketta kasutamise kohta:

<ul>
<li><i>tps</i> - Ülekannete arv sekundis. Ülekanne on seadmele suunatud sisend/väljund päring. Mitu loogilist päringut võib liita üheks sisend/väljund päringuks. Ülekanne on määramata suurusega.</li>
<li><i>kB_read/s</i> - Seadmelt loetud andmete kogus kilobaitides sekundi kohta.</li>
<li><i>kB_wrtn/s</i> - Seadmele kirjutatud andmete kogus kilobaitides sekundi kohta.</li>
<li><i>kB_read</i> - Summaarne kilobaitide arv, mis seadmelt loeti.</li>
<li><i>kB_wrtn</i> - Summaarne kilobaitide arv, mida seadmele kirjutati.</li>
</ul>

## Harjutus

Kasutada *iostat*'i ketta kasutuse kuvamiseks.

## Küsimus

Millise käsuga saab kuvada sisendi/väljundi ja protsessori kasutust?

## Vastus

*iostat*
