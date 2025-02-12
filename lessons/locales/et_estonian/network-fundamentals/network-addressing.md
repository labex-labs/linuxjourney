# Adresseerimine

## Tunni sisu

Enne kui vaatame kuidas pakettid võrgus liiguvad, peab tuttavaks saama terminoloogiaga. Kui saata kirja siis pean teadma, kellele seda saadetakse ja kust see tuleb. Pakettidel on vaja samasugust informatsiooni. Hoste tuvastavad MAC (*media access control*)ja IP aadressid. Et inimestele asja lihtsamaks teha kasutatakse hostide tuvastamiseks hostinimesid.

<b>MAC aadressid</b>

MAC aadress on unikaalselt tuvastatav riistvara aadress. See ei muutu kunagi.  Kui kasutaja tahab ühenduda Internetti, on arvutisse vaja seadet nimega võrguliidese kaart (NIC - *Network Interface Card*). Sellel võrguadapteril ongi riistvara aadress, mille abil saab arvutit võrgus tuvastada. Etherneti seadme MAC aadress näeb välja umbes selline: 00:C4:B5:45:B2:43. MAC aadressid antakse võrguadapteritele tootmise käigus. Igal tootjal on organisatsiooni unikaalselt tuvastav number (OUI). Selle OUI leiab MAC aadressi esimesest kolmes baidist. Näites on Dellil see 00-14-22, mistõttu võiks Delli adapteriga arvuti MAC aadress olla näiteks 00-14-22-34-B2-C2.

<b>IP aadressid</b>

IP aadressi kasutatakse seadme tuvastamiseks võrgus, need ei ole riisvarast sõltuvad ja erinevad süntaksi poolest sõltuvalt, kas kasutatakse IPv4 või IPv6 (sellest rohkem vähe hiljem) aadressi. Hetkel eeldame, et kasutatakse IPv4 aadressi. Sellisel juhul näeks tüüpiline aadress välja nii: 10.24.12.4. IP aadressi kasutatakse võrgunduse tarkvaralise poole peal. Süsteemil, mis on ühendatud Internetti, peaks olema igal hetkel IP aadress. See aadress võib ka muutuda kui vahetada võrku. IP aadressid on Internetis unikaalsed (ei pruuga ka alati nii olla, sellest saab aimu kui jõuame NAT'i peatükini).

<b>Hostinimed</b>

Viimane variant seadet tuvastada on hostinimed. Hostinimed võimaldavad IP aadressi esitada inimloetaval kujul. Selle asemel, et pidada meeles 192.12.41.4 võib pidada meeles hoopis minuhost.com

## Harjutus

Harjutust pole.

## Küsimus

Mitu baiti on IPv4 aadress pikk?

## Vastus

4
