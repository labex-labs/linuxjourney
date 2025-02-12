# Paketi teekond

## Tunni sisu

<b>Vaatame kuidas pakett liigub kohalikus võrgus</b>

<ol>
<li>Esiteks vaatab kohalik masin sihtkoha IP aadressi, et tuvastada kas alamvõrgu mask vastab samale alamvõrgule.</li>
<li>Kui paketti saadetakse, on vajalikud MAC ja IP aadressid. Selles punktis on sihtkoha MAC aadress teadmata.</li>
<li>ARP leviedastuse sõnumiga tuvastame kohalikus võrgus asuva sihtkoha MAC aadressi.</li>
<li>Nüüd on pakett saatmiseks valmis.</li>s
</ol>

<b>Vaatame kuidas pakett liigub võrgust väljapoole</b>

<ol>
<li>Esiteks vaadatakse sihtkoha IP aadressi. Kuna see asub kohtvõrgust väljaspool, ei ole MAC aadress nähtav ja  ARP'i ei ole võimalik kasutada (kuna ARP leviedastus töötab ainult kohtvõrgu piires).</li>
<li>Seega pöördutakse nüüd marsruutimistabeli poole. Kuna sihtkoha aadress on kohalikule seadmele tundmatu, saadetakse see vaikelüüsile (teine marsruuter). Nüüd on paketil IP aadressid ja saatja MAC aadress. Saaja MAC aadress on ikka veel puudu. Meenutame, et MAC aadresse saab tuvastada vaid sama võrgu piires. Mis siis nüüd edasi saab? ARP päring saadetakse vaikelüüsile.</li>
<li>Marsruuter vaatab paketti ja kinnitab MAC aadressi. Kuid pakett ei ole veel jõudnud sihtkoha, mistõttu vaadatakse taaskord marsruutimistabelit leidmaks sihtkohta. Iga kord kui pakett edasi liigub, eemaldatakse eelmised MAC aadressid ja lisatakse uued.</li>
<li>Kui pakett lõpuks õigesse võrku jõuab kasutatakse ARPi leidmaks viimane MAC aadress.</li>
<li>Kogu selle protsessi jooksul on saaja ja saatja IP aadressid muutumatud.</li>
</ol>

## Harjutus

Harjutust pole

## Küsimus

Mille abil leitakse IP aadressile vastav MAC aadress?

## Vastus

*ARP*
