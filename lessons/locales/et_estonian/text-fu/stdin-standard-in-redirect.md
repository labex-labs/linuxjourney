# stdin (Standard In)

## Tunni sisu

Eelmises tunnis õppiti, et saab kasutada erinevaid *stdout* (standardväljundi) vooge, näiteks faili või ekraani. Samamoodi on olemas ka standardsisendi (*stdin*) vood. Teame, et on olemas *stdin* seadmetelt nagu klaviatuur, kuid võib kasutada ka faile, teiste protsesside väljundeid ning ka terminali. Vaatame näidet.

Kasutame selle näite jaoks eelmise tunni *pähklid.txt* faili. Meenutame, et seal oli sees tekst *Hello World*.

<pre>$ cat <b>&lt;</b> pähklid.txt <b>&gt;</b> banaan.txt </pre> 

Nii nagu <b>&gt;</b> on *stdout* (standardväljundi) ümbersuunamiseks, on <b>&lt;</b> *stdin* (standardsisendi) ümbersuunamise jaoks.

Tavaliselt saadetakse *cat* käsu puhul fail sisendisse ja sellest saab *stdin* (standardsisend), praegusel juhul aga suunasime me *stdin*'ks *pähklid.txt*. Sedasi suunatakse *cat pähklid.txt* väljund ümber faili mimega *banaan.txt*

## Harjutus

Proovida paari käsku:
<pre>
$ echo <b>&lt;</b> pähklid.txt <b>&gt;</b> banaan.txt
$ ls <b>&lt;</b> pähklid.txt <b>&gt;</b> banaan.txt
$ pwd <b>&lt;</b> pähklid.txt <b>&gt;</b> banaan.txt
</pre>

## Küsimus

Millise käsuga suunatakse ümber *stdin* (standardsisend)?

## Vastus

<
