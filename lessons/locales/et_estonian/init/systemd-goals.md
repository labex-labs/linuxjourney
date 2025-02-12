# Systemd sihtkohad

## Tunni sisu

*Systemd* üksuse failide kirjutamise osas siin kursusel detailidesse ei minda. Selle eest vaatame kergelt üle üksuste failid ja kuidas käsitsi üksusi kontrollida.

Tavapärane teenuse üksuse fail: foobar.service

<pre>
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
</pre>

Tegu on lihtsa teenuse sihtkohaga. Faili alguses näeme sektsiooni *[Unit]*, mis lubab kasutajal määrata üksuse failile kirjelduse ja ka kontrollida üksuse käivitumise korraldusi. Järgmine on *[Service]* osa, mille all saab teenust käivitada, peatada või taaslaadida. *[Install]* osa kasutatakse sõltuvuste jaoks. Ja see on alles *systemd* failide kirjutamise jäämäe tipp, mistõttu võib teadmisjanulisem õpilane teema kohta juurde lugeda.

Mõned käsud, mida saab kasutada *systemd* üskustega:

<b>Kuva teenused</b>

<pre>$ systemctl list-units</pre>

<b>Kuva teenuse olek</b>

<pre>$ systemctl status networking.service</pre>

<b>Käivita teenus</b>

<pre>$ sudo systemctl start networking.service</pre>

<b>Peata teenus</b>

<pre>$ sudo systemctl stop networking.service</pre>

<b>Taaskäivita teenus</b>

<pre>$ sudo systemctl restart networking.service</pre>

<b>Luba teenus</b>

<pre>$ sudo systemctl enable networking.service</pre>

<b>Keela teenus</b>

<pre>$ sudo systemctl disable networking.service</pre>

Kordame, et *systemd* sügavused on alles paljastamata, mistõttu tuleb õpilasel ise juurde õppida.

## Harjutus

Kuvada teenuste olekuid, käivitada ja peatada teenuseid. Mida võib märgata?

## Küsimus

Millise käsuga saab käivitada teenuse nimega *moos.service*?

## Vastus

*sudo systemctl start moos.service*
