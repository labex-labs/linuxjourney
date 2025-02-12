# netstat

## Tunni sisu

<b>*Well Known Ports* ehk kasutatavamad pordid</b>

Andmete edastamist läbi portide on siin kursustel arutatud. Vaatame nüüd rohkem kasutatavaid porte.

Nimekirja levinud portidest saab kui vaadata faili <b>/etc/services</b>:

<pre>
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp 
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
...jne...
</pre>

Esimeses väljas on teenuse nimi, sellele järgneb pordi number ja kasutatava transpordikihi protokolli number.

<b>netstat</b>

See on üks väga kasulik tööriist saamaks detailset võrguga seotud informatsiooni. *Netsat* kuvab väga erinevat informatsiooni, näiteks võrguühendused, marsruutimistabelid, info võrguliideste kohta ja veel muudki. See on justkui võrgu tööriistade šveitsi armee nuga. Selles peatükis keskendume ühele omadusele, selleks on võrguühenduse olek. Enne näitega tutvumist räägime natuke soklitest ja portidest. Sokkel on liides, mis võimaldab programmidel andmeid vahetada, port aga tuvastab rakenduse, mis peaks andmete edastamist teostama. Sokli moodustavad IP aadress ja port. Iga üksik ühendus vajab unikaalset soklit. Toome näiteks HTTP. See on teenus, mis kasutab porti nr 80. Meil võib ju olla mitu HTTP ühendust (mitu samaaegselt avatud veebilehte). Selleks, et iga ühendust alal hoida luuakse iga ühenduse kohta unikaalne sokkel.

<pre>
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 icebox:domain           *:*                     LISTEN     
tcp        0      0 localhost:ipp           *:*                     LISTEN     
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT  
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT  
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT  
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN     
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT 
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
</pre>

*Netstat -a* käsk kuvab kuulavad ja mittekuulavad võrguühenduste soklid. Võti *-t* kuvab ainult tcp ühendused.

Väljad vasakult paremale on järgmised:

<ul>
<li><i>Proto</i>: Kasutatav protokoll, TCP või UDP (IPv4). Kui on IPv6 siis number 6 protokolli nimetuse järel.</li>
<li><i>Recv-Q</i>: Vastuvõtmise järjekorras ootavad andmed</li>
<li><i>Send-Q</i>: Saatmise järjekorras ootavad andmed</li>
<li><i>Local Address</i>: Kohalikult ühendatud host</li>
<li><i>Foreign Address</i>: Kaugpöördushost</li>
<li><i>State</i>: Sokli olek</li>
</ul>

Lehelt *man netstat* leiab sokli olekute nimekirja kuid siin on mõned näiteks:

<ul>
<li><i>LISTENING</i>: Sokkel kuulab sissetulevaid ühendusi. Meenutame, et kui luua TCP ühendus siis peab sihtkoht kuulama, et tabada meie ühendumise soov.</li>
<li><i>SYN_SENT</i>: Sokkel püüab aktiivselt ühendust luua.</li>
<li><i>ESTABLISHED</i>: Soklil on loodud ühendus.</li>
<li><i>CLOSE_WAIT</i>: Sihtkoht on ühenduse katkestanud ja oodatakse sokli sulgumist.</li>
<li><i>TIME_WAIT</i>: Sokkel on pärast sulgumist ootavas seisundis, et tegeleda pakettidega, mis on endiselt võrgus.</li>
 </ul>

## Harjutus

Tutvuda *man netstat* leheküljel kõikide netstat'i kasutamise võimalustega.

## Küsimus

Millist porti kasutab HTTPS?

## Vastus

443
