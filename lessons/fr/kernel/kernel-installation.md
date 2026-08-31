---
lesson_id: "kernel-installation"
course_id: "kernel"
lang: "fr"
order_index: 4
title: "Installation du noyau"
description: "Découvrez comment installer, démarrer, vérifier et conserver un noyau de distribution avec une solution de repli testée."
meta_title: "Installation du noyau - Noyau"
meta_description: "Apprenez à installer et gérer les noyaux Linux, à vérifier leur version avec uname -r et à conserver une solution de repli."
meta_keywords: "noyau Linux, installer noyau, uname -r, gestion noyau, initramfs, chargeur démarrage, noyau de secours"
---

Les distributions empaquettent les noyaux avec leurs modules, l'intégration de l'initramfs, les mises à jour du chargeur d'amorçage, les signatures et les règles d'assistance. Employez ce processus géré, sauf si vous développez ou testez délibérément un noyau personnalisé et savez récupérer la machine.

## Noyaux actifs et installés

Affichez la version du noyau en cours d'exécution :

```bash
$ uname -r
6.8.0-00-generic
```

Cette commande ne répertorie pas tous les noyaux installés et ne change pas immédiatement lorsqu'un paquet plus récent est installé. Le système doit démarrer la nouvelle image avant que `uname -r` ne l'affiche. Interrogez les paquets installés et les entrées d'amorçage avec les outils propres à la distribution.

:::single-choice{#kernel-installation-uname-release}
Qu'affiche `uname -r` ?

::option[La chaîne de version du noyau actuellement en cours d'exécution.]{#kernel-installation-running-release .correct explanation="La commande indique l'état réel du noyau, pas simplement l'image la plus récente stockée sur le disque."}
::option[Tous les paquets de noyaux disponibles dans tous les dépôts.]{#kernel-installation-all-packages explanation="L'inventaire des dépôts relève du gestionnaire de paquets."}
::option[La version du micrologiciel de chaque périphérique connecté.]{#kernel-installation-device-firmware explanation="La version du noyau et l'inventaire des micrologiciels sont des données différentes."}
:::

## Préférer le paquet de suivi de la distribution

Installez ou conservez le paquet de suivi ou méta-paquet du noyau pris en charge par la distribution afin de continuer à recevoir les futures mises à jour de sécurité. Les noms dépendent de la version, de l'architecture, de la catégorie du matériel et de la variante du noyau. Ubuntu propose par exemple souvent `linux-generic`, mais les systèmes cloud, à faible latence, HWE, OEM, temps réel ou propres à une architecture utilisent d'autres paquets.

Ne transformez pas directement la chaîne de `uname -r` en opérande d'`apt install` en supposant qu'elle convient. Consultez la documentation actuelle de la distribution et examinez les candidats avec le gestionnaire de paquets avant l'installation.

:::single-choice{#kernel-installation-meta-package}
Pourquoi un méta-paquet de noyau pris en charge est-il utile ?

::option[Il garantit qu'aucun redémarrage ne sera jamais nécessaire.]{#kernel-installation-no-reboot explanation="Un noyau nouvellement installé ne devient actif qu'après un démarrage sur celui-ci, hormis la portée particulière des correctifs à chaud."}
::option[Il convertit tous les pilotes externes en code intégré au noyau.]{#kernel-installation-convert-drivers explanation="Les modules externes exigent toujours une construction compatible et une signature."}
::option[Il suit la suite de mises à jour du noyau prévue par la distribution.]{#kernel-installation-update-tracking .correct explanation="Ses dépendances font passer le système aux nouveaux paquets d'images et de modules pris en charge à mesure de leur publication."}
:::

## Préparer le changement

Avant une transaction concernant le noyau :

1. Confirmez les dépôts pris en charge, les signatures des paquets, le cycle de vie de la version et la variante de noyau prévue.
2. Assurez-vous que `/boot` ou la partition système EFI possède assez d'espace.
3. Conservez au moins un noyau installé et connu pour fonctionner, ainsi qu'une entrée d'amorçage sélectionnable.
4. Vérifiez les accès à la console, à la gestion distante, au support de secours, à la récupération du chiffrement et au retour arrière.
5. Contrôlez les modules externes, les pilotes de stockage et de réseau, la signature Secure Boot, l'hibernation et la compatibilité de la virtualisation.

La transaction des paquets doit générer un initramfs correspondant et mettre à jour les entrées d'amorçage par les hooks de la distribution. Lisez chaque erreur : l'état installé du paquet ne suffit pas si la génération de l'initramfs ou du chargeur a échoué.

:::single-choice{#kernel-installation-initramfs-error}
Pourquoi une erreur de génération de l'initramfs interdit-elle de conclure à la réussite ?

::option[La génération de l'initramfs change le mot de passe du shell de l'utilisateur.]{#kernel-installation-initramfs-password explanation="Le processus de l'archive de démarrage est sans rapport avec les secrets d'authentification des comptes."}
::option[Le nouveau noyau peut ne pas disposer des modules ou outils précoces nécessaires pour atteindre le stockage racine.]{#kernel-installation-missing-early-tools .correct explanation="Une image peut être installée alors que son artefact requis de l'espace utilisateur précoce est absent ou obsolète."}
::option[L'erreur prouve que le noyau actuellement actif s'est déjà arrêté.]{#kernel-installation-current-stopped explanation="Les hooks de paquets s'exécutent tandis que l'ancien noyau peut rester actif."}
:::

## Démarrer et valider

Planifiez un redémarrage contrôlé en tenant compte des parties prenantes et des charges actives. Assurez-vous que la console permet de sélectionner l'ancienne entrée si celle par défaut échoue. Après le démarrage :

```bash
$ uname -r
$ journalctl -k -b
$ systemctl --failed
```

Employez les outils équivalents sur les systèmes sans systemd. Validez le stockage, les systèmes de fichiers, le réseau, l'affichage, les périphériques d'entrée, les modules de sécurité, les modules externes, les conteneurs, les machines virtuelles et la santé applicative. Une invite de connexion seule ne constitue pas une validation complète.

:::single-choice{#kernel-installation-activation}
Quand un paquet ordinaire de noyau nouvellement installé devient-il le noyau en cours d'exécution ?

::option[Dès que `uname -r` est saisi.]{#kernel-installation-uname-activates explanation="Uname agit en lecture seule et ne peut pas changer de noyau."}
::option[Après que la machine a démarré cette image du noyau.]{#kernel-installation-after-boot .correct explanation="L'installation des fichiers ne remplace pas le noyau déjà exécuté en mémoire."}
::option[Lorsque l'archive du paquet est téléchargée, avant même son installation.]{#kernel-installation-download-activates explanation="Une archive téléchargée n'a aucun effet sur l'exécution active."}
:::

## Supprimer les anciens noyaux

N'employez le mécanisme de nettoyage pris en charge par le gestionnaire de paquets qu'après la validation du nouveau noyau. Ne supprimez jamais le noyau actuellement actif, la seule solution de repli connue pour fonctionner ou les paquets requis par le paquet de suivi actif. Examinez précisément la suppression proposée et les entrées d'amorçage qui en résulteront.

Une suppression manuelle dans `/boot` rend incohérents l'état des paquets et celui du chargeur. Si l'espace est déjà épuisé, préparez une récupération avant de modifier les fichiers au lieu de supprimer des images arbitraires.

:::single-choice{#kernel-installation-old-kernel-removal}
Quel noyau doit rester installé pendant la validation initiale d'un nouveau ?

::option[Uniquement le nouveau noyau non testé.]{#kernel-installation-only-new explanation="Supprimer toutes les solutions de repli avant le test transforme un problème de compatibilité en incident de récupération."}
::option[Aucun fichier de noyau sous le chemin de démarrage.]{#kernel-installation-no-kernels explanation="La machine a besoin d'un artefact de noyau chargeable pour démarrer Linux."}
::option[Une solution de repli connue pour fonctionner et sélectionnable dans le chargeur.]{#kernel-installation-known-good-fallback .correct explanation="Elle fournit une voie de récupération si le nouveau noyau échoue sur le matériel ou les charges."}
:::

Le laboratoire [Personnaliser le menu d'amorçage GRUB2](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) fournit un environnement sûr pour comprendre les entrées multiples.

## Résumé

Vous savez maintenant considérer une mise à jour du noyau comme un changement de la chaîne d'amorçage et de compatibilité.

1. Distinguer la version active des images installées.
2. Suivre les mises à jour prises en charge au moyen du bon paquet de la distribution.
3. Préparer le stockage, l'initramfs, les signatures, les modules et l'accès de récupération.
4. Démarrer puis valider le comportement du matériel et des applications.
5. Conserver une solution de repli connue jusqu'à ce que le nouveau noyau soit éprouvé.
