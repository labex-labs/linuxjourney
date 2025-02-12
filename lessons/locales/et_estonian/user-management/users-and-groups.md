# Kasutajad ja grupid

## Tunni sisu

Traditsiooniliselt on igas operatsioonisüsteemis kasutajad ja grupid. Need eksisteerivad selleks, et tagada ligipääsu ja õigusi. Iga protsess käivitub selle omaniku õigustes, olgu see siis Mari või Mart. Failide ligipääs ja omanik sõltub samuti ligipääsuõigustest. Me ju ei taha, et Mari näeks Mardi dokumente ja vastupidi.

Igal kasutajal on isiklik kodukataloog kus hoitakse kasutajaga seotud faile. See asub tavaliselt */home/kasutajanimi*, kuid võib distributsiooniti erineda.

Süsteem kasutab kasutajate haldamiseks kasutaja ID'sid (UID), kasutajanimed on sõbralikum viis kasutaja tuvastamiseks kuid süsteem kasutab selleks just UID'sid. Sellele lisaks on süsteemis õiguste haldamiseks grupid, mis kujutavad endast lihtsalt mingit komplekti kasutajaid, kellel kõigil on samad grupi õigused. Neid eristatakse süsteemis grupi ID (GID) järgi.

Linuxis võivad olla ka kasutajad, kes ei olegi tavapärased süsteemi kasutavad inimesed. Leidub selliseid kasutajaid, kes on tegelikult süsteemi deemonid, mis pidevalt käivitavad protsesse ja hoiavad süsteemi töökorras. Üks olulisimaid selliseid kasutajaid on *root* ehk siis *superkasutaja* (ka *juurkasutaja*). Juurkasutaja on süsteemis kõige mõjuvõimsam: ta saab ligi kõikidele failidele ja käivitada või peatada ükskõik millist protsessi. Sellel põhjusel on ka ohtlik pidevalt juurkasutajana tegutseda: näiteks võib kogemata kustutada mõne kriitilise süsteemi faili. Õnneks aga kui kasutajal on ligipääs juurkasutajale ja tal selle õigusi peaks vaja minema, võib ta *sudo* käsuga sisestada käske hoopis juurkasutaja õigustega. Sudo käsku (*superuser do*) kasutataksegi just selleks, et käsk käivituks juurkasutaja õigustega. Sellest, kuidas kasutaja saab omandada juurkasutaja õigused räägitakse süvitsi veidi hiljem.

Proovi vaadata kaitsud faili, näiteks */etc/shadow*:

<pre>$ cat /etc/shadow</pre>

Pane tähele, et antakse veateade ligipääsu keelamise kohta. Nii saab vaadata õigusi:

<pre>$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
</pre>

Õigustest ei ole küll veel lähemalt räägitud kuid eelnevast on näha, et faili omanik on juur (ehk *root*) ja faili sisu lugemiseks on vaja juurkasutaja ligipääsuõigusi või kuulumist *shadow* gruppi. Nüüd aga prooviks sama käsku *sudo*ga:

<pre>$ sudo cat /etc/shadow</pre>

Nüüd on faili sisu nähtav!

## Harjutus

Selles peatükkis harjutust ei ole.

## Küsimus

Kuidas saab sisestada käsku juurkasutaja õigustega?

## Vastus

sudo
