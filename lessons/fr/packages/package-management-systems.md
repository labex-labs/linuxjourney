---
lesson_id: "package-management-systems"
course_id: "packages"
lang: "fr"
order_index: 6
title: "yum et apt"
description: "Découvrez les procédures APT et DNF qui utilisent les dépôts pour examiner, installer, supprimer et mettre à niveau les paquets."
meta_title: "yum et apt - Paquets"
meta_description: "Explorez les différences entre yum et apt et apprenez à installer, supprimer et mettre à jour des paquets sur les systèmes Linux Debian et RPM."
meta_keywords: "yum ou apt, yum apt, gestion des paquets Linux, apt, yum, Debian, Red Hat, installer des paquets, mettre à jour des paquets, commandes Linux"
---

Les gestionnaires de paquets qui connaissent les dépôts récupèrent les métadonnées, résolvent les dépendances, vérifient le contenu authentifié et coordonnent les transactions. Les systèmes de la famille Debian emploient couramment APT. Les versions actuelles de Fedora et Red Hat Enterprise Linux utilisent DNF ; sur les versions actuelles de RHEL, la commande `yum` reste un alias de compatibilité de DNF, tandis que les systèmes plus anciens employaient l’implémentation YUM d’origine.

Suivez toujours la documentation de la distribution et de la version installées plutôt que de supposer qu’un même ensemble de commandes convient partout.

## Actualiser et examiner les métadonnées

APT sépare l’actualisation des métadonnées de la mise à niveau des paquets :

```bash
Debian family: $ sudo apt update
```

Recherchez et examinez les paquets avant de les installer :

```bash
Debian family: $ apt search package-name
Debian family: $ apt show package-name
RPM family:    $ dnf search package-name
RPM family:    $ dnf info package-name
```

La configuration des dépôts détermine ce que ces commandes peuvent découvrir. Lisez attentivement les noms des sources, les architectures, les versions et les erreurs de signature.

:::single-choice{#package-management-systems-apt-show}
Quelle commande affiche les détails APT de `package-name` ?

::option[`apt remove package-name`]{#package-management-systems-apt-remove-command explanation="La sous-commande `remove` propose de désinstaller le paquet."}
::option[`dnf search package-name`]{#package-management-systems-dnf-search-command explanation="Cette commande recherche dans les dépôts de la famille RPM et n’est pas la commande de détails d’APT."}
::option[`apt show package-name`]{#package-management-systems-apt-show-command .correct explanation="La sous-commande `show` présente les métadonnées du paquet binaire nommé."}
:::

## Installer des paquets

Installez un paquet par son nom dans le dépôt avec :

```bash
Debian family: $ sudo apt install package-name
RPM family:    $ sudo dnf install package-name
```

Le gestionnaire propose les dépendances ainsi que les conflits ou remplacements éventuels. Ne confirmez pas automatiquement avant d’avoir examiné l’origine, la version et l’architecture du paquet, le volume téléchargé, la variation de l’espace disque, les suppressions et les nouvelles dépendances installées.

:::single-choice{#package-management-systems-dnf-install}
Quelle commande actuelle installe `package-name` depuis les dépôts configurés de la famille RPM ?

::option[`rpm -qa package-name`]{#package-management-systems-rpm-query-command explanation="Il s’agit d’une requête sur la base des paquets RPM installés, et non d’une demande d’installation depuis un dépôt."}
::option[`dnf install package-name`]{#package-management-systems-dnf-install-command .correct explanation="DNF est le gestionnaire actuel qui connaît les dépôts sur Fedora et les versions récentes de RHEL."}
::option[`apt update package-name`]{#package-management-systems-apt-update-package explanation="APT update actualise les index et n’installe pas un paquet nommé de la famille RPM."}
:::

## Supprimer des paquets

Demandez une suppression avec :

```bash
Debian family: $ sudo apt remove package-name
RPM family:    $ sudo dnf remove package-name
```

La suppression peut affecter les paquets dépendants ou laisser des dépendances et une configuration désormais inutilisées. Examinez la transaction proposée, distinguez la suppression de la purge sur les systèmes de la famille Debian et préservez les données de l’application conformément à sa propre procédure de sauvegarde et de conservation. La suppression d’un paquet ne garantit pas celle des données créées par les utilisateurs.

:::single-choice{#package-management-systems-remove-review}
Pourquoi faut-il examiner une transaction de suppression avant de la confirmer ?

::option[La suppression reformate toujours le système de fichiers qui contient le paquet.]{#package-management-systems-removal-format explanation="Les gestionnaires suppriment des fichiers et un état gérés ; ils ne formatent normalement pas le système de fichiers."}
::option[Les gestionnaires de paquets ne peuvent pas afficher les changements proposés.]{#package-management-systems-no-proposal explanation="Les gestionnaires interactifs affichent normalement la transaction prévue précisément pour permettre son examen."}
::option[D’autres paquets peuvent dépendre du paquet sélectionné et être également affectés.]{#package-management-systems-dependent-removal .correct explanation="Les contraintes de dépendances peuvent étendre la demande au-delà du seul nom de paquet saisi."}
:::

## Appliquer les mises à jour

Sur un système APT, actualisez les métadonnées, puis examinez les mises à niveau comme deux étapes distinctes qui doivent réussir :

```bash
$ sudo apt update
$ apt list --upgradable
$ sudo apt upgrade
```

Sur un système DNF, examinez et appliquez les mises à jour disponibles selon la procédure documentée localement :

```bash
$ dnf check-update
$ sudo dnf upgrade
```

Une commande de mise à jour peut modifier les bibliothèques essentielles, les services, les noyaux et les dépendances. Employez les sauvegardes, la politique de maintenance, les notes de version et la planification des redémarrages adaptées au système. Vérifiez la sémantique de l’état de sortie : certaines opérations de contrôle, par exemple, emploient un état non nul pour signaler que des mises à jour sont disponibles plutôt qu’un échec d’exécution.

:::single-choice{#package-management-systems-apt-update-upgrade}
Quelle est la relation entre `apt update` et `apt upgrade` ?

::option[`update` supprime des paquets ; `upgrade` restaure leurs fichiers de configuration.]{#package-management-systems-apt-remove-restore explanation="Ces commandes n’entretiennent pas cette relation de suppression et de restauration."}
::option[`update` actualise les métadonnées ; `upgrade` applique un plan approuvé de mise à niveau des paquets.]{#package-management-systems-apt-two-steps .correct explanation="APT sépare l’actualisation du catalogue de l’installation de versions plus récentes des paquets."}
::option[Ce sont deux noms identiques pour une seule opération.]{#package-management-systems-apt-identical explanation="Elles réalisent des étapes distinctes qui doivent être vérifiées séparément."}
:::

## Choisir `dnf` ou `yum`

Employez `dnf` dans la documentation actuelle de Fedora et RHEL. Sur un système RHEL récent, la commande `yum` peut appeler le comportement de compatibilité de DNF, mais les scripts ne doivent pas déduire l’implémentation du seul nom de l’exécutable. Sur les anciens hôtes, vérifiez la version installée et la syntaxe prise en charge avant d’adapter les instructions.

:::single-choice{#package-management-systems-yum-current-rhel}
Que représente couramment `yum` sur un système RHEL actuel ?

::option[Une commande de compatibilité reposant sur DNF.]{#package-management-systems-yum-dnf-alias .correct explanation="Les versions récentes de RHEL emploient DNF tout en conservant le nom de commande yum pour la compatibilité."}
::option[L’outil Debian de bas niveau pour les archives `.deb`.]{#package-management-systems-yum-dpkg explanation="Les systèmes Debian emploient notamment APT et dpkg, et non YUM, pour la gestion native des paquets."}
::option[Un compresseur réservé aux métadonnées des dépôts.]{#package-management-systems-yum-compressor explanation="YUM et DNF sont des interfaces de gestion des paquets, et non des formats de compression autonomes."}
:::

Entraînez-vous à APT dans [Installer et supprimer des paquets](https://labex.io/fr/labs/linux-installing-and-removing-packages-385380) et aux concepts de la famille DNF/YUM dans [Interroger et mettre à jour des paquets avec YUM](https://labex.io/fr/labs/rhel-query-and-update-packages-with-yum-in-linux-590869).

## Résumé

Vous savez maintenant choisir et examiner les opérations courantes sur les paquets de dépôts.

1. Employer APT sur les systèmes de la famille Debian et DNF sur les systèmes actuels de la famille RPM.
2. Examiner les métadonnées et les changements de dépendances proposés avant l’installation.
3. Considérer la suppression comme une transaction qui tient compte des dépendances, et non comme la suppression d’un seul fichier.
4. Séparer l’actualisation des métadonnées de l’application des mises à niveau lorsque l’outil le fait.
5. Vérifier si `yum` désigne l’ancien YUM ou une commande de compatibilité de DNF.
