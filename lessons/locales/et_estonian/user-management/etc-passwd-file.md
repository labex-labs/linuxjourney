# /etc/passwd

## Tunni sisu

Meenutame, et kasutajanimed ei ole tegelikult kasutajate tuvastamise aluseks. Süsteem kasutab selleks hoopis kasutajate ID'sid (UID - *User ID*). Selleks, et näha millised kasutajad milliste ID'dega seotud on, võib vaadata faili */etc/passwd*.

<pre>$ cat /etc/passwd</pre>

See fail sisaldab nimekirja kasutajatest ja igaühe kohta ka detailset informatsiooni. Kõige tõenäolisemalt näeb faili esimene rida välja nõnda:

<pre>root:x:0:0:root:/root:/bin/bash</pre>

Iga rida kuvab infot ühe kasutaja kohta ning juurkasutaja on tavaliselt kõige esimesel real. Paljud koolonitega eraldatud väljad annavad kasutajate kohta täiendavat infot, vaatame neid kõiki:

<ol>
<li>Kasutajanimi</li>
<li>Kasutaja salasõna - seda tegelikult selles failis ei hoita, tavaliselt on see hoopis failis <i>/etc/shadow</i>. Sellest failist räägitakse rohkem järgmises peatükis, praegu aga võiks meelde jätta vaid, et seal hoitakse kasutajate krüpteeritud salasõnu. Selles väljas võivad olla väga erinevad sümbolid. "x" tähendab, et salasõna hoitakse failis <i>/etc/shadow</i>, "*" tähendab, et kasutajal puudub sisse logimise õigus ja kui see väli on tühi, tähendab, et kasutajale pole salasõna seatud.</li>
<li>Kasutaja ID - nagu näha on juurkasutaja UID 0</li>
<li>Grupi ID</li>
<li><i>GECOS</i> väli - Tavapäraselt kasutatakse seda välja, et jätta kasutaja konto kohta kommentaar, näiteks kasutaja päris nimi või telefoni number, eraldajaks on koma.</li>
<li>Kasutaja kodukataloog</li>
<li>Kasutaja kestprogramm - väga paljudel kasutajatel on see vaikimisi *bash*</li>
</ol>

Tavaliselt oleks ootuspärane leida kasutajaseadete lehelt vaid inimkasutajad, siin aga on näha, et */etc/passwd* sisaldab ka teisi. Meenutame, et kasutajad eksisteerivad ainult selleks, et süsteemis erinevate õigustega protsesse käivitada. Mõnikord on eelistatud käivitada mingeid protsesse eelnevalt sätestatud õigustest. Näiteks, deemoni kasutajat kasutatakse deemoni protseside jaoks.

Märgiks ära, et */etc/passwd* faili saab ka käsitsi muuta, kui on vaja lisada kasutajaid või muuta olemasolevate informatsiooni. Selleks on tööriist nimega <b>vipw</b> kuid targem oleks siiski jätta sellised tegevused tööriistadele, millest räägitakse veidi hiljem. Need on näiteks *useradd* ja *userdel*. 

## Harjutus

Vaadata faili */etc/passwd* ning uurida milliseid õigusi erinevatel kasutajatel on.

## Küsimus

Kuidas on märgitud failis */etc/passwd*, kui kasutajal puudub sisselogimise õigus?

## Vastus

*
