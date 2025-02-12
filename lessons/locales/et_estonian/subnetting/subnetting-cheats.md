# Alamvõrkude spikker

## Tunni sisu

See peatükk on natuke kahtlase väärtusega kuna tõenäoliselt ei ole kunagi vaja käsitsi alamvõrke arvutada kuid ütleme, et meid tabab äkitselt mingi selleteemaline intervjuu siis oleks hea osata teisendada detsimaali ja binaari vahel. Õnneks on olemas aritmeetiline spikker, et sellega aidata.

Alustuseks tuleb õppida ära esimesed kahe astmed:

<ul>
<li>2<sup>1</sup> = 2</li>
<li>2<sup>2</sup> = 4</li>
<li>2<sup>3</sup> = 8</li>
<li>2<sup>4</sup> = 16</li>
<li>2<sup>5</sup> = 32</li>
<li>2<sup>6</sup> = 64</li>
<li>2<sup>7</sup> = 128</li>
<li>2<sup>8</sup> = 256</li>
<li>2<sup>9</sup> = 512</li>
<li>2<sup>10</sup> = 1024</li>
<li>2<sup>11</sup> = 2048</li>
<li>2<sup>12</sup> = 4096</li>
</ul>

<b>Detsimaalist binaari</b>

<pre>
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
</pre>

On väga palju põhjuseid miks see graafik näeb välja just selline, huvi korral võib Internetist leida hulgaliselt materjale.

Jäi see kõik pähe? Nüüd siis kiire detsimaalist binaari teisendus:

<b>Teisendame binaaresitusse 192.168.23.43</b>

Meenutame: 128 / 64 / 32 / 16 / 8 / 4 / 2 / 1

Teeme koos läbi esimese okteti teisendamise ja see asi saab kiiresti selgeks.

<ol>
<li>Saame lahutada 192 - 128? Jah, seega esimene bitt on 1</li>
<li>192 - 128 = 64, järgmine number graafikus on 64, kas saame lahutada 64 - 64?Jah, seega teine bitt on 1</li>
<li>Kuna numbrid mida lahutada said otsa siis arvu 192 binaaresitus on 11000000</li>
</ol>

<b>Teisendame detsimaalesitusse 11000000</b>

Selleks liidame kokku need arvud, kus bitt on 1:

128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 = 192!

Tulemusi võib kontrollida näiteks aadressil <a target="_blank" href="http://jodies.de/ipcalc">http://jodies.de/ipcalc</a>

## Harjutus

Tuvastada arvuti IP aadress ja alamvõrgu mask ning arvutada maksimaalne hostide arv enda võrgus.

## Küsimus

Kuidas on arvu 123 binaaresitus?

## Vastus

11111011
