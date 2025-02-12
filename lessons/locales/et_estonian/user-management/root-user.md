# Juur

## Tunni sisu

Eelmises peatükis vaadeldi ühte superkasutajale ligipääsemise viisi. Superkasutaja käske saab sisestada ka *su* käsuga. See käsk vahetab kasutaja välja kui kasutajanime ei täpsustata ehk siis avatakse kestprogramm juurõigustes. Selle käsuga saab vahetada kasutajat ükskõik millise vastu, vaja on ainult teada ka vastavat salasõna.

<pre>$ su</pre>

Eks sellel metoodikal on ka pahupool: juurkasutajana töötades on palju lihtsam teha kriitilisi vigu. Näiteks ei peeta arvet nende käskude üle, mida kasutatakse süsteemi seadete muutmiseks jpm. Lihtsamalt öeldes: kui on vaja sisestada käsku superkasutajana, tasub esialgu jääda *sudo* juurde.

Nüüd on selge kuidas sisestada käske superkasutajana. Kuid kuidas teha kindlaks, kellel on selleks õigused? Süsteem ei lase igal Tuha Juhanil superkasutajana käske sisestada. Kuidas ta siis aga teab? On olemas fail */etc/sudoers*, milles on nimekiri kasutajatest kellel on õigus *sudo*t kasutada. Seda faili saab muuta käsuga <b>visudo</b>.

## Harjutus

Avada fail */etc/sudoers* ja vaadata millistel kasutajatel selles masinas on superkasutaja õiguseid.

## Küsimus

Millisest failist saab infot selle kohta, kellel on ligipääsu õigus *sudo*le?

## Vastus

*/etc/sudoers*
