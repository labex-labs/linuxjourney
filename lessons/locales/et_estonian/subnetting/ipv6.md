# IPv6

## Tunni sisu

Mis asi on see IPv6, millest nii palju kuuldud on? Igal seadmel, mis ühendub Internetti, on isiklik IP aadress. IP aadresse on aga juhtumisi lõplik arv ning tegelikult on viimased IPv4 aadressid ka juba regionaalsetele Interneti registritele välja jagatud. IPv6 loodigi selleks, et ühendada rohkem hoste Internetti, samuti on sellelel protokollil palju täiustusi eelkäijaga võrreldes. Algselt ei olnud IPv6 eesmärk IPv4 välja vahetada kuid maailm võtab juba tasapisi uut protokolli omaks. Kaks protokolli on tegelikult üksteisele üsna sarnased, seega kui IPv4 on arusaadav, mõistab kindlasti ka IPv6'te. Peamine erinevus seisneb selles, kuidas aadressi kirja pannakse. Tüüpiline IPv6 aadress näeb välja selline:

<pre>
2dde:1235:1256:3:200:f8ed:fe23:59cf
</pre>

IPv6 aadresside vaatamine (vaata *inet6* väärtust) - vali üks neist:<br>
<pre>
ip -6 a
ifconfig -a
ifconfig -a | grep inet6
</pre>

IPv4 aadressruum on 32-bit: 2<sup>32</sup> (~4,3 miljardit)<br>
IPv6 aadressruum on 128-bit: 2<sup>128</sup> (~3,4*10<sup>38</sup>)<br>
Suurte arvude nimede osas ei ole maailmas üksmeelt <a target="_blank" href="https://en.wikipedia.org/wiki/Names_of_large_numbers">https://en.wikipedia.org/wiki/Names_of_large_numbers</a>

IPv6 tutvustav video <a target="_blank" href="https://www.youtube.com/watch?v=2wa7y3W2DI0">https://www.youtube.com/watch?v=2wa7y3W2DI0</a>

## Harjutus

Kontrollida *ifconfig* käsuga, kas arvutile on määratud IPv6 aadress.

## Küsimus

Millise protokolliga suurendatakse Internetti ühenduvate hostide arvu?

## Vastus

IPv6
