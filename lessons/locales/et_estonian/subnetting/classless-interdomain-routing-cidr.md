# CIDR

## Tunni sisu

CIDR (*classless inter-domain routing*) ehk klassideta domeenidevaheline marsruutimine kasutab alamvõrgu maske kompaktselt. Alamvõrkude CIDR tähistust võib näha, kui näiteks alamvõrku 10.42.3.0 255.255.255.0 kujutatakse kujul 10.42.3.0/24, mis tegelikult tähendab samamoodi alamvõrgu eesliidet (*prefiks*) ja maski.

Meenutame veelkord, et IPv4 aadress koosneb 4 baidist, et 32 bittist. CIDR viitab bittidele, mida kasutatakse võrgu eesliitena. Seega 123.12.24.0/23 tähendab, et selleks on esimesed 23 bitti. Mida see siis tähendab? Mitu hosti see teeb?

Lihtne nipp on lahutada IP aadressi kõikidest bittidest (32) CIDR aadress (23), siis jääb meile 9 bitti. 2^9 =512, kuid lahutada tuleb veel 2 (võrgu aadress ja leviedastuse aadress). Seega kokku 510 lõppkasutajat.

## Harjutus

Harjutust pole.

## Küsimus

Küsimusi ka pole!

## Vastus
