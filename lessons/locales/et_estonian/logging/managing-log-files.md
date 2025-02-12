# Logifailide haldamine

## Tunni sisu

Logifailid toodavad palju andmeid ja neid hoitakse kasutaja kõvakettal. Sellega seoses tekivad probleemid. Enamasti soovib kasutaja näha uuemaid logisid, samuti tahetakse hallata kettaruumi efektiivselt. Kuidas seda aga teha? Vastus on haldusvahendis logrotate.

Logrotate haldab kasutaja eest tema logifaile. Sätete failis saab täpsustada kui palju ja milliseid logisid alles hoida, kuidas nende mahtu vähendada, et kettaruumi säästa ja palju muud. Logrotate käivitatakse tavaliselt läbi CRON'i korra päevas ning selle sätete failid leiab */etc/logrotate.d/* kataloogist.

*Logrotate*'ile sarnaseid tööriistu logide haldamiseks leidub veel kuid *logrotate* on kõige levinum.

## Harjutus

Tutvuda *logrotate* sätete failiga ning tuvastada kuidas see haldab mõningaid logisid.

## Küsimus

Milline on levinuim logide haldamise vahend?

## Vastus

*logrotate*
