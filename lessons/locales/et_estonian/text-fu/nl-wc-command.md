# wc ja nl

## Tunni sisu

wc (word count ehk sõnade loendus) käsk kuvab faili täieliku sõnade hulga.

<pre>$ wc /etc/passwd
 96     265    5925 /etc/passwd
</pre>

Vastavalt väljundile on kuvatud ridade, sõnade ja baitide arv.

Selleks, et ainult ühte välja kuvataks, kasuta vastavalt *-l, -w* või *-c*.

<pre>$ wc -l /etc/passwd
96</pre>

Veel üks käsk, millega saab faili ridade arvu teada, on <i>nl</i> (<i>number lines</i> ehk ridade number).

<pre>
fail1.txt
mulle
meeldivad
kilpkonnad
</pre>

<pre>$ nl file1.txt
1. mulle
2. meeldivad
3. kilpkonnad
</pre>

## Harjutus

Kuidas saab *nl* käsku kasutades faili lõpliku ridade arvu ilma, et peaks kogu väljundit läbi vaatama? Vihje: Kasuta mõningaid teisi käske, mida sellel kursusel juba õppinud oled.

## Küsimus

Millist käsku kasutaksid, et saada failist ainult lõplik sõnade arv.

## Vastus

*wc -w*
