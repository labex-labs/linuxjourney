# rm (Remove)

## Tunni sisu

Nüüd kui mulle tundub, et meil on liiga palju faile, eemaldaks mõned. Selleks, et faile eemaldada, kasutame *rm* käsku. *Rm* (inglise keeles *remove* ehk eemalda) käsku kasutatakse, et kustutada faile ja katalooge.

<pre>$ rm fail1</pre>

**Ole *rm* kasutamisega ettevaatlik**, ei ole olemas maagilist prügikasti kust hiljem eemaldatud faile välja õngitseda. Kui nad on läinud, siis on nad igaveseks läinud, seega ole tähelepanelik.

Õnneks on üles seatud turvameetmed, et päris igaüks ei saaks eemaldada olulisi faile. Kirjutamise vastu kaitstud failid küsivad kinnitust enne, kui nad ära kustutada. Samuti ei ole kirjutamise vastu kaitstud kataloogi niisama lihtne eemaldada.

Kui kõik see eelnev ei huvita, siis saab faile igal juhul eemaldada.

<pre>$ rm -f fail1</pre>

-f (inglise keeles *force* ehk jõuga) valik ütleb rm käsule, et see eemaldaks kõik failid hoolimata sellest, kas nad on kirjutuskaitstud või mitte. Seda ilma, et eelnevalt üle küsitakse (kui selleks on vastavad volitused).

<pre>$ rm -i fail</pre>

Sarnaselt teistele käskudele, annab lipu *-i* lisamine enne faili või kataloogi kustutamist võimaluse valida, kas ikka soovitakse seda teha.

<pre>$ rm -r kataloog</pre>

Kataloogi ei saa niisama lihtsalt eemaldada, vaja on lisada lipp *-r* (rekursiivne), et eemaldatakse kõik failid ja alamkataloogid, mis seal olla võivad.

Kataloogi saab eemaldada *rmdir* käsuga.

<pre>$ rmdir kataloog</pre>

## Harjutus

<ol>
<li>Luua fail nimega <i>-fail</i> (ära unusta sidekriipsu!).</li>
<li>Eemalda see fail.</li>
</ol>

## Küsimus

Kuidas eemaldada fail nimega *minufail*?

## Vastus

*rm minufail*
