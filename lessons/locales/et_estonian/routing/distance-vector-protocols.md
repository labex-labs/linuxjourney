# Kaugusvektori protokollid

## Tunni sisu

Kaugusvektori protokollid määravad paketi teekonna välistesse võrkudesse kasutades hüpete kogust. Kui võrk A on kolme hüppe kaugusel ja võrk B on kohe võrgu A kõrval siis eeldame, et võrk B on nelja hüppe kaugusel. Kaugusvektori protokollide puhul valitakse marsruudiks vähemate hüpetega marsruut.

Kaugusvektori protokollid sobivad paremini väikestele võrkudele kui võrgud muutuvad suuremaks, võtab lõimumine rohkem aega kuna perioodiliselt saadetakse marsruutimistabel välja kõikidele marsruuteritele. Kaugusvektori protokollid on ka ebaefektiivsemad kuna valivad marsruudi, mis on hüpete poolest lähemal hoolimata sellest kas see on ka tegelikult kiireim tee.

Kõige tavalisem kaugusvektori protokoll on RIP (*Routing Information Protocol*) ehk marsruutimisinformatsiooni protokoll. See saadab marsruutimistabeli kohta leviedastuse sõnumeid kõikidele marsruuteritele iga 30 sekundi tagant. Suuremates võrkudes hakkab see nõudma rohkelt ressurssi. RIP on piiratud maksimaalselt 15 hüppega.

## Harjutus

Harjutust pole.

## Küsimus

Õige või vale? Kaugusvektorprotokollide marsruutimisotsused põhinevad ribalaiusel?

## Vastus

vale
