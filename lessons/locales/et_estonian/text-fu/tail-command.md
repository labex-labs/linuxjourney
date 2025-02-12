# tail

## Tunni sisu

Sarnaselt head käsuga, laseb *tail* käsk vaadata vaikimisi etteantud faili viimast 10 rida.

<pre>$ tail /var/log/syslog</pre>

Just nagu head puhulgi saab muuta, mitu rida kuvatakse.

<pre>$ tail -n 10 /var/log/syslog</pre>

Teine hea variant on kasutada *-f* (*follow* ehk järgi) lippu. See jälgib faili jooksvalt, kui see peaks kasvama. Proovida ja vaadata, mis juhtub.

<pre>$ tail -f /var/log/syslog</pre>

Kui süsteemi aktiivselt kasutada, muutub *syslog* fail pidevalt. *tail -f* käsu kasutamisega näeb kõike, mida sinna parasjagu lisatakse.

## Harjutus

Vaadata tail käsu *man* lehekülge ja uurida mõne käsu kohta, mida me ei tutvustanud.

<pre>$ man tail</pre>

## Küsimus

Millist lippu kasutakse faili jooksvaks jälgimiseks?

## Vastus

*-f*
