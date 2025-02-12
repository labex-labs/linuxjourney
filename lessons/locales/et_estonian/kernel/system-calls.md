# Süsteemsed kutsed

## Tunni sisu

On veel Britney meeles eelmisest peatükist? Ütleme, et me tahame temaga kohtuda ja mõned joogid teha, kuidas me saame õuest rahva hulgast tema kõige sisemisse seltskonda? Me kasutame süsteemseid kutseid. Need on nagu VIP pääsmed, mis loovad salajase kõrvalukse, mis viib otse Britney juurde.

Süsteemsed kutsed (*syscall*) annavad kasutaja protsessidele võimaluse paluda tuumal nende jaoks midagi teha. Tuum võimaldab teatud teenuseid läbi süsteemsete kutsete API. Need teenused võimaldavad kasutajal lugeda ja kirjutada faili, muuta mälu kasutust, seadistada võrku jne. Nende teenuste arv on kindlaks määratud, seega ei saa uisa-päisa süsteemseid kutsed lisada. Süsteemil on tabel olemasolevatest süsteemsetest kutsetest ja igal ühel neist on unikaalne ID.

Me ei lähe süsteemsete kutsetega väga süvitsi, kuna see eeldab kasutajalt natuke C programmeerimiskeele tundmist. Kuid põhiliselt kui kutsuta programm nagu *ls*, sisaldab selle kood süsteemse kutse mähist (mitte veel päris kutset ennast). Selle mähise sees kutsutakse esile süsteemne kutse, mis käivitab lõksu. See lõks püütakse süsteemsete kutsete töötleja poolt kinni ja talle otsitakse vaste süsteemsete kutsete tabelist. Ütleme, et proovitakse kutsuda välja süsteemset kutset stat(). Seda iseloomustab syscall ID ja ta eesmärk on pärida faili oleku kohta. Meenutame, et sisestasime *ls* programmi mittepriviligeeritud režiimis. Nüüd aga nähakse, et üritatakse teostada *syscall*, kasutaja lülitatakse seejärel ümber tuumarežiimi, seal toimuvad mitmed asjad, kuid peamine, et kontrollitakse syscall numbrit, see leitakse tabelist ja funktsioon, mida kasutaja soovis, viiakse täide. Kui kõik on valmis, pöördutakse tagasi kasutaja režiimi ja protsessid saavad oleku, kas kõik läks hästi või ilmnes vigu. *Syscall*'ide hingeelu on väga detailne, soovitame otsida informatsiooni Internetist lisaks.

Protsessi süsteemseid kutseid saab vaadata *strace* käsuga. See on hea käsk programmide töö silumiseks.

<pre>$ strace ls</pre>

## Harjutus

Harjutust pole.

## Küsimus

Mida kasutatakse kasutaja režiimilt tuuma režiimile lülitumiseks?

## Vastus

Süsteemset kutset
