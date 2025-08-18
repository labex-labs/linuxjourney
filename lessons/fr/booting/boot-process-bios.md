---
lang: "fr"
title: "Processus de démarrage : BIOS"
meta_title: "Processus de démarrage : BIOS - Démarrer le Système"
meta_description: "Découvrez le processus de démarrage Linux, le BIOS et le MBR. Comprenez comment votre système démarre avec ce guide convivial pour débutants. Explorez les concepts UEFI !"
meta_keywords: "processus de démarrage Linux, BIOS, MBR, UEFI, tutoriel Linux, chargeur de démarrage, Linux pour débutants, démarrage du système"
---

## Lesson Content

### BIOS

La première étape du processus de démarrage Linux est le BIOS, qui effectue des vérifications d'intégrité du système. Le BIOS est un firmware très courant dans les ordinateurs compatibles IBM PC, le type d'ordinateurs dominant aujourd'hui. Vous avez probablement utilisé le firmware BIOS pour modifier l'ordre de démarrage de vos disques durs, vérifier l'heure du système, l'adresse MAC de votre machine, etc. L'objectif principal du BIOS est de trouver le chargeur de démarrage du système.

Ainsi, une fois que le BIOS démarre le disque dur, il recherche le bloc de démarrage pour savoir comment démarrer le système. Selon la façon dont vous partitionnez votre disque, il se tournera vers le Master Boot Record (MBR) ou le GPT. Le MBR est situé dans le premier secteur du disque dur, les 512 premiers octets. Le MBR contient le code pour charger un autre programme quelque part sur le disque ; ce programme charge à son tour notre chargeur de démarrage.

Maintenant, si vous avez partitionné votre disque avec GPT, l'emplacement du chargeur de démarrage change un peu.

### UEFI

Il existe une autre façon de démarrer votre système au lieu d'utiliser le BIOS, et c'est avec l'UEFI (qui signifie "Unified Extensible Firmware Interface"). L'UEFI a été conçu pour succéder au BIOS ; la plupart des matériels actuels sont livrés avec le firmware UEFI intégré. Les machines Macintosh utilisent le démarrage EFI depuis des années maintenant, et Windows a majoritairement transféré tout son contenu vers le démarrage UEFI. Le format GPT était destiné à être utilisé avec l'EFI. Vous n'avez pas nécessairement besoin de l'EFI si vous démarrez un disque GPT. Le premier secteur d'un disque GPT est réservé à un "MBR protecteur" pour permettre le démarrage d'une machine basée sur le BIOS.

L'UEFI stocke toutes les informations de démarrage dans un fichier `.efi`. Ce fichier est stocké sur une partition spéciale appelée partition système EFI sur le matériel. À l'intérieur de cette partition, il contiendra le chargeur de démarrage. L'UEFI apporte de nombreuses améliorations par rapport au firmware BIOS traditionnel. Cependant, comme nous utilisons Linux, la majorité d'entre nous utilisent le BIOS. Toutes ces leçons suivront donc cette prémisse.

## Exercise

Allez dans votre menu BIOS et voyez si le démarrage UEFI est activé.

## Quiz Question

Que charge le BIOS ?

## Quiz Answer

bootloader
