# sysfs

## Tunni sisu

*Sysfs* loodi väga ammu selleks, et paremini hallata seadmeid, mille haldamisega */dev* kataloog hakkama ei saanud. *Sysfs* on virtuaalne failisüsteem, mis on tavaliselt ühendatud */sys* kataloogi. Selle kuvatav informatsioon on detailsem kui */dev* kataloogi oma. Mõlemad kataloogid tunduvad väga sarnased ja mõneti nad seda ka on kuid neil on ka olulisi erinevusi. Põhimõtteliselt on */dev* kataloog lihtne - see võimaldab teistel programmidel ise seadmetele ligi pääseda, samas kui */sys* failisüsteemi kasutatakse informatsiooni kuvamiseks ja seadmete haldamiseks.

*/sys* failisüsteem sisadab kogu informatsiooni süsteemi kõikide seadmete kohta, näiteks tootja ja mudel kuhu seade on ühendatud, seadme olek, seadme hierarhia ja muudki. Failid, mida seal kuvatakse ei ole seadmesõlmed, seega ei suhelda seadmetega */sys* kataloogist vaid pigem just hallatakse neid.

*/sys* kataloogi sisu näide:

<pre>
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
</pre>


## Harjutus

Vaadata */sys* kataloogi. Millised failid seal asuvad?

## Küsimus

Millises kataloogis on seadmete detailne informatsioon?

## Vastus

*/sys*
