# sort

## Tunni sisu

*Sort* käsk on kasulik ridade sorteerimiseks.

<pre>
fail1.txt
koer
lehm
kass
elevant
lind

$ sort fail1.txt
elevant
kass
koer
lehm
lind
</pre>

Saab teha ka tagurpidise sorteerimise:

<pre>$ sort -r fail1.txt
lind
lehm
koer
kass
elevant
</pre>

Samuti ka numbrilise väärtuse põhjal:

<pre>$ sort -n fail1.txt
elevant
kass
koer
lehm
lind
</pre>

## Harjutus

*Sort* käsu tõeline jõud tuleneb võimalusest kasutada seda koos teiste käskudega. Proovida järgmist käsku ja vaadata, mis juhtub?

<pre>$ ls /etc | sort -rn</pre>

## Küsimus

Millise lipuga saab teha tagurpidi sorteerimist?

## Vastus

*-r*
