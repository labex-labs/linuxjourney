# lsusb, lspci, lsscsi

## Tunni sisu

Just nagu *ls* kuvab nimekirja failidest ja kataloogidest, on olemas sarnased tööriistad ka seadmete jaoks.

<b> USB seadmete kuvamine</b>

<pre>$ lsusb </pre>

<b>PCI seadmete kuvamine</b>

<pre>$ lspci </pre>

<b>SCSI seadmete kuvamine</b>

<pre>$ lsscsi </pre>

Vajadusel paigaldamiseks:
<pre>sudo apt update && sudo apt install lsscsi && sudo apt clean</pre>

<b>Plokkseadmete kuvamine</b>

<pre>$ lsblk</pre>

Plokkseadmete failisüsteeme näeb võtmega f:
<pre>$ lsblk -f</pre>

<b>Veel võimalusi</b>

Protsessoriarhitektuuri info:
<pre>$ lscpu</pre>

PCMCIA seadmete info:
<pre>$ lspcmcia</pre>

Riistvara info (soovitav käivitada superkasutajana):
<pre>$ sudo lshw</pre>

## Harjutus

Proovida kõiki õpitud käske ja tutvuda väljundiga.

## Küsimus

Millise käsuga saab kuvada usb seadmed?

## Vastus

*lsusb*
