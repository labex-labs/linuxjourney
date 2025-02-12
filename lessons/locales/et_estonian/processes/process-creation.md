# Protsesside loomine

## Tunni sisu

See ja eelmine peatükk on puhtalt informatiivsed, et tutvustada natuke protsesside hingeelu. Siia võib igal ajal tagasi pöörduda kui ollakse veidi rohkem protsesside kallal töötanud.

Protsessi loomisel põhimõtteliselt kloonitakse juba olemasolevat protsessi kasutades midagi, mida nimetatakse *haru* (ingl.k *fork*) süsteemseks kutseks (süsteemsetest kutsetest räägitakse alles väga kauges tulevikus). *Haru* kutse loob olemasolevale protsessile identse tütarprotsessi, mis võtab endale uue protsessi ID (PID) ja esialgsest protsessist saab vanemprotsess, mis saab endale vanemprotsessi ID ehk <b>PPID</b> (*Parent Process ID*). Hiljem võib aga tütarprotsess jätkata sama programmi kasutamist, mida kasutas tema vanem või kasutada *execve* süsteemset kutset, et käivitada uus programm. See kutse hävitab senise tuuma poolt selle protsessi jaoks loodud mälu haldamise ning seab üles uued just selle programmi jaoks.

Seda võib tegevuses näha:

<pre>$ ps l</pre>

Valik l (nagu *long format* ehk *pikk formaat*) võimaldab jooksvaid protsesse vaadelda isegi veel detailsemalt. Näha on tulp nimega <b>PPID</b>, see ongi vanemprotsessi ID. Kui nüüd vaadata oma terminali siis on näha protsess, mis on jooksev kestprogramm, näiteks *bash*. Meenutame, et kui sisestada *ps l* käsk, käivitati see protsessist, mis käivitas *bash*i. Paneme tähele, et *bash*i kesta <b>PID</b> on selle *ps l* käsu <b>PPID</b>.

Seega kui igal protsessil peab olema vanem ja kõik protsessid on üksteise harud, peab ju kusagil olema kõikide protsesside ema, eks? Nii ongi. Kui süsteem algkäivitub, loob tuum protsessi nimega <b>init</b>, mille PID on 1. Seda protsessi saab peatada vaid siis kui süsteem välja lülitada. *Init* töötab juurkasutaja õigustes ja käitab mitmeid teisi protsesse, mis võimaldavad süsteemil töötada. *Init* tuleb lähema vaatluse alla süsteemi algkäivitamise kursusel, praegu võiks meelde jätta, et tegu on kõikide teiste protsesside loojaga.

## Harjutus

Vaadelda töötavaid protsesse - millistel protsessidel on vanemad?

## Küsimus

Milline süsteemi kutse loob uue protsessi?

## Vastus

*haru*
