# Süsteemi logimine

## Tunni sisu

Teenused, tuum, deemonid jms kasutaja süsteemis on pidevalt tegevuses. Sellekohased andmed salvestatakse tegelikult logide kujul. Inimloetavates logides hoitakse informatsiooni sündmuste kohta, mis süsteemis toimuvad. Neid andmeid hoitakse tavaliselt kataloogis */var*, kus hoitakse muutuvaid andmeid, logid on üks näide.

Kuidas selliseid sõnumeid süsteemis üldse vastu võetakse? On olemas teenus nimega *syslog*, mis saadab informatsiooni süsteemi logijale.

*Syslog* koosneb tegelikult mitmest komponendist. Üks olulisematest on deemon nimega *syslogd* (uuemates Linuxites kasutatakse *rsyslogd*), mis ootab sündmuste teateid ja nende ilmnemisel filtreerib välja enda jaoks olulised. Sõltuvalt sellest, mis sõnumiga peab peale hakkama - see saadetakse kas faili, konsooli või siis ei tehta sellega midagi.

Võiks ju arvata, et see süsteemi logija ongi keskne logide haldamise koht. Kuid kahjuks see ei ole nii. Leidub palju rakendusi, mis kirjutavad isiklikud reeglid ja toodavad erinevaid logifaile. Sellest hoolimata, tavapärane logi formaat näeb ette ajatempli ja sündmuse detailid.

Siin on näide ühest reast *syslog*'ist:

<pre>
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
</pre>

Võib näha, et 27. jaanuaril kell 07.41.32 käivitas CRON'i teenus töö cron.weekly.job. Kõikide sündmuste teateid, mida *syslog* kogub võib näha failis */var/log/syslog*.

## Harjutus

Vaadata faili */var/log/syslog*. Mis veel kasutaja arvutis toimub?

## Küsimus

Milline deemon haldab logisid uuematel Linuxi süsteemidel?

## Vastus

*rsyslogd*
