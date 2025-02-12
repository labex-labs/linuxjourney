# dd

## Tunni sisu

*dd* tööriist on väga kasulik andmete teisendamiseks ja kopeerimiseks. See loeb sisendi failist või andmevoost ja kirjutab selle samuti faili või andmevoogu.

Mõelda järgmise käsu peale:

<pre>$ dd if=/home/pete/backup.img of=/dev/sdb bs=1024 </pre>

Käsk kopeerib backup.img sisu seadmele /dev/sdb. Andmeid kopeeritakse 1024 baidiste blokkidena nii kaua kui pole enam midagi kopeerida.

<ul>
<li>if=fail - Sisendfail, standardsisendi asemel tuleb sisend lugeda failist</li>
<li>of=fail - Väljundfail, väljund kirjutatakse standardväljundi asemel faili</li>
<li>bs=bytes - Bloki suurus, määrab kui palju baite andmetest korraga loetakse ja kirjutatakse. Kasutada võib erinevaid suurusi märkides kilobaidi kohta k, megabaidi kohta m jne. 1024 baiti on 1k.</li>
<li>count=number - kopeeritavate blokkide arv.</li>
</ul>

Mõned *dd* käsud kasutavad loendurit (*count*). Kui on soov kopeerida 1 megabaidine fail siis ilmselt võiks ta ka peale kopeerimist olla kuvatud kui 1 megabait. Ütleme, et sisestatakse järgmine käsk:

<pre>$ dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2</pre>

backup.img fail on 10M, käsk ütleb aga, et kopeerida tuleb 1M kaks korda, mis tähendab, et kopeeritakse vaid 2M, mis tähendab, et kopeeritud andmed ei ole täielikud. Loendur *count* võib päris paljudes olukordades kasulikuks osutuda, kuid kui eesmärk on lihtsalt andmete kopeerimine võib *count*'i ja isegi *bs*'i vabalt vahele jätta. Kui eesmärk on tõsine andmete ülekandmise optimeerimine siis tasub alles hakata neid variante kaaluma.

*dd* on äärmisel võimas, sellega võib teha varukoopiaid ükskõik millest, sealhulgas terved kettad, kettakujutiste taastamine ja palju muud. Ettevaatus kulub ära, sest võimsa tööriista kasutamine võib kätte maksta, kui ei olda oma tegevustes päris kindel.

## Harjutus

Kasutada *dd* käsku, et teha oma kettast varukoopia, seada väljundiks .img fail.

## Küsimus

Millist võtit kasutab *dd* bloki suuruse jaoks?

## Vastus

bs
