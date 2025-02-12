# Protsessori seire

## Tunni sisu

Kordame kasulikku käsku <b>uptime</b>:

<pre>
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
</pre>

Tööajast sai juba räägitud kursuse esimeses peatükis, kuid siis ei peatutud lähemalt keskmise koormuse väljal.  See on hea viis saada infot protsessori koormuse kohta. Kuvatav number esindab keskmist protsessori koormust 1, 5 ja 15 minutistes intervallides. Mida mõeldakse protsessi koormuse all? See on keskmine number protsesse, mis ootavad, et protsessor nad täidaks.

Ütleme, et kasutajal on ühetuumaline protsessor. Sellest tuumast võib mõelda kui ühest sõidureast liikluses. Tipptunnil on seal väga tihe sagimine ja liiklus on 100% juures, ehk siis koormus on 1. Kui aga liiklus läheb veel tihedamaks, täituvad ka sellele teele suubuvad teised teed ja autode hulk kahekordistub. Võib öelda, et liikluse koormus on 200% või siis 2. Kui aga liiklus natuke hajub ja autosid on ainult poole jagu, võib öelda, et raja koormus on 0,5. Kui ummikud on pea olematud ja inimesed saavad koju kiiremini, peaks koormus olema väga väike, nagu kell 2 öösel. Selles metafooris on autod protsessid ja protsessid ootavad, et saada sõiduteelt minema ja koju.

Kui kasutaja koormuse määr on 1 ei tähenda see kohe, et arvuti on lõpmata aeglane. Enamusel moodsatel masinatel on tänapäeval mitu tuuma. Neljatuumalisel masinal tähendaks keskmine koormus 1, et mõjutatud on ainult 25% protsessorist. Võib mõelda, et iga tuum on liikluses eraldi sõidurida. Protsessori tuumade arvu saab kuvada käsuga: <b>cat /proc/cpuinfo</b>.

Tundes huvi keskmise koormuse vastu, tuleb alati võtta arvesse ka tuumade arv. Kui seire tulemusel selgub, et arvutis on koormus pidevalt üle keskmise taseme, võib midagi olla korrast ära.

## Harjutus

Uurida süsteemi keskmist koormust ja selle käitumist.

## Küsimus

Millise käsuga saab kuvada keskmist koormust?

## Vastus

*uptime*
