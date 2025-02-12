# DNS protsess

## Tunni sisu

Vaatame näidet selle kohta, kuidas host leiab DNS'i abil domeeni (kiizudinternetis.com). Põhimõtteliselt kammitakse servereid kuni leitakse üks, mis otsitavat domeeni tunneb.

<b>Kohalik DNS server</b>

Esiteks küsib host "Kus asub kiizudinternetis.com?". Kohalik DNS server ei tea ja pöördub seega juurserverite poole. Tasub ära märkida, et neid päringuid kiizudinternetis.com kohta ei teosta otseselt host, enamus kasutajaid suhtleb Interneti teenusepakkuja rekursiivse DNS serveriga, mille ülesandeks saab otsitava lehekülje asukoha väljaselgitamine.

<b>Juurserverid</b>

Internetis on 13 juurserverit, need on dubleeritud ja jagatud üle maailma, et hallata Interneti DNS päringuid. Seega tegelikkuses töötab sadu serveid, mida kontrollivad erinevad organisatsioonid ja need sisaldavad informatsiooni tippdomeenide kohta. Tippdomeenid on näiteks  .org, .com ja .net aadressid. Seega juurserverid ei tea kus päritav aadress asub ja ta suunab meid edasi .com tippnimeserveri poole (annab selle serveri IP aadressi).

<b>Tippdomeenid TLD (*Top-Level Domain*)</b>

Järgnevalt saadetakse päring serverile, mis teab ".com" aadresse. Kas see server teab kus kiizudinternetis.com asub? Sellel serveril ei ole otsitavat aadressi tsoonifailis kuid on olemas aadressile vastav nimeserver. Kasutajale antakse selle nimeserveri IP aadress ja palutakse sealt edasi otsida.

<b>Autoriteetne DNS server</b>

Viimane päring tehakse serverile, milles asub otsitav kirje. Nimeserver tuvastab, et aadressi kiizudinternetis.com kohta on olemas tsoonifail ja hosti kohta on olemas ka "www" kirje. Kasutajale edastatakse seejärel IP aadress ja lõpuks ongi võimalik Internetis kiisusid vaadata.

## Harjutus

Harjutust pole.

## Küsimus

Milline lühend tähistab nimeservereid kus hoitakse .com, .net ja .org aadresse?

## Vastus

TLD
