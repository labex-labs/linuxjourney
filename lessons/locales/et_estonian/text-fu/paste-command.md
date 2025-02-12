# paste

## Tunni sisu

Paste käsk on sarnane cat käsule. See ühendab read failis kokku.
Loome uue faili järgneva sisuga:

<pre>
näide2.txt
kiire
pruun
rebane
</pre>

Ühendame nüüd kõik need read:

<pre>$ paste -s näide2.txt</pre>

Vaikimisi on *paste*'i eraldaja tabulaator, seega nüüd on siis tulemuseks üks rida, kus sõnu eraldab tabulaator.

Muudame selle eraldaja (-d) millegi loetavama vastu:


<pre>$ paste -d ' ' -s näide2.txt</pre> 

Nüüd peaks kõik sõnad olema ühes reas tühikutega eraldatud.

## Harjutus

Proovida *paste* käsku mitme faili peal. Mis juhtub?

## Küsimus

Millist lippu kasutada, et saada kogu sisu ühele reale?

## Vastus

*-s*
