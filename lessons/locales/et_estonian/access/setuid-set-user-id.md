# Setuid

## Tunni sisu

Paljudes olukordades võib tavakasutajal vaja olla kõrgendatud ligipääsu mingitele andmetele ja süsteemiadministraator ei saa alati joosta kohale, et juurkasutaja salasõna sisestada. Kuid õnneks on olemas spetsiaalsed ligipääsuõiguste bitid, mis aitavad seda probleemi lahendada. *Set User ID* (SUID) ehk kasutaja ID seadmine võimaldab kasutaja asemel käivitada programmi selle omaniku õigustes.

Vaatame näidet:

Ütleme, et tahan muuta oma salasõna. Lihtne eks? Kasutan lihtsalt *passwd* käsku:

<pre>
$ passwd
</pre>

Mida see käsk teeb? See muudab mõnda faili kuid kõige olulisem on, et see muudab */etc/shadow* faili. Vaatame seda korraks:

<pre>
$ ls -l /etc/shadow


-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow

</pre>

See fail on ju aga juurkasutaja omanduses! Kuidas on mul võimalik muuta faili, mille omanik on juurkasutaja?

Vaatame veel ühte õiguste komplekti, seekord sisestatud käsu oma:

<pre>
$ ls -l /usr/bin/passwd


-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
</pre>

Võib märgata, et käivitusõigus on seal <b>s</b>. See õiguste bitt on SUID, mille olemasolul failiõigustes lubab see käivitajal võtta faili omaniku, meie näites juurkasutaja õigused, sealhulgas käivitamise õiguse. Seega tegelikkuses kui sisestada *passwd* käsk, käivitatakse see juurkasutajana.

Seetõttu ongi võimalik pääseda passwd käsuga ligi kaitstud failidele nagu */etc/shadow*. Kui see bitt eemaldada siis on kohe selge, et vastavat faili muuta ei saa ja salasõna jääb samuti muutmata.

<b>SUID muutmine</b>

Sarnaselt teistele õigustele saab SUID õigusi ka muuta kahel viisil.

*Sümboliline viis:*

<pre>
$ sudo chmod u+s minufail
</pre>

*Numbriline viis:*

<pre>
$ sudo chmod 4755 minufail
</pre>

Nagu näha tähistab SUID'd number 4 ja see lisatakse teiste õiguste ette. SUID võib olla märgitud ka kui suurtäht <b>S</b>, see tähistab sama asja, kuid ei hõlma endas käivitamise õigust.

Õiguste arvutamiseks on loodud ka mitmeid veebipõhiseid vahendeid, üks näide on <a target="_blank" href="http://permissions-calculator.org/">http://permissions-calculator.org/</a>

## Harjutus

Vaadata */etc/passwd* õigusi detailselt. Mida veel võib märgata? Failid, millele on seatud SUID on teistest kergesti eristatavad.

## Küsimus

Milline number tähistab SUID'd?

## Vastus

4
