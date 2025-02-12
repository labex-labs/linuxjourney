# Protsesside õigused

## Tunni sisu

Lipsame nüüd korraks protsesside õiguste teemasse. Meenutame, et kui sisestada passwd käsk, millel on lubatud SUID bitt, on võimalik programm käivitada juurkasutajana. Kui see on tõsi, et ajutiselt ollakse juurkasutaja kas siis on võimalik ka teiste kasutajate salasõnu muuta? Kahjuks see nii pole.

See on nii Linuxis teostatavate erinevate UID'de tõttu. Iga protsessiga on seostatud kolm UID'd.

Kui protsess käivitada, töötab see käivitanud kasutaja või grupi õigustes. Seda tuntakse *kehtiva UID'na*, millega antakse protsessidele ligipääsuõigused. Seega kui Jaanus sisestaks *touch* käsu, töötaks protsess ja kõik loodavad failid tema õigustes ja tema omandina.

On olemas ka *tegelik UID*, mis on protsessi käivitaja ID. Sellega tuvastatakse, milline kasutaja käivitas protsessi.

*Salvestatud UID* võimaldab protsessidel edukalt vahetada kehtiva ja efektiivse UID vahel ning ka vastupidi. See on vajalik kuna ei ole soovitav, et protsess töötab pidevalt kõrgendatud õigustes. Hea tava kohaselt kasutatakse spetsiaalseid õigusi kindlatel aegadel.

Paneme selle nüüd kõik kokku ja vaatame uuesti *passwd* käsku.

Käivitades *passwd* käsu on kehtiv UID kasutaja ID, ütleme praegu, et see on 500. Kuid *passwd*'l on SUID õigus lubatud. Seega seda käivitades on kehtiv UID 0 (0 on juurkasutaja UID). Sedasi saab programm failidele ligi juurkasutajana.

Ütleme, et kasutaja läheb võimuahneks ja tahab muuta Liisi salasõna. Tema UID on aga 600. Kasutajal ei vea, kuna kahjuks on protsessil ka tema tegelik UID, meie näites 500. Kuna on kasutaja ID on teada, ei lubata teistsuguse UID (600) parooli muuta. (Loomulikult saab sellest mööda minna olles juurkasutaja ja omades kõige kontrollimise ja muutmise õigusi).

Sisestades *passwd*, käivitub protsess kasutades kasutaja tegelikku UID'd ning salvestatakse faili omaniku UID (kehtiv UID), mistõttu saab nende kahe vahel kergesti vahetada. Pole mingit põhjust muuta kõiki faile juurkasutaja õigustega kui see pole otseselt vajalik.

Enamasti on tegelik ja kehtiv UID samad kuid juhtudel nagu *passwd* see muutub.

## Harjutus

Protsessidest ei ole küll veel räägitud kuid siiski võib vaadelda järgnevat muutust reaalajas:

<ol>
<li>Avada üks terminali aken ja sisestada käsk <b>watch -n 1 "ps aux | grep passwd"</b>. See hakkab jälgima <b>passwd</b> protsessi.</li>
<li>Avada teine terminali aken ja sisestada <b>passwd</b></li>
<li>Kui vaadata esimest terminali akent võib näha <b>passwd</b> protsessi. Tabeli esimene veerg on kehtiv UID. Vaata aga! See on juurkasutaja.</li>
</ol>

## Küsimus

Milline UID määrab antavad õigused?

## Vastus

kehtiv
