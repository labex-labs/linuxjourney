# ICMP

## Tunni sisu

Interneti kontrollsõnumite protokoll ICMP (*Internet Control Message Protocol*) on osa TCP/IP protokollistikust. Sellega saadetakse veateateid ja see on äärmiselt kasulik võrguga seotud probleemide silumiseks, näiteks pakettide ebaõnnestunud kohaletoimetamise korral.

Igas ICMP teates on tüübi, koodi ja kontrollsumma väljad. Tüübi väljas on ICMP sõnumi tüüp, kood on alamtüüp ja see annab täiendavat informatsiooni sõnumi kohta ning kontrollsummat kasutatakse sõnumi terviklikkuse probleemide tuvastamiseks.

Tavalisemad ICMP tüübid:

<ul>
<li>Type 0 - <i>Echo Reply</i> ehk kajapäringu vastus</li>
<li>Type 3 - <i>Destination Unreachable</i> ehk sihtkoht on kättesaamatu </li>
<li>Type 8 - <i>Echo Request</i> ehk kajapäring</li>
<li>Type 11 - <i>Time Exceede</i> ehk aeg on ületatud</li>
</ul>

Kui pakett ei ole võimeline sihtkohta jõudma, gerereeritakse kolmandat tüüpi ICMP sõnum. Selle tüübi piires on 16 koodi, mis kirjeldavad täpsemalt, miks pakett sihkohta ei saa jõuda:

<ul>
<li>Code 0 - <i>Network Unreachable</i> ehk võrk on kättesaamatu</li>
<li>Code 1 - <i>Host Unreachable</i> ehk host on kättesaamatu</li>
jne...jne...
</ul>

Need sõnumid muutuvad arusaadavamaks kui tutvuda võrgu tõrkeotsingu tööriistadega.

## Harjutus

Harjutust pole.

## Küsimus

Millist tüüpi on ICMP kajapäring?

## Vastus

8
