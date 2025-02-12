# Töö kontroll

## Tunni sisu

Ütleme, et töötatakse terminali aknas ja käivitatud on käsk, mille täitmiseks kulub lõpmata palju aega. Kestprogrammi ei saa kasutada nii kaua kui see oma ülesandega valmis saab, soov on aga tööga jätkata. Õnneks saab kontrollida kuidas protsessid töödega töötavad:

<b>Töö tagaplaanile saatmine</b>

Ampersandi (&) lisamisel käsule käivitub protsess tagaplaanil, võimaldades kestprogrammi edasi kasutada. Näide:

<pre>$ sleep 1000 &
$ sleep 1001 &
$ sleep 1002 &
</pre>

<b>Tagaplaanil olevate tööde kuvamine</b>

Tagaplaanile saadetud töid saab vaadata.

<pre>$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &

</pre>

Kui mõni töö juba käib ja vaja on ta tagaplaanile saata, pole vaja teda peatada ja siis uuesti käivitada. Peata töö ajutiselt klahvikombinatsiooniga Ctrl-Z, see järel sisesta <b>bg</b> käsk, mis saadab töö tagaplaanile.

<pre>
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &

pete@icebox ~ $ jobs

[1]    Running     sleep 1000 &
[2]    Running     sleep 1001 &
[3]-   Running     sleep 1002 &
[4]+   Running     sleep 1003 &
</pre>

<b>Töö tagaplaanilt esiplaanile toomine</b>

Et tuua töö tagaplaanilt ära on vaja täpsustada vaid töö ID. Kui sisestada *fg* ilma täpsustusteta tuuakse tagasi kõige hilisem taustatöö (töö mille juures on +).

<pre>$ fg %1</pre>

<b>Tagaplaanil olevate tööde peatamine </b>

Tööde esiplaanile liigutamise käsule sarnases formaadis on ka nende peatamise käsk, ikka kasutades ID'd.

<pre>kill %1</pre>

## Harjutus

Liigutada töid esi- ja tagaplaani vahel.

## Küsimus

Millise käsuga näeb tagaplaani töid?

## Vastus

*jobs*
