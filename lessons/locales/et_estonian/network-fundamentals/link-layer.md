# Andmevahetuskiht

## Tunni sisu

TCP/IP mudeli põhjas istub andmevahetuskiht. See kiht on seotud riistvaraga.

Siin kapseldatakse pakett veelkord, seekord nimetatakse seda raamiks. Raami päisesse pannakse saaja ja saatja MAC aadressid, kontrollsummad ja paketieraldajad, et vastuvõtja teaks millal pakett lõpeb.

Õnneks oleme endiselt samas võrgus, mistõttu ei pea pakett liiga kaugele reisima. Esiteks lisab kiht saatja aadressi päisesse kuid vaja on ka Peetri aadressi. Kuidas see kiht seda küll teab? Kuidas seda teada saada kui seda pole Internetis? Me kasutame ARPi.

<b>ARP (*Aadress Resolution Protocol*) ehk aadressiteisenduse protokoll</b>

ARP leiab IP aadressiga seotud MAC aadressi. Seda kasutatakse ühe võrgu piires. Kui Peeter ei asuks samas võrgus, kasutaksime marsruutimise süsteemi, et teada saada järgmine marsruuter, mis paketi vastu võtab. Kuna me oleme aga samas võrgus, kasutame ARPi.

Süsteem kasutab kõigepealt ARP tabelit, miles hoitakse informatsiooni IP aadressidega seotud MAC aadressidest. Kui vajalikku aadressi seal pole, kasutame ARP'i. Süsteem kasutab ARP protokolli leviedastust, et tuvastada kellele kuulub IP aadress 10.10.1.4. Leviedastus on teate saatmine nõnda, et selle saavad kõik võrgus olevad hostid. Arvutid, millel on päritav IP aadress, saadavad vastu ARP paketi, milles on nende IP ja MAC aadress.

Nüüd kui kõik vajalikud andmed on olemas, saadab Andmevahetuskiht läbi NIC kaardi paketid järgmisele seadmele, et leida Peetri võrk. See etapp on natukene keerulisem kui sai just kirjeldatud, kuid seletame selle lahti marsruutimise peatükis.

Selline ongi lihtne (või mitte nii lihtne) paketi liikumine TCP/IP mudelis. Paketid aga ei liigu vaid ühesuunaliselt. Me pole veel Peetri võrku jõudnud. Andmed peavad mudeli läbima vähemalt kaks korda, enne kui midagi saadetakse või vastu võetakse. Reaalsuses näeks see välja umbes nii:

<b>Paketi liikumine</b>

<ol>
<li> Jaanus saadab Peetrile e-kirja: andmed saadetakse transpordikihile.</li>
<li> Transpordikiht kapseldab andmed TCP või UDP päisesse ja moodustab segmendi. Segmendile lisatakse siht- ja lähtekoha TCP või UDP port. Seejärel saadetakse segment võrgukihile.</li>
<li> Võrgukiht kapseldab TCP segmendi IP paketiks. Lisatakse siht- ja lähtekoha IP aadress. Pakett edastatakse andmevahetuskihile.</li>
<li> Pakett jõuab seejärel Jaanuse riistvarani ja kapseldatakse raami, millele lisatakse MAC aadressid.</li>
<li> Peeter võtab andmeraami oma riistvaral vastu ja kontrollib iga raami terviklikkust. Seejärel pakitakse raami sisu lahti ja IP pakett saadetakse võrgukihile.</li>
<li> Võrgukiht loeb paketti, et saada teada varem lisatud IP aadressid, kontrollitakse kas kohaliku arvuti IP aadress vastab saaja aadressile. Pakett pakitakse lahti ja segment saadetakse transpordikihile.</li>
<li>Transpordikiht pakib lahti segmendi, kontrollib pordi numbrit ja loob vastavalt sellele vajaliku ühenduse rakenduskihiga.</li>
<li>Rakenduskiht võtab andmed vastu läbi viidatud pordi ja edastab need e-kirja kujul Peetrile.</li>
</ol>

## Harjutus

Harjutust pole.

## Küsimus

Millega saab välja uurida seadme MAC aadressi sama võrgu piires?

## Vastus

ARP
