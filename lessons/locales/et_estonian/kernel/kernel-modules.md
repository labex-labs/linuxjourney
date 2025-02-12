# Tuuma moodulid

## Tunni sisu

Ütleme, et mul on uhke auto, ma olen sinna investeerimud palju aega ja raha. Lisan tagaspoileri, veokonksu, rattaraami ja veel igasuguseid asju. Need komponendid ei muuda tegelikult auto keskset toimimist ning ma võin neid lisada ja eemaldada väga lihtsalt. Tuum kasutab sama kontseptsiooni moodulitega.

Tuum iseenesest on üks monoliitne tükk tarkvara. Kui me tahame lisada tuge uut tüüpi klaviatuurile, ei kirjuta me seda otse tuuma koodi. Just nagu me ei keevita rattaraami auto külge (kes teab, vahest mõni inimene tahab seda teha). Tuuma moodulid on tükid koodi, mida saab nõudmisel tuumale peale laadida ja eemaldada. Moodulid lasevad meil laiendada tuuma funktsionaalsust ilma, et peaks sekkuma tuuma kesksesse koodi. Mooduleid saab lisada ka ilma süsteemi taaskäivitamata (enamustel juhtudel).

<b>Kuva nimekiri hetkel laetud moodulitest</b>

<pre>$ lsmod</pre>

<b>Lae moodul></b>

<pre>$ sudo modprobe bluetooth</pre>

*Modprobe* laeb mooduli kataloogist <b>/lib/modules/(tuuma versioon)/kernel/drivers</b>. Tuuma moodulitel võivad samuti olla sõltuvused, *modprobe* laeb moodulite sõltuvused, kui nad veel laetud ei ole.

<b>Mooduli eemaldamine</b>

<pre>$ sudo modprobe -r bluetooth</pre>

<b>Laadimine alglaadimisel</b>

Mooduleid saab laadida ka süsteemi alglaadimisel, selle asemel, et neid ajutiselt *modprobe* abil laadida (taaskäivitamisel jälle eemaldatakse). Tuleb lihtsalt modifitseerida kataloogi <b>/etc/modprobe.d</b> ja lisada sinna sätete fail sedasi:

<pre>pete@icebox:~$ /etc/modprobe.d/maasikamoos.conf

options maasika_moos type=parim
</pre>

Natuke ebaraalne näide, kuid kui oleks moodul nimega maasika_moos ja oleks vaja lisada tuuma parameeter type=parim, saaks seda laadida alglaadimisel selle sättefailiga. Olgu ära märgitud, et moodulitel on isiklikud tuuma parameetrid, seega peaks mooduli kohta lugema, et nendest rohkem teada saada.

<b>Alglaadimisel mitte laadida</b>

Võib hoolitseda ka selle eest, et moodulit kindlasti ei laetaks alglaadimisel, lisades sättefaili:

<pre>pete@icebox:~$ /etc/modprobe.d/maasikamoos.conf

blacklist maasika_moos
</pre>

## Harjutus

Eemalda modprobe abil bluetooth moodul ja vaata, mis juhtub. Kuidas seda uuest korda teha?

## Küsimus

Millise käsuga eemaldatakse moodul?

## Vastus

*modprobe -r*


