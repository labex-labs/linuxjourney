# Üldine logimine

## Tunni sisu

Kasutaja süsteemis on päris palju logifaile, enamus olulisi on leitavad kataloogist */var/log/*. Kõiki ei hakata selles peatükis tutvustama kuid mõned olulisemad tulevad siiski jutuks.

Kaks üldist logifaili, mis annavad kasutajale süsteemis toimuvast ülevaate:

<b>/var/log/messages</b>

See logi sisaldab endast kõik mitte-kriitilised ja mitte-silumise teated. Kaasatud on teated, mis on logitud alglaadmise ajal (*dmesg*), *auth, cron, daemon* jpt. Väga kasulik uurimaks, kuidas arvuti käitub.

<b>/var/log/syslog</b>

See logib kõike peale auth teadete. Äärmiselt kasulik kui käsil on vigade otsimine.

Nendest kahest logist on enam kui küll süsteemi seisukorra uurimisel. Kui aga peaks tekkima vajadus mõne konkreetse logi komponendi järgi, on ka need eraldi logidena olemas.

## Harjutus

Vaadata */var/log/messages* ja */var/log/syslog* faile ning märgata nende erinevusi.

## Küsimus

Milline logi logib kõike peale auth teadete?

## Vastus

*syslog*
