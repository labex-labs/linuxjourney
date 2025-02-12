# System V teenus

## Tunni sisu

Sys V teenuste haldamiseks on võimalik kasutada mitmeid käsurea tööriistu.

<b>Kuva teenused</b>

<pre>$ service --status-all</pre>

<b>Käivita teenus</b>

<pre>$ sudo service networking start</pre>

<b>Peata teenus</b>

<pre>$ sudo service networking stop</pre>

<b>Taaskäivita teenus</b>

<pre>$ sudo service networking restart</pre>

<b>Kuva teenuse olek</b>

<pre>$ sudo service networking status</pre>

Need käsud ei ole *Sys V init* süsteemile spetsiifilised, nendega võib hallata ka *Upstart* teenuseid. Kuna Linux püüab liikuda eemale traditsioonilisematest *Sys V* skriptidest, on tehtud üleminek võimalikult lihtsaks.

## Harjutus

Halda mõnda teenust ja muuda nende olekuid. Mida võib märgata?

## Küsimus

Millise *Sys V* käsuga saab peatada teenuse moos?

## Vastus

*sudo service moos stop*

