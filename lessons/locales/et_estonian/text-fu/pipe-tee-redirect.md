# toru ja tee

## Tunni sisu

Nüüd hakkame natuke torustikuga tegelema. No mitte päris, aga natuke ikkagi. Proovime käsku:

<pre>$ ls -la /etc</pre>

Peaks nägema väga pikka nimekirja, mida on isegi natuke raske lugeda. Selle asemel, et seda faili suunata, kas ei oleks toredam, kui saaksime seda väljundit vaadata mõne teise käsga nagu less? Aga saamegi!

<pre>$ ls -la /etc | less </pre>

Toru operaator |, mida esindab püstkriips, lubab meil saada mõne käsu *stdout* (standardväljund või kõnekeeles ka väljund) ja teha sellest teisele protsessile *stdin* (standardsisend või kõnekeeles ka sisend). Meie näite puhul võtsime *ls -la /etc* väljundi ja siis suunasime <i>toruga</i> *less* käsu sisendisse. Toru operaator on äärmiselt kasulik ja me jätkame selle kasutamist aegade lõpuni.

Aga kui on vaja kirjutada käsu väljund kahele erinevale voole? See on võimalik järgmise käsuga:

<pre>$ ls | tee pähklid.txt</pre>

*ls* väljund on näha ekraanil ja kui avada *pähklid.txt* fail, näeb seal täpselt sama sisu!
 

## Harjutus

Proovida järgmist käsku:
<pre>$ ls | tee pähklid.txt banaan.txt</pre>

## Küsimus

Milline sümbol esindab toruoperaatorit?

## Vastus

|
