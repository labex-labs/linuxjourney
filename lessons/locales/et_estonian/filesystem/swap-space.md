# Saalimine

## Tunni sisu

Eelmises näites tutvustati kettajaotustabelit. Vaatame seda uuesti, aga nüüd täpsemalt seda rida:

<pre>
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
</pre>

Mis on see *swap* ehk saaleala? Saaleala kasutatakse virtuaalmälule süsteemis ruumi eraldamiseks. Kui mälumahtu hakkab väheks jääma, kasutab süsteem seda kettajagu, et saalida sinna tegevusetute protsesside mälu "tükid". Nõnda ei saa muutmälu otsa.

<b>Kettajao kasutamine saalimiseks</b>

Ütleme, et soovime seada */dev/sdb2* kettajao saalealaks.

<ol>
<li>Esiteks tuleb teha kindlaks, et kettajaol ei asu midagi</li>
<li>Tuvasta kasutuses olevad saalealad: <i>swapon -s</i></li>
<li>Tuvastamaks ka kasutuses mitteolevad saalealad - neil puudub lõpus haakepunkt <i>[SWAP]</i>: <i>lsblk -f | grep swap</i></li>
<li>Saaleala loomine: <i>sudo mkswap /dev/sdb2</i></li>
<li>Saaleala haakimine: <i>sudo swapon /dev/sdb2</i></li>
<li>Kui on soovitud, et saalealad püsiksid käivitamisel, on vaja lisada ka kirje <i>/etc/fstab</i> faili. Kasutada tuleb sw failisüsteemi tüüpi.</li>
<li>Saaleala lahtiühendamiseks: <i>sudo swapoff /dev/sdb2</i></li>
</ol>

<b>Saaleala haakimine alglaadimisel</b><br>
Teeme esmalt varukoopia */etc/fstab* failist juhuks kui midagi peaks valesti minema (hiljem saab sellest taastada):
<pre>
sudo cp /etc/fstab /etc/fstab-original
</pre>

Vaatame saaleala kettajao UUID ja suuname selle faili */etc/fstab*
<pre>
sudo blkid | grep swap | grep sdb2 >> /etc/fstab
</pre>

Seejärel kustutame üleliigse ja lisame vajaliku, et jääks lõpuks selline rida:
<pre>
UUID=xxxxxxxxxxx    none    swap    sw    0 0
</pre>
Jälgime, et UUID väärtus ei oleks jutumärkides ning muu ülearune info oleks kustutatud.

Juhul kui on vaja eelnevalt tehtud varukoopiast taastada:
<pre>
sudo cp /etc/fstab-original /etc/fstab
</pre>

Tavaliselt peaks määrama kaks korda nii palju ruumi saalealale kui on mälu, kuid tänapäeva süsteemid on juba piisavalt võimsad, et piisab ka sama suurest alast kui muutmälu (RAM) maht on. Näiteks 4 GB või suurema muutmälu korral võib rakendada valemit *saaleala = muutmälu maht*.

# Harjutus

Luua USB pulga vabale alale saaleala.

## Küsimus

Millise käsuga lubatakse (haagitakse) seadmel saaleala?

## Vastus

*swapon*
