# /etc/group

## Tunni sisu

Kasutajate haldamiseks kasutatakse veel ühte faili. */etc/group* võimaldab erinevate õigustega gruppe.

<pre>$ cat /etc/group

root:*:0:pete
</pre>

Sarnaselt */etc/shadow* failile, on */etc/group* väljad järgmised:

<ol>
<li>Grupi nimi</li>
<li>Grupi salasõna - tegelikult pole vajadust seada grupile salasõna, pigem on tavapärane tõstetud õiguste kasutamine, nagu näiteks <i>sudo</i> puhul. Vaikimis väärtus on "*".</li>
<li>Grupi ID (GID)</li>
<li>Nimekiri kasutajatest - kasutajate gruppi kuuluvust saab käsitsi määrata</li>
</ol> 

## Harjutus

Käivitada käsk <b>*groups*</b>. Mida kuvatakse?

## Küsimus

Mis on juurkasutaja GID?

## Vastus

0
