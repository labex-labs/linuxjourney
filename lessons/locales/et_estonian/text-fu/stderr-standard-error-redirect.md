# stderr (Standard Error)

## Tunni sisu

Proovime nüüd midagi natuke teistsugust. Proovime saada sisu loetelu mingist kataloogist, mida ei eksisteeri ja suuname selle info taaskord *pähklid.txt* faili.

<pre>$ ls /olematu/kataloog > pähklid.txt </pre>

Vastuseks on midagi sellist:

<pre>ls: /fake/directory ei ole kättesaadav: Faili või kataloogi ei eksisteeri</pre>

Võib mõelda, et kas see teade ei oleks pidanud saadetama hoopis faili? Tegelikult on olemas veel üks sisend-väljundvoog, standardvea väljund (*stderr*). Vaikimisi saadab *stderr* oma väljundi ka muuhulgas ekraanile, see on *stdout* voost täiesti erinev ning ka selle väljundit tuleb teisiti suunata.

Kahjuks ei ole see ümbersuunamise operaator sama kena, kui <b>&lt;</b> või <b>&gt;</b>, kuid see on üsna sarnane. Tuleb kasutada failikirjeldajat.  Failikirjeldaja on mittenegatiivne number, mida kasutatake faili voole ligipääsemiseks. Me süveneme sellesse hiljem, kuid praegu peab vaid teadma, et failikirjeldaja *stdin, stdout* ja *stderr* jaoks on vastavalt 0, 1 ja 2:
<pre>
0 <i>stdin</i>
1 <i>stdout</i>
2 <i>stderr</i>
</pre>

Seega, kui soovitakse suunata *stderr* ümber faili, saab toimida järgnevalt:

<pre>$ ls /olematu/kataloog 2> pähklid.txt</pre>

Failis *pähklid.txt* on näha ainult *stderr* teadet.

Aga mis saab siis, kui on vaja näha nii *stderr* kui ka *stdout* väljundit *pähklid.txt* failis? Seda saab samuti teha failikirjeldajaga:

<pre>$ ls /olematu/kataloog > pähklid.txt 2>&1</pre>

See käsk saadab *ls /olematu/kataloog* tulemuse failile *pähklid.txt* ja seejärel suunab *stderr* väljundi *stdout*'le kasutades operaatorit *2>&1*. Siin on oluline toimingute järjekord, *2>&1* saadab *stderr*'i millelegi, millele *stdout* viitab. Hetkel viitab see failile. Seega kui avada fail *pähklid.txt*, peaks nägema mõlemat *stderr* ja *stdout* väljundit. Meie näite põhjal on ülemise käsu väljund ainult *stderr*.

Selline on lühem viis kuidas suunata faili mõlemad *stdout* ja *stderr*:

<pre>$ ls /olematu/kataloog &> pähklid.txt</pre>

Aga mis siis, kui ei olegi vaja seda üleliia risustavat infot ja soovitakse *stderr* teatest täielikult vabaneda? Siis võib suunata väljundi spetsiaalsesse faili */dev/null* ja igasugune sisendinfo lihtsalt heidetakse kõrvale.

<pre>$ ls /olematu/kataloog 2> /dev/null</pre>

## Harjutus

Mida teeb allolev käsk?

<pre>$ ls /olematu/kataloog >> /dev/null 2>&1</pre>

## Küsimus

Millist märki kasutatakse *stderr* ümbersuunamiseks?

## Vastus

*2>*
