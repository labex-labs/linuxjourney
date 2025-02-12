# cd (Change Directory)

## Tunni sisu

Vaatame kas meil õnnestub failisüsteemis pisut ringi liikuda teadmistega, mis käesolevaks hetkeks kogutud. Tuleb meeles pidada, et liikumiseks peame kasutama asukohtade otsiteekondi. Asukoha määramiseks on kaks võimalust: absoluutne ja suhteline otsiteekond.

<ul>
<li>Absoluutne otsiteekond: See on asukoht alates juurkataloogist. Juur on meil see kõige olulisem tegelane. Juurkataloogi kuvatakse tavaliselt kaldkriipsuga. Kui asukoha alguses on /, siis tähendab, et alustatakse juurkataloogist. Näiteks <i>/home/pete/Töölaud</i>.</li>

<li>Suhteline otsiteekond: See on asukoht alates praegusest asukohast failisüsteemis. Kui hetkel asutakse <i>/home/pete/Dokumendid</i> ja tahetakse liikuda kataloogis <i>Dokumendid</i> asuvasse <i>arved</i> alamkataloogi, siis ei ole vaja täpsustada kogu asukohta alates juurkataloogist vaid võib otse minna alamkataloogi <i>arved/</i> .</li>
</ul>

Kui on teada kuidas asukohad toimivad siis on vaja midagi, mis aitaks liikuda soovitud kataloogi. Õnneks on olemas *cd* või siis "muuda kataloogi", et seda saavutada.

<pre>$ cd /home/pete/Pildid</pre>

Sellega muudeti asukohaks home/pete/Pildid.

Selles kaustas on aga alamkataloog Hawaii, ma saan sinna liikuda nõnda:

<pre>$ cd Hawaii</pre>

Paneme tähele, et kasutati ainult kausta nime! See on võimalik kuna asukoht juba oli /home/pete/Pildid.

Võib muutuda päris väsitavaks kui kogu aeg peab kasutama absoluutseid või suhtelisi asukohti. Õnneks on meie abistamiseks olemas otseteed.

<ul>
<li>. (praegune kataloog). See on kataloog, milles sa asud</li>
<li>.. (eelnev kataloog). Viib su praeguse kataloogi ülemkataloogi</li>
<li>~ (home kataloog). See on vaikimisi su kodukataloog, näiteks /home/pete</li>
<li>- (eelmine kataloog). Viib su kataloogi, kus sa viimati asusid</li>
</ul>

Kui käsurida on äsja avatud siis ei pruugi ajalugu olla eelnevates kataloogides liikumisest ja seetõttu ei pruugi kohe eelmisesse kataloogi liikumine toimida. Eelmise kataloogi väärtust näeb käsuga:
<pre>
echo $OLDPWD
</pre>

<pre>$ cd .
$ cd ..
$ cd ~
$ cd -
</pre>
Proovi need ära!

<ol>
<li>Kuhu satutakse kui sisestada cd käsk ilma täiendava infota?</li>
</ol>

Lisainfo:<br />
<pre>
man bash-builtins
</pre>

## Küsimus

Kui asukoht on /home/pete/Pildid ja soovitakse minna kataloogi /home/pete, siis millist otseteed oleks hea kasutada?

## Vastus

cd ..
