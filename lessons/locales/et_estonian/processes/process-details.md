# Protsessi detailid

## Tunni sisu

Enne kui süveneda protsesside praktilise rakendamise poolele, peaks mőistma, mis nad on ja kuidas nad töötavad. See osa vőib päris keeruliseks minna, kuna läheme päris asja tuumani. Kui pole soovi praegu asjasse süveneda, vőib selle peatüki juurde soovi korral ka hiljem tagasi pöörduda.

Nagu enne mainitud on protsess programm, mis süsteemis töötab, täpsemalt öeldes eraldab süsteem programmile töötamise jaoks mälu, protsessorit ja sisendit/väljundit. Protsess on töötava programmi üks esinemine. Proovida järgmist: Avada kolm terminali akent, kahes neist käiviata <b>cat</b> ilma lippudeta. Kolmandas aknas aga käivita <b>ps aux | grep cat</b>. On näha kaks *cat*i protsessi hoolimata sellest, et need mőlemad pöörduvad ühe programmi poole.

Protsesside eest vastutab tuum. Kui käivitada programm siis tuum laeb mälust programmi koodi, tuvastab ja määrab sellele vajalikud ressursid ning peab arvet kőikide protsesside üle, mis sellega seotud on:

<ul>
<li>Protsessi olek</li>
<li>Ressursid, mida protsess kasutab ja vastu vőtab</li>
<li>Protsessi omanik</li>
<li>Signaalide käsitlemine (sellest räägitakse hiljem lähemalt)</li>
<li>Ja pőhimőtteliselt kőik muu ka</li>
</ul>

Kőik protsessid tahavad maitsta magusat ressursside pirukat, tuuma ülesanne on hoolitseda selle eest, et iga protsess saab just nii palju kui vaja on. Kui protsess lőpeb, vabanevad ressursid mőne teise jaoks.     

## Harjutus

Selles peatükis harjutust ei ole.

## Küsimus

Mis haldab ja kontrollib protsesse?

## Vastus

tuum
