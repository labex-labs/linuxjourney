---
lesson_id: "listing-devices"
course_id: "devices"
lang: "fr"
order_index: 6
title: "lsusb, lspci, lsscsi"
description: "Apprenez à inspecter la topologie USB, les fonctions PCI, les périphériques de la couche SCSI et leurs pilotes actifs."
meta_title: "lsusb, lspci, lsscsi - Périphériques"
meta_description: "Découvrez comment lister et inspecter le matériel USB, PCI et SCSI sur votre système Linux. Ce guide couvre les commandes lsusb, lspci et lsscsi, y compris des options comme lsusb -t pour afficher les arborescences des périphériques."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, lister périphériques usb, lister périphériques pci, lister périphériques scsi, matériel linux, information périphériques"
---

Linux propose des outils d'inventaire propres aux bus et sous-systèmes. Chacun fournit une vue différente : combinez identifiants, topologie, pilotes, chemins sysfs et journaux plutôt que d'attendre d'une seule commande une liste matérielle exhaustive.

## Inspecter les périphériques USB

`lsusb` liste les périphériques visibles par le sous-système USB :

```bash
$ lsusb
```

La sortie comprend normalement les numéros de bus et de périphérique, une paire d'identifiants fournisseur-produit et une description issue de la base USB locale. L'adresse numérique peut changer après une reconnexion ou un redémarrage et ne constitue pas une identité persistante.

Affichez les relations entre contrôleurs, concentrateurs, ports, interfaces, pilotes et vitesses avec :

```bash
$ lsusb -t
```

Une sortie détaillée des descripteurs existe, mais certains éléments exigent un accès en lecture privilégié. N'accordez pas de larges permissions USB uniquement pour faire taire une commande d'inspection.

:::single-choice{#listing-devices-usb-tree}
Quelle commande affiche les périphériques USB sous forme d'arborescence topologique ?

::option[`lspci -k`]{#listing-devices-lspci-tree explanation="Cette commande liste les fonctions PCI et leurs pilotes, pas la topologie USB."}
::option[`lsscsi -t`]{#listing-devices-lsscsi-tree explanation="Ce n'est pas la commande d'arborescence USB présentée."}
::option[`lsusb -t`]{#listing-devices-lsusb-tree .correct explanation="L'option d'arborescence montre les périphériques sous leurs contrôleurs et concentrateurs, avec les relations de ports et d'interfaces."}
:::

## Inspecter les fonctions PCI

`lspci` liste les fonctions découvertes sur les bus PCI et PCI Express :

```bash
$ lspci
```

Les périphériques PCIe internes ou externes peuvent inclure des contrôleurs graphiques, réseau, stockage, USB, audio ou des ponts. Affichez le pilote du noyau utilisé et les modules candidats avec :

```bash
$ lspci -k
```

La présence d'un contrôleur PCI dans la liste ne prouve pas que chaque périphérique sous-jacent est initialisé ou sain. Vérifiez l'association du pilote et les journaux du noyau lors d'un diagnostic.

:::single-choice{#listing-devices-pci-driver}
Quelle commande ajoute les informations sur le pilote du noyau à une liste PCI ?

::option[`lspci -k`]{#listing-devices-lspci-k .correct explanation="L'option `-k` affiche le pilote actif et les modules capables de gérer chaque périphérique PCI."}
::option[`lsusb -t`]{#listing-devices-usb-not-pci explanation="Cette commande décrit la hiérarchie USB et les pilotes d'interfaces."}
::option[`lsblk -f`]{#listing-devices-lsblk-filesystem explanation="Cette commande rapporte des champs de périphériques bloc et de systèmes de fichiers, pas les associations de pilotes PCI."}
:::

## Inspecter les périphériques de la couche SCSI

`lsscsi` liste les périphériques représentés par la couche intermédiaire SCSI de Linux :

```bash
$ lsscsi
```

Cela peut inclure des périphériques SCSI natifs et des disques SATA, USB ou virtuels présentés par des couches compatibles SCSI. Les espaces de noms NVMe appartiennent normalement à un autre sous-système et ne sont pas inventoriés de manière exhaustive par `lsscsi`.

Pour une hiérarchie orientée stockage qui inclut de nombreux types bloc, utilisez aussi :

```bash
$ lsblk -o NAME,TYPE,SIZE,MODEL,SERIAL,TRAN,FSTYPE,MOUNTPOINTS
```

:::single-choice{#listing-devices-lsscsi-scope}
Que liste principalement `lsscsi` ?

::option[Exclusivement tous les espaces de noms et contrôleurs NVMe.]{#listing-devices-only-nvme explanation="NVMe utilise son propre sous-système et ses outils, même si des vues bloc associées peuvent apparaître ailleurs."}
::option[Uniquement les fichiers dont le nom se termine par `.scsi`.]{#listing-devices-scsi-extension explanation="La commande interroge les interfaces de périphériques du noyau et non les extensions de noms."}
::option[Les périphériques représentés par la couche intermédiaire SCSI de Linux.]{#listing-devices-scsi-mid-layer .correct explanation="La commande rapporte les hôtes, cibles, unités logiques SCSI et les nœuds correspondants lorsqu'ils existent."}
:::

## Interpréter les résultats d'inventaire

Les descriptions proviennent souvent de bases locales d'identifiants et peuvent être génériques ou obsolètes. Un périphérique listé peut ne pas avoir de pilote fonctionnel ; un environnement virtualisé peut présenter du matériel émulé ou paravirtualisé. Selon les permissions et le problème, mettez les résultats en relation avec `udevadm info`, sysfs, `lsblk`, les outils réseau et `journalctl -k` ou `dmesg`.

Ces utilitaires peuvent être distribués dans des paquets séparés, souvent `usbutils`, `pciutils` et `lsscsi`. Si une commande manque, utilisez le gestionnaire de paquets de la distribution plutôt qu'un remplacement inconnu.

:::single-choice{#listing-devices-listed-not-working}
La présence d'un périphérique dans `lspci` prouve-t-elle que son pilote est actif et fonctionne correctement ?

::option[Non ; il faut aussi inspecter l'association du pilote et les messages du noyau.]{#listing-devices-needs-correlation .correct explanation="L'énumération prouve qu'une fonction PCI est visible, pas que son initialisation de haut niveau a réussi."}
::option[Oui ; l'énumération PCI réalise un test fonctionnel complet.]{#listing-devices-complete-test explanation="La liste n'exerce pas chaque fonction matérielle et ne valide pas le comportement des services."}
::option[Oui ; `lspci` installe automatiquement un pilote adapté.]{#listing-devices-installs-driver explanation="Cette commande est un outil d'inventaire et n'installe aucun paquet de pilotes."}
:::

Utilisez [Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861) pour comparer ces vues sur un hôte contrôlé.

## Résumé

Vous savez maintenant choisir une commande d'inventaire selon le sous-système concerné.

1. Utiliser `lsusb` et `lsusb -t` pour l'identité et la topologie USB.
2. Utiliser `lspci -k` pour les fonctions PCI et les pilotes.
3. Utiliser `lsscsi` pour la couche SCSI et `lsblk` pour la topologie bloc.
4. Relier l'énumération aux pilotes, à sysfs et aux messages du noyau.
