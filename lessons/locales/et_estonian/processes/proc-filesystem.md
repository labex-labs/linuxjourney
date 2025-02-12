# */proc* failisüsteem

## Tunni sisu

Meenutame, et Linuxis on kõik asjad failid - isegi protsessid. Informatsiooni protsesside kohta hoitakse spetsiaalses failisüsteemis */proc*.

<pre>$ ls /proc</pre>

Sealt paistavad erinevad väärtused, iga PID jaoks on alamkataloog. Kui eelnevalt on *ps* väljundi abil PID tuvastatud, saab selle */proc* kaustast üles otsida.

Sisestame ühe protsessi ja uurime selle faili:

<pre>$ cat /proc/12345/status</pre>

Seal on informatsioon protsesside olekute kohta aga ka palju muud detailset infot. Tuum näeb süsteemi nii nagu see on */proc* kaustas, mistõttu on seal ka oluliselt rohkem infot kui *ps* näitab.

## Harjutus

Selles peatükis harjutust pole.

## Küsimus

Millises failisüsteemis hoitakse infot protsesside kohta?

## Vastus

*/proc*
