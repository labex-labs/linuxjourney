# kill (Peatamine)

## Tunni sisu

Protsessi peatamiseks saadetakse signaal, mida nimetatakse *kill*.

<pre>$ kill 12445</pre>

12445 on peatatava protsessi tunnus (PID). Vaikimisi saadab see TERM signaali. SIGTERM saadetakse aga protsessile, et ta saaks rahulikult oma ressursid vabastada ja oleku salvestada. See on protsessi viisakas sulgemine.

*Kill* käsuga saab signaali ka täpsustada:

<pre>$ kill -9 12445</pre>

See käivitab SIGKILL signaali ja peatab jõuga protsessi töö - siin ei anta aega olekut salvestada vaid lõpetatakse protsessi töö koheselt ning jõuga ja samuti vabastatakse ressursid jõuga.

<b>Erinevused SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP vahel?</b>

Need signaalid kõlavad kõik üsna sarnaselt kuid on siiski erinevad.

<ul>
<li><i>SIGHUP (1)</i> - saadetakse protsessile kui kontrollterminal on suletud. Näiteks kui sulgeda terminali aken, milles protsess alles töötas, siis saadetakse SIGHUP signaal.</li>
<li><i>SIGINT (2)</i> - See on vahelesegamise signaal. Kui sisestad klahvikombinatsiooni Crtl-C püüab süsteem viisakalt protsessi peatada.</li>
<li><i>SIGTERM (15)</i> - Peata protsess aga lase tal enne korralikult enda järelt ära koristada</li>
<li><i>SIGKILL (9)</i> - Peata protsess, peata vahendeid valimata, mingist koristamisest pole juttugi</li>
<li><i>SIGSTOP (19)</i> - Peatab protsessi ajutiselt </li>
</ul>

Kõigi signaale ja nende numbrilisi väärtusi näeb näiteks kui paigaldada programm *htop* ja mõne protsessi peal vajutada F9 (katkestamiseks *ESC*).

## Harjutus

Peatada protsesse erinevate signaalidega.

## Küsimus

Milline on vaikimisi peatamise signaal?

## Vastus

*SIGTERM*

