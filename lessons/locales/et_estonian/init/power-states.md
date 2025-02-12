# Süsteemi olekud

## Tunni sisu

Natuke raske uskuda, et veel ei ole arutatud süsteemi oleku käsurea kaudu konktrollimise viise. Kuid rääkides *init*ist räägime lisaks süsteemi käivitamise režiimidest kuid ka nendest, millega süsteemi peatada.

Süsteemi peatamiseks:

<pre>$ sudo shutdown -h now</pre>

Kuid võib kasutada ka sulgemise käsku:

<pre>$ sudo poweroff</pre>

See lülitab süsteemi välja, täpsustama peab, millal see peab aset leidma. Lisada võib aja minutites, mille möödudes süsteem lõpetab töö.

<pre>$ sudo shutdown -h +2</pre>

Selline käsk lülitab süsteemi välja kahe minuti möödudes. *Shutdown* käsuga saab teostada ka taaskäivitamist.

<pre>$ sudo shutdown -r now</pre>

Kuid võib kasutada ka taaskäivitamise käsku:

<pre>$ sudo reboot</pre>

## Harjutus

Mõtiskleda, mis toimub *init*'iga süsteemi sulgemisel.

## Küsimus

Millise käsuga lülitatakse süsteem välja 4 minuti möödumisel?

## Vastus

*sudo shutdown -h +4*
