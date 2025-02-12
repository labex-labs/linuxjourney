# Alglaadimisprotsessi ülevaade

## Tunni sisu

Nüüd kui on juba olemas üsna hea ülevaade olulisematest Linuxi komponentidest, on aeg kõik tükikesed kokku panna ja tutvustada süsteemi alglaadimist. Kui arvuti käivitada, teeb see igasuguseid asju. Näiteks ilmub logokuva, erinevad sõnumid vilksavad läbi ja lõpuks ilmub ette sisselogimise kuva. Tegelikult juhtub päris palju asju selle aja jooksul, mis mahub sisselülitusnupu vajutuse ja sisselogimise vahele ning see ongi käesoleva kursuse teema.

Linuxi alglaadimisprotsessi võib jagada neljaks lihtsaks etapiks:

<b>1. BIOS</b>

BIOS (*Basic Input/Output System*) tuvastab riistvara ja teeb POST (*Power-on self test*) testiga kindlaks, et riistvara on tööks valmis. BIOS'i peamine ülesanne on laadida alglaadur.

<b>2. Alglaadur</b>

Alglaaduri ülesanne on laadida mällu operatsioonisüsteemi tuum ning seejärel see ka koos hulga parameetritega käivitada. Üks tavalisemaid alglaadureid on GRUB (*GRand Unified Boot Loader*), mis on ka universaalne Linuxi standard.

<b>3. Tuum </b>

Kohe kui tuum on laetud tuvastab see seadmed ja mälu. Tuuma peamine ülesanne on laadida *init* protsess.

<b>4. Init</b>

Meenutame, et *init* on esimene protsess, mis käivitatakse. See omakorda käivitab ja peatab esmatähtsaid teenusprotsesse. Linuxis on *init*'il kolm peamist teostust. Neist läheme kergelt üle, sügavuti tuleb neist juttu teisel kursusel.

Ja selline ongi üks vägagi lihtne kirjeldus Linuxi alglaadimisprotsessist. Järgmistes peatükkides süveneme igasse etappi rohkem.

## Harjutus

Taaskäivitada arvuti ja proovida tuvastada kõiki äsja õpitud alglaadimise etappe.

## Küsimus

Milline on Linuxi alglaadimise viimane protsess?

## Vastus

*Init*
