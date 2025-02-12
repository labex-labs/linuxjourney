# Õiguste tasemed

## Tunni sisu

Järgmised paar õppetundi on üsna teoreetilised. Kui on suurem huvi praktiliste asjade vastu võib esialgu natuke ette rutata ja hiljem siia tagasi pöörduda.

Milleks eraldame operatsioonisüsteemis üksteisest kasutaja ja tuuma? Miks mitte neid kujutada ühe kihina? Nende kahe eraldi eksisteerimiseks on väga hea põhjus. Nad mõlemad opereerivad erinetel režiimidel. Tuum töötab tuuma režiimis ja kasutaja kasutaja režiimis.

Tuuma režiimis on tuumal täielik ligipääs riistvarale, see kontrollib kõike. Kasutaja režiimis antakse kasutajale väga väike turvaline kogus mälu ja protsessori ligipääsuõigust. Põhimõtteliselt kui miski hõlmab riistvara, andmete lugemist või kirjutamist ketastelt, võrgu kontrollimine ja muu siis see kõik toimub tuuma režiimis. Miks see aga vajalik on? Kujutleme, et arvutit tabab nuhkvara - me ju ei tahaks, et see saaks otsese ligipääsu süsteemi riistvarale. See saaks ligi kõikidele andmetele, võrgukaamerale ja muule ja see ei oleks üldsegi hea.

Neid erinevaid režiime nimetatake õiguste tasemeteks (selle järgi kui palju õigusi kasutajal on) ja neid kujutatakse tihti kaitsvate ringidena. Et sellest oleks kergem aru saada, kujutle, et Britney Spears on sinu kohalikus klubis, teda kaitsevad tema *groupie*d, seejärel turvamehed ja ka väljaviskaja klubi uksel. Sa tahad tema autogrammi (sest miks mitte?) kuid sa ei saa talle ligi, sest ta on korralikult turvatud. Operatsioonisüsteemi ringid toimivad sama moodi. Kõige sisemine ring on vastav kõige suurematele õigustele. x86 arvuti arhitektuuris on kaks peamist režiimi. Ring #3 on õigused, milles töötavad kasutaja režiimi rakendused. Ring #0 on õigused, milles töötab tuum. Ring #0 võib käivitada iga süsteemi juhise ja sellele kuulub täielik usaldus. Kas ehk tekib nüüd küsimus, et kuidas ma siis üldse midagi riistvarale kirjutada saame? Kas me pole siis alati tuumast erinevas režiimis?

Vastus on süsteemsetes kutsetes. Need lubavad meil teostada asju tuuma režiimis ja siis pöörduda tagasi kasutaja režiimi.

## Harjutus

Harjutust pole.

## Küsimus

Millise numbriga ringil on suurimad õigused?

## Vastus

0
