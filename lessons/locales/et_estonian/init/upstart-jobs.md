# Upstart'i tööd

## Tunni sisu

*Upstart* võib algatada palju sündmusi ja töid, paraku aga ei ole kerge tuvastada, kust midagi neist pärineb. Selleks tuleb natuke sobrada kataloogis */etc/init*. Suurema tõenäosusega pole kasutajal aga kunagi vaja *Upstart*'i sätete faile vaadata, kuid need võimaldavad soovi korral mingeid spetsiifilisi töid paremini kontrollida. *Upstart* süsteemis on võimalik kasutada hulgaliselt kasulikke käske.

<b>Tegumite kuvamine</b>

<pre>initctl list

shutdown stop/waiting
console stop/waiting
...
</pre>

Kuvatakse nimekiri *Upstart*'i töödest neile rakendatud erinevate olekutega. Igal real on töö nimi esimene väärtus, teine väli (enne /) on töö sihtkoht. Kolmas väärtus (/ järel) on hetke olek. Kasutaja võib näha, et süsteemi sulgemise töö tahab mingil hetkel lõpetada kuid on hetkel ootavas olekus. Töö olek ja sihtkoht muutuvad töid käivitades ja sulgedes.

<b>Kuva konkreetne tegum</b>

<pre>initctl status networking
networking start/running
</pre>

Siin kursusel ei minda *Upstart*'i tööde seadete kirjutamise oskuse osas detailidesse kuid juba on tutvustatud, et nende seadete kaudu töid alustatakse, peatatakse ja taaskäivitatakse. Töödest võivad käivituda ka teised tegumid. Olulisemad *Upstart*'i manuaalsed käsud käiakse siinkohal üle kuid kui huvi on suurem peaks uurima lähemalt  .conf faile.

<b>Käivita töö käsitsi</b>

<pre>$ sudo initctl start networking</pre>

<b>Peata töö käsitsi</b>

<pre>$ sudo initctl stop networking</pre>

<b>Taaskäivita töö käsitsi</b>

<pre>$ sudo initctl restart networking</pre>

<b>Võta kasutusele (emiteeri) töö käsitsi</b>

<pre>$ sudo initctl emit some_event</pre>

## Harjutus

Kuvada *Upstart* tööde nimekiri. Muuta mõne tegumi olekut äsja õpitud käskudega. Mida võib selle tagajärjel märgata?

## Küsimus

Kuidas käsitsi taaskäivitada töö nimega *moos*?

## Vastus

*sudo initctl restart moos*
