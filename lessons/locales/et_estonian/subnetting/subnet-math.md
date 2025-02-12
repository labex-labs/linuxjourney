# Alamvõrgu matemaatika

## Tunni sisu

Nonii, eelmises peatükis sai selgeks, et alamvõrgu maskide abil on võimalik välja selgitada, mitu kasutajat alamvõrku mahub. Kui palju siis ikkagi?

Võtame näiteks IP aadressi <b>192.168.1.0</b> ja alamvõrgu maski <b>255.255.255.0</b>. Asetame need numbrid binaarkujul kohakuti. Hetkel kasutame teisendamiseks [võrgus leiduvat kalkulaatorit](http://jodies.de/ipcalc).

<pre>
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
</pre>

IP aadress maskitakse alamvõrgu poolt seal kus alamvõrgu maskis on ühed. Kuna see on maskitud siis teeskleme, et me ei näe seda osa. Seega ainult nullide osa on see, kus meil saavad olla kasutajad.Meenutame, et 11111111 binaaresituses on võrde arvuga 255. Kuna loeme ka 0 kui võimalikku varianti, on meil 256 võimalikku hosti. Tegelikult päris nii ei ole. Sellest numbrist tuleb veel lahutada 2, kuna meil on ka võrgu enda aadress ning leviedastuse aadress. Seega jääb järgi 254 võimalikku lõppkasutajat, kelle IP aadressid jäävad vahemikku 192.168.1.1 - 192.168.1.254.

## Harjutus

Harjutust pole.

## Küsimus

Mis vastab binaaresituses arvule 255?

## Vastus

11111111
