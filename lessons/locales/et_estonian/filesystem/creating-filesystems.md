# Failisüsteemide loomine

## Tunni sisu

Nüüd kui kettajagude loomine on seljataga, asume failisüsteemi looma.

<pre>$ sudo mkfs -t ext4 /dev/sdb2</pre>
või ka
<pre>$ sudo mkfs.ext4 /dev/sdb2</pre>

Kui kirjutada *mkfs* ja vajutada kiirelt kaks korda TAB-klahvi siis näidatakse, millised valikud failisüsteemide osas antud süsteemis on.

Nii lihtne ongi! <b>mkfs</b> laseb kasutajal täpsustada soovitava failisüsteemi tüüpi ja asukohta. Failisüsteem luuakse äsja loodud või vana ümberjaotamise tulemusel loodud kettajaole. Kui luua failisüsteem juba olemasoleva peale on tulemuseks tõenäoliselt vigane failisüsteem.

## Harjutus

Teha USB pulgale ext4 failisüsteem.

## Küsimus

Millise käsuga luuakse failisüsteem?

## Vastus

*mkfs*
