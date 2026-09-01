---
lesson_id: "boot-process-bios"
course_id: "boot-system"
lang: "fr"
order_index: 2
title: "Processus de Démarrage : BIOS"
description: "Découvrez comment le BIOS historique et le micrologiciel UEFI moderne localisent et autorisent l'étape suivante du démarrage."
meta_title: "Processus de Démarrage : BIOS - Démarrer le Système"
meta_description: "Découvrez la première étape du démarrage Linux : le BIOS. Apprenez comment il trouve le chargeur de démarrage via MBR ou GPT, et comprenez le rôle de l'UEFI. Ce guide explique le démarrage du système et aborde comment accéder au BIOS pour la configuration."
meta_keywords: "processus démarrage Linux, BIOS, MBR, UEFI, bios sous linux, bios linux, comment accéder au bios, chargeur de démarrage, démarrage système"
---

Le micrologiciel s'exécute avant le noyau Linux. Sur le matériel de type PC, les deux principales interfaces sont le BIOS historique et l'UEFI. Leurs modèles de découverte du démarrage diffèrent ; l'affirmation « le BIOS lit le chargeur de démarrage » ne décrit donc qu'un parcours possible.

## Démarrage avec un BIOS historique

Après l'initialisation précoce de la plateforme et le choix du périphérique de démarrage, un BIOS historique lit généralement le premier secteur de 512 octets du disque choisi et transfère le contrôle à son code d'amorçage si le secteur possède la signature attendue.

Dans une disposition MBR, ce secteur contient une petite zone de code d'amorçage, quatre entrées de partition et une signature. Cette zone est trop petite pour un chargeur riche en fonctionnalités ; elle localise donc souvent une autre étape ailleurs sur le disque ou dans un système de fichiers.

Le démarrage BIOS depuis un disque GPT est possible, mais le MBR protecteur ne contient pas à lui seul les étapes ultérieures du chargeur. Sur GPT, GRUB utilise couramment une petite partition BIOS Boot pour son code principal intégré. La disposition exacte dépend du chargeur installé.

:::single-choice{#boot-bios-legacy-first-sector} Que charge généralement en premier un BIOS historique depuis le disque de démarrage choisi ?

::option[Le secteur d'amorçage initial contenant un petit code de démarrage.]{#boot-bios-boot-sector .correct explanation="Le parcours historique du micrologiciel transfère le contrôle au code situé dans le premier secteur du disque choisi."}
::option[L'intégralité du système de fichiers racine Linux dans la mémoire du micrologiciel.]{#boot-bios-entire-root explanation="Le secteur de première étape est minuscule ; un logiciel ultérieur localise le noyau et le stockage racine."}
::option[Toute la configuration des services utilisateur sous `/etc`.]{#boot-bios-etc-config explanation="Le micrologiciel n'analyse pas toute la configuration des services du système installé."}
:::

## Démarrage avec UEFI

Le micrologiciel UEFI peut comprendre un système de fichiers défini dans une partition système EFI, ou ESP, et charger des exécutables EFI. Les entrées de démarrage du micrologiciel, stockées dans des variables non volatiles, désignent normalement un disque, une partition et un chemin d'exécutable. Un chemin de repli standard peut servir aux supports amovibles ou aux scénarios de récupération.

L'ESP contient des applications de démarrage et leurs fichiers associés, pas « toutes les informations de démarrage ». Les images du noyau, les fichiers initramfs et la configuration du chargeur peuvent se trouver sur cette partition ou ailleurs selon la conception. GPT est conventionnel sur les systèmes UEFI, mais l'interface du micrologiciel et le schéma de table de partitions restent deux couches distinctes.

:::single-choice{#boot-bios-uefi-esp} Que charge généralement l'UEFI depuis une partition système EFI ?

::option[Un exécutable EFI choisi par une entrée de démarrage du micrologiciel.]{#boot-bios-efi-executable .correct explanation="La gestion du démarrage UEFI indique au micrologiciel un fichier exécutable situé sur une partition système prise en charge."}
::option[Un script shell POSIX provenant de n'importe quel répertoire personnel ext4.]{#boot-bios-shell-script explanation="Le micrologiciel charge des formats exécutables définis depuis des chemins de démarrage pris en charge ; il n'exécute pas un shell utilisateur ordinaire."}
::option[Une partition étendue MBR contenant les comptes utilisateur.]{#boot-bios-extended-users explanation="Les données de comptes ne participent pas à la découverte des exécutables UEFI."}
:::

## Secure Boot et chaîne de confiance

Lorsque Secure Boot est activé, l'UEFI vérifie les signatures de la chaîne de démarrage selon les clés et la politique enregistrées dans la plateforme. Une distribution Linux peut employer un shim signé, un chargeur, un noyau et une politique de modules du noyau pour prolonger cette chaîne.

Secure Boot ne chiffre pas le disque et ne prouve pas que tous les programmes de l'espace utilisateur sont sûrs. Il contribue à empêcher l'acceptation de code non autorisé avant le démarrage selon la politique de confiance configurée.

:::single-choice{#boot-bios-secure-boot-purpose} Que fait principalement respecter UEFI Secure Boot ?

::option[Le chiffrement automatique de tous les fichiers de tous les disques.]{#boot-bios-secure-encryption explanation="La confidentialité du disque nécessite un système de chiffrement distinct."}
::option[L'autorisation par signature des exécutables de la chaîne de démarrage.]{#boot-bios-secure-signatures .correct explanation="Le micrologiciel et les composants vérifiés ultérieurs acceptent le code selon les clés et la politique enregistrées."}
::option[L'absence garantie de vulnérabilités dans les logiciels signés.]{#boot-bios-secure-no-vulnerabilities explanation="Une signature valide prouve l'autorisation et l'intégrité, pas l'absence de défauts dans le code."}
:::

## Accéder à la configuration du micrologiciel

Les touches d'accès à la configuration dépendent du fabricant et du modèle. Il s'agit souvent de Suppr, Échap ou d'une touche de fonction pendant le démarrage initial. Consultez la documentation de l'appareil plutôt que de modifier des valeurs au hasard. Certains systèmes UEFI permettent aussi au système d'exploitation de demander un redémarrage dans la configuration du micrologiciel.

Notez les valeurs existantes et les clés de récupération avant de modifier Secure Boot, le mode du contrôleur de stockage, le TPM, la virtualisation ou l'ordre de démarrage. Un changement du micrologiciel peut rendre temporairement inaccessibles les volumes chiffrés ou le système installé.

:::single-choice{#boot-bios-setup-key} Pourquoi n'existe-t-il pas de touche universelle pour accéder à la configuration du micrologiciel ?

::option[Linux attribue une nouvelle touche aléatoire après chaque démarrage.]{#boot-bios-random-key explanation="Le système d'exploitation ne définit pas aléatoirement la touche de démarrage précoce du micrologiciel."}
::option[La touche et le moment de l'appui sont choisis par le fabricant du système.]{#boot-bios-vendor-key .correct explanation="Les interfaces de micrologiciel varient selon les modèles ; la documentation officielle de l'appareil est donc nécessaire."}
::option[La configuration n'est accessible qu'en supprimant le chargeur de démarrage.]{#boot-bios-delete-loader explanation="L'accès à la configuration du micrologiciel ne dépend pas de la destruction des fichiers de démarrage installés."}
:::

## Résumé

Vous savez maintenant distinguer les modèles de découverte du démarrage du BIOS historique et de l'UEFI.

1. Relier le BIOS historique au code du premier secteur et aux étapes ultérieures du chargeur.
2. Relier les entrées UEFI aux exécutables EFI d'une ESP.
3. Traiter GPT, l'interface du micrologiciel et la disposition du chargeur comme des choix distincts.
4. Ne modifier les réglages de confiance et de stockage du micrologiciel qu'avec une procédure de récupération.
