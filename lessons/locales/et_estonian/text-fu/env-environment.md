# env (Environment)

## Tunni sisu

Käivitada käsk:

<pre>$ echo $HOME</pre>

Peaks nägema kodukataloogi otsiteekonda, näiteks /home/pete.

Aga see käsk?

<pre>$ echo $USER</pre> 

Peaks nägema enda kasutajanime!

Kust see informatsioon pärineb? See pärineb keskkonnamuutujatest. Neid saab näha, kui trükkida

<pre>$ env</pre> 

See väljund kuvab palju infot parasjagu seatud keskkonnamuutujate kohta. Nendes muutujates on palju kasulikku infot, mida kest ja teised protsessid saavad kasutada.

Siin on lühike näide:

<pre>
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
</pre>

Üks eriliselt oluline muutuja on PATH (otsiteekond). Muutujate väärtusi saab vaadata kui kirjutada $ sümbol muutujanime ette:

<pre>
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
</pre>

Kui käsk käivitada, tagastab see nimekirja koolonitega eraldatud otsiteekondadega. Näiteks kui laadida internetist käsitsi alla ja paigaldada tarkvarapakett, mis pannakse mittestandardsesse (otsiteekonnas mitteasuvasse) kataloogi ja tahta käivitada seda käsku. Kui kirjutada $ lahekäsk ja käsuviip ütleb, et käsku ei leitud kuigi on teada, et see on olemas. Mis toimub on see, et $PATH muutuja ei kontrolli seda kataloogi ega seal asuvat binaarfaili ning seetõttu annab veateate.

Ütleme, et arvutis on tonnides binaare, mida tahetakse käivitada väljaspool otsiteekonda asuvat kataloogi. Võib lihtsalt muuta PATH muutujat, et see sisaldaks vajalikku kataloogi sisseloginud kasutaja PATH keskkonnamuutujas.

## Harjutus

Mida teeb järgmine käsk? Miks?
<pre>$ echo $HOME</pre>

## Küsimus

Kuidas näha keskkonna muutujaid?

## Vastus

*env*
