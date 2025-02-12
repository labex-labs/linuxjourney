# Alglaadimisprotsess: BIOS

## Tunni sisu

<b>BIOS</b>

Esimene samm Linuxi alglaadimisel on BIOS, mis teostab süsteemi terviklikkuse kontrolle. BIOS on püsivara, mis tuleb enamuse IBM PC, tänapäeval juhtivat tüüpi arvutitega kaasa. Kasutaja on kõige tõenäolisemalt kasutanud BIOS'i selleks, et muuta kõvaketaste algaadimise järjekorda, kontrollida süsteemi aega, arvuti MAC aadressi jne. BIOS'i peamine eesmärk on leida süsteemi alglaadur.

Kui BIOS on laadinud kõvaketta, otsib see alglaadimise blokki, et tuvastada kuidas laadida süsteemi. Sõltuvalt kettajagudest otsitakse kas alglaadimissektorit (MBR) või GPT'd. MBR asub kõvaketta esimeses sektoris, esimese 512 baidi peal. MBR sisaldab koodi veel ühe programmi laadimiseks kusagilt kettalt. See programm aga alles omakorda laeb tegelikult algaaduri.

Kui kettajaod on tekitatud GPT'ga, võib alglaaduri asukoht olla pisut teine.

<b>UEFI</b>

Peale BIOS'e on võimalik süsteemi alglaadida ka UEFI'ga (*Unified extensible firmware interface*). UEFI disainiti BIOS'i järglaseks ja enamus riistvara kasutab tänapäeval just seda. Machintoshi masinad on EFI alglaadimist kasutanud juba aastaid ja MS Windows on samuti suuremalt jaolt üle läinud UEFI peale. GPT formaat oli ette nähtud kasutamiseks koos EFI'ga. Sellegi poolest ei ole tingimata vaja EFI't kui alglaadida GPT ketas, sest GPT ketta esimene sektor on reserveeritud "kaitsvale MBR'ile", et võimaldada BIOS-põhise masina alglaadimist.

UEFI hoiab kogu käivitamisega seotud informatsiooni .efi failis, mida hoitakse spetsiaalsel kettajaol: EFI süsteemipartitsioonil riistvaras. Sellel kettajaol asub alglaadur. UEFI'l on palju parandusi ja edasiminekuid võrreldes BIOS'ega. Peatükid jätkuvad seda silmas pidades.

## Harjutus

Siseneda BIOS menüüsse ja uurida, kas UEFI alglaadimine on lubatud.

## Küsimus

Mille laeb BIOS?

## Vastus

Alglaaduri
