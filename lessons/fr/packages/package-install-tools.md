---
lesson_id: "package-install-tools"
course_id: "packages"
lang: "fr"
order_index: 5
title: "rpm et dpkg"
description: "Découvrez comment `dpkg` et `rpm` examinent et modifient leurs bases de paquets natifs et leurs archives locales."
meta_title: "rpm et dpkg - Paquets"
meta_description: "Apprenez à installer, supprimer et répertorier des paquets avec rpm et dpkg, et comprenez la gestion directe des fichiers .deb et .rpm."
meta_keywords: "rpm, dpkg, gestion des paquets Linux, .deb, .rpm, tutoriel Linux, guide débutant, installer des paquets"
---

`dpkg` est l’outil de gestion de paquets de bas niveau des systèmes de la famille Debian, tandis que `rpm` joue un rôle semblable sur ceux de la famille RPM. Ils décompressent les archives natives, exécutent les actions du cycle de vie des paquets et mettent à jour les bases de paquets installés. Les outils qui connaissent les dépôts, tels qu’APT et DNF, reposent sur ces mécanismes de niveau inférieur.

## Examiner une archive avant l’installation

Une archive de paquet ne se réduit pas à un fichier exécutable. Elle peut contenir de nombreux fichiers utiles, des métadonnées, une gestion de la configuration et des scripts de cycle de vie privilégiés. Examinez son origine, sa signature ou son chemin de téléchargement authentifié, ses métadonnées et son contenu avant l’installation.

```bash
Debian: $ dpkg-deb --info ./some-package.deb
Debian: $ dpkg-deb --contents ./some-package.deb
RPM:    $ rpm -qip ./some-package.rpm
RPM:    $ rpm -qlp ./some-package.rpm
```

Dans les formes de requête RPM présentées, `p` signifie « interroger un fichier de paquet » plutôt que la base des paquets installés. La sortie aide à examiner un paquet, mais ne peut pas prouver que ses scripts ou ses programmes sont sûrs.

:::single-choice{#package-install-tools-native-format} Quel outil de bas niveau gère les paquets Debian `.deb` et leur base installée ?

::option[`rpm`]{#package-install-tools-rpm-debian explanation="RPM gère son propre format natif et sa base sur les systèmes de la famille RPM."}
::option[`tar`]{#package-install-tools-tar-debian explanation="Tar peut lire des archives, mais ne met pas en œuvre le cycle de vie des paquets Debian installés."}
::option[`dpkg`]{#package-install-tools-dpkg-debian .correct explanation="Les systèmes de la famille Debian emploient `dpkg` pour les opérations de bas niveau sur les archives `.deb` et la base des paquets."}
:::

## Installer une archive locale

L’installation directe de bas niveau emploie :

```bash
Debian: $ sudo dpkg -i ./some-package.deb
RPM:    $ sudo rpm -U ./some-package.rpm
```

`dpkg -i` peut décompresser et configurer l’archive demandée, mais ne récupère pas les dépendances manquantes dans les dépôts. De même, un appel direct de `rpm` n’offre pas la procédure habituelle du solveur de dépôts. Une commande de niveau supérieur est généralement préférable pour une archive locale, car elle peut résoudre les dépendances à partir des sources configurées :

```bash
Debian: $ sudo apt install ./some-package.deb
RPM:    $ sudo dnf install ./some-package.rpm
```

Examinez la transaction avant de la confirmer. Dans APT, le préfixe `./` distingue le chemin d’une archive Debian locale du nom d’un paquet de dépôt.

:::single-choice{#package-install-tools-local-dependencies} Quelle commande présentée peut installer un fichier `.deb` local tout en résolvant les dépendances disponibles dans les dépôts ?

::option[`dpkg -l ./some-package.deb`]{#package-install-tools-dpkg-list-file explanation="`dpkg -l` répertorie les sélections de paquets installés et ne constitue pas une procédure d’installation locale avec résolution des dépendances."}
::option[`rpm -qa ./some-package.deb`]{#package-install-tools-rpm-query-deb explanation="La syntaxe d’interrogation de RPM n’installe pas une archive Debian."}
::option[`apt install ./some-package.deb`]{#package-install-tools-apt-local .correct explanation="APT reconnaît le chemin local explicite et peut employer les dépôts configurés pour satisfaire les dépendances déclarées."}
:::

## Supprimer un paquet installé

La suppression vise le nom d’un paquet installé, et non celui de l’archive utilisée auparavant :

```bash
Debian: $ sudo dpkg --remove package-name
RPM:    $ sudo rpm --erase package-name
```

Sous Debian, `--remove` conserve normalement les fichiers de configuration classés comme conffiles ; `--purge` demande également leur suppression, sous réserve des scripts du paquet et des données non gérées. Aucune des deux commandes ne garantit la suppression des données créées par les utilisateurs. Les commandes de niveau supérieur `apt remove` ou `dnf remove` sont généralement préférables, car elles peuvent évaluer les paquets liés et présenter une transaction complète.

:::single-choice{#package-install-tools-remove-operand} Quel opérande `dpkg --remove` attend-il pour un paquet installé ?

::option[L’URL de l’index du dépôt.]{#package-install-tools-remove-url explanation="L’emplacement du dépôt n’est pas l’identité du paquet transmise à la suppression de bas niveau."}
::option[Le nom du paquet installé.]{#package-install-tools-remove-name .correct explanation="La suppression vise l’enregistrement du paquet, par exemple `example`, et non l’ancien chemin de son fichier `.deb`."}
::option[Le PID d’un processus démarré par le paquet.]{#package-install-tools-remove-pid explanation="Les identifiants de processus sont sans rapport avec la clé de la base des paquets installés."}
:::

## Interroger l’état installé

Répertoriez les paquets installés ou connus avec :

```bash
Debian: $ dpkg-query -l
RPM:    $ rpm -qa
```

Pour un examen ciblé, préférez un nom de paquet précis et un format exploitable par une machine lorsque la fiabilité d’un script est importante. Les bases de paquets décrivent l’état géré ; les administrateurs locaux ou les applications peuvent encore modifier les fichiers ensuite. Employez donc les fonctions de vérification lorsque vous devez comparer les fichiers installés aux métadonnées enregistrées.

:::single-choice{#package-install-tools-rpm-list-installed} Quelle commande interroge tous les paquets enregistrés comme installés dans la base RPM ?

::option[`rpm -qa`]{#package-install-tools-rpm-query-all .correct explanation="`-q` sélectionne le mode d’interrogation et `-a` l’étend à tous les enregistrements de paquets installés."}
::option[`rpm -e`]{#package-install-tools-rpm-erase explanation="`-e` demande la suppression d’un paquet plutôt qu’une liste en lecture seule."}
::option[`dpkg-deb --contents`]{#package-install-tools-deb-contents explanation="Cette commande examine le contenu d’une archive Debian, et non la base des paquets RPM installés."}
:::

Utilisez [Gérer des paquets avec RPM](https://labex.io/fr/labs/rhel-managing-packages-with-rpm-in-linux-590868) pour vous exercer aux requêtes sur les archives et aux contrôles d’intégrité dans un système isolé.

## Résumé

Vous savez maintenant distinguer les opérations de bas niveau sur les paquets des transactions de dépôts.

1. Examiner les métadonnées et le contenu d’une archive locale avant l’installation.
2. Employer `dpkg` pour les fichiers `.deb` et `rpm` pour les fichiers `.rpm`.
3. Préférer APT ou DNF lorsque les dépendances doivent être résolues.
4. Supprimer par le nom du paquet installé et vérifier séparément l’état géré.
