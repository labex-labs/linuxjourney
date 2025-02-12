# Protsesside peatamine

## Tunni sisu

Õppisime, mis toimub kui protsesse luuakse kuid mis saab siis kui neid enam vaja pole? Ole hoiatatud, Linux kipub vahel veidi süngeks...

Protsessist võib väljuda kasutades *_exit* süsteemset kutset. Sellisel juhul vabastatakse protsessi ressursid ümberjaotamise tarbeks. Kui protsess on valmis oma tööd lõpetama, annab ta tuumale teada lõpetamise põhjuse läbi lõpetamise oleku. Tavaliselt tähendab 0, et protsess oli edukas. Kuid sellest ei piisa, et protsessi tööd lõpetada. Vanemprotsess peab tütre töö lõpetamist tunnistama kasutades selleks *wait* süsteemset kutset, mis kontrollib tütarprotsessi töö peatamise olekut. Võib ju tunduda julm, aga *wait* kutse on paratamatult vajalik, sest milline vanem ei tahaks teada, kuidas nende laps suri?

On veel üks viis protsessi peatamiseks, mis hõlmab signaalide kasutamist, millest räägitakse õige pea.

<b>Hüljatud protsessid</b>

Kui vanemprotsess peaks surema enne kui tütarprotsess, siis tuum teab, et *wait* kutset ei tule. Need protsessid nimetatakse orbudeks ja antakse *init*'i hoole alla (mäletatavasti kõikide protsesside ema). *Init* teostab mingil hetkel ikkagi *wait* kutse, nii et need hüljatud protsessid saavad ka ära lõppeda.

<b>Zombiprotsessid</b>

Mis juhtub aga kui tütar on peatunud aga vanemprotsess pole veel *wait* kutset teostanud? Soovime sellegipoolest teada kuidas see juhtus ning hoolimata sellest, et tütarprotsess oma tegevuse lõpetas, muudab tuum ta zombiprotsessiks. Tütarprotsessi ressursid on ikkagi vabastatud, kuid protsesside tabelis on selle zombi kohta endiselt kanne. Zombiprotsesse ei saa "tappa", st sunniviisiliselt peatada, kuna nad on juba tegelikult peatunud. Zombide tapmiseks kasutatakse signaale. Kui lõpuks vanemprotsess selle *wait* süsteemse kutse teostab, saab zombi kaduda, seda protsessi nimetatakse *reaping* (lõikus). Kui vanem *wait* kutset ei teosta, lapsendab *init* selle zombi ja teeb seda automaatselt ise, mille järel zombi eemaldatakse. Zombide üleküllus võib olla väga halb, kuna nad võtavad tabelis ruumi ning seega ei võimalda teistel protsessidel töötada.

## Harjutus

Selles peatükis harjutuse pole.

## Küsimus

Milline on kõige tavalisem edukalt töö lõpetanud protsessi peatumise staatus?

## Vastus

0
