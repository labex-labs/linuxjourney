# Alglaadimisprotsess: Alglaadur

## Tunni sisu

Alglaaduri peamised kohustused on:

<ul>
<li>Operatsioonisüsteemi alglaadimine, kasutatakse ka mitte-Linux süsteemide korral</li>
<li>Valida kasutamiseks tuum</li>
<li>Täpsustada tuuma parameetrid</li>
</ul>

Kõige tavalisem Linuxi alglaadur on GRUB, kuid on veel palju teisi nagu LILO, efilinux, coreboot, SYSLINUX jt. Sellel kursusel aga piirdutakse GRUB'iga.

Alglaaduri ülesanne on laadida tuum, kuid kust seda leida? Selleks peab vaatama tuuma parameetreid. Parameetrid leiab GRUB'i menüüst, kui hoida all süsteemi käivitumisel *SHIFT* klahvi GRUB'i menüü avamiseks (kui arvutis on vaid Linux) ja soovitud menüükirje muutmiseks 'e' klahvi. Kui kasutaja ei ole ka GRUB'i, pole tarvis muretseda, aglaadimise parameetrid käikse selles peatükis üle:

<ul>
<li>initrd - Täpsustab algse RAM ketta asukoha (täpsemalt järgises peatükis)</li>
<li>BOOT_IMAGE  - tuuma kujutise faili asukoht</li>
<li>root -  Juurfailisüsteemi asukoht, tuum otsib sellest init'it. Seda esindab tihtipeale selle UUID või seadme nimi /dev/sda1.</li>
<li>ro - Standardne parameeter, mis haagib failisüsteemi külge vaid loetavana.</li>
<li>quiet - See lisatakse, et ei kuvataks teateid selle kohta, mis algaadimise ajal taustal toimub.</li>
<li>splash - Lubab kuvada käivitusekraani.</li>
</ul>
 
## Harjutus

Minna 'e' klahviga käivitusmenüü kirje muutmisesse ja tutvuda sealsete seadetega.

## Küsimus

Milline tuuma parameeter peidab alglaadimise teated?

## Vastus

quiet
