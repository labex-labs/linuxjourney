# head

## Tunni sisu

Ütleme, et meil on väga pikk fail, meil on isegi mitu, mille hulgast valida, proovida cat /var/log/syslog. Peaks nägema lehekülgede kaupa teksti.  Mis siis kui tahta näha ainult paari esimest tekstifaili rida? Seda saab teha käsuga head. Vaikimisi näitab head käsk faili esimest 10 rida.

<pre>$ head /var/log/syslog</pre>

Saab ka muuta ridade arvu sobivaks. Näiteks soovime näha hoopis esimest 15 rida.

<pre>$ head -n 15 /var/log/syslog</pre>

Lipp -n esindab ridade arvu.

## Harjutus

Mida teeb järgnev käsk ja miks?

<pre>$ head -c 15 /var/log/syslog</pre>

## Küsimus

Millist lippu kasutad, kui tahad muuta head käsuga vaadeldavate ridade arvu?

## Vastus

-n

