---
lesson_id: "package-repositories"
course_id: "packages"
lang: "fr"
order_index: 2
title: "Dépôts de paquets"
description: "Découvrez comment les dépôts publient des index de paquets signés et comment APT trouve les sources configurées des distributions de la famille Debian."
meta_title: "Dépôts de paquets - Paquets"
meta_description: "Explorez les dépôts de paquets Linux, leur rôle dans la gestion des logiciels et les sources APT telles que /etc/apt/sources.list."
meta_keywords: "dépôts de paquets Linux, liste des sources APT, /etc/apt/sources.list, paquets Linux, Linux débutant, tutoriel Linux, gestion des paquets"
---

Un dépôt de paquets publie des paquets accompagnés d’index et de métadonnées de version. Le gestionnaire de paquets télécharge ces index, sélectionne les versions compatibles avec la distribution et l’architecture configurées, vérifie l’authentification du dépôt et récupère les fichiers de paquets nécessaires.

## Métadonnées du dépôt et catalogues locaux

Un dépôt est plus qu’un répertoire d’archives. Ses métadonnées décrivent les noms de paquets disponibles, leurs versions, leurs architectures, leurs sommes de contrôle, leurs dépendances et les sections du dépôt. Le client conserve un catalogue local afin de rechercher et de résoudre les paquets sans devoir télécharger d’abord chaque archive.

Sur un système de la famille Debian, actualisez les métadonnées configurées avec :

```bash
$ sudo apt update
```

Cette commande met à jour les index de paquets locaux ; elle n’installe pas à elle seule toutes les mises à niveau disponibles. Examinez les sources signalées et les erreurs d’authentification au lieu d’ignorer les entrées qui ont échoué.

:::single-choice{#package-repositories-apt-update}
Qu’est-ce que `apt update` actualise principalement ?

::option[Chaque binaire de paquet installé, sans confirmation.]{#package-repositories-all-binaries explanation="L’installation des mises à niveau est une opération distincte de l’actualisation des métadonnées."}
::option[Les mots de passe des utilisateurs autorisés à installer des paquets.]{#package-repositories-user-passwords explanation="L’actualisation des index de dépôts ne modifie pas les identifiants d’authentification locaux."}
::option[Les index locaux qui décrivent les paquets disponibles dans les sources configurées.]{#package-repositories-local-indexes .correct explanation="APT télécharge les métadonnées actuelles des dépôts afin que les recherches et la résolution des dépendances utilisent un catalogue à jour."}
:::

## Configuration des sources APT

APT lit les sources configurées dans :

- `/etc/apt/sources.list` ;
- les fichiers dont le nom se termine par `.list` ou `.sources` dans `/etc/apt/sources.list.d/`.

L’extension `.list` emploie le format traditionnel à une ligne. L’extension `.sources` emploie des strophes de style deb822, recommandées par la documentation actuelle d’APT pour les nouvelles configurations. Une distribution peut placer ses sources par défaut dans l’un ou l’autre emplacement ; `/etc/apt/sources.list` ne contient donc pas nécessairement la configuration complète ou principale.

Une source de style deb822 peut ressembler à ceci :

```text
Types: deb
URIs: https://deb.example.invalid/repository
Suites: stable
Components: main
Signed-By: /etc/apt/keyrings/example.gpg
```

Il s’agit uniquement d’un exemple de syntaxe ; le domaine réservé `.invalid` ne correspond pas à un dépôt utilisable.

:::single-choice{#package-repositories-apt-locations}
Où APT peut-il lire les définitions actives des dépôts ?

::option[Uniquement dans `/etc/apt/sources.list`.]{#package-repositories-only-main-list explanation="APT lit également les fichiers de sources pris en charge dans `/etc/apt/sources.list.d/`."}
::option[Uniquement dans des fichiers situés dans le répertoire personnel de chaque utilisateur.]{#package-repositories-only-home explanation="La configuration système des sources APT se trouve normalement sous `/etc/apt`."}
::option[Dans `/etc/apt/sources.list` et les fichiers pris en charge de `/etc/apt/sources.list.d/`.]{#package-repositories-both-locations .correct explanation="APT combine le fichier principal et les définitions `.list` et `.sources` du répertoire des listes de sources."}
:::

## Authentification du dépôt

APT vérifie les métadonnées de version signées du dépôt, puis compare les fichiers de paquets téléchargés aux sommes de contrôle authentifiées qu’elles contiennent. `Signed-By` peut limiter une source à un trousseau de clés précis au lieu d’accorder à chaque clé configurée globalement la confiance nécessaire pour ce dépôt.

Une signature valide établit que les métadonnées proviennent du détenteur d’une clé de signature acceptée et n’ont pas été modifiées sans détection. Elle ne prouve pas que le logiciel de l’éditeur est exempt de défauts, inoffensif ou adapté au système. Confirmez l’empreinte de la clé et les instructions relatives à la source par un canal de confiance indépendant.

:::single-choice{#package-repositories-signed-by}
Quel est l’objectif de sécurité de `Signed-By` dans une définition de source APT ?

::option[Chiffrer chaque paquet installé afin que root ne puisse pas le lire.]{#package-repositories-package-encryption explanation="La signature des dépôts assure des contrôles d’origine et d’intégrité, et non le secret face à l’administrateur local."}
::option[Limiter cette source à certaines clés de signature.]{#package-repositories-key-scope .correct explanation="Ce champ lie la vérification du dépôt à des trousseaux sélectionnés plutôt qu’à un ensemble global de clés sans restriction."}
::option[Garantir que le dépôt ne contient aucun logiciel vulnérable.]{#package-repositories-no-vulnerabilities explanation="L’authenticité cryptographique n’évalue ni la qualité du logiciel ni ses failles de sécurité."}
:::

## Ajouter délibérément des sources tierces

Un dépôt peut installer des paquets et des scripts de cycle de vie avec les privilèges du système ; son ajout étend donc la frontière de confiance logicielle du système. Avant de procéder :

1. Privilégiez le dépôt de la distribution s’il répond au besoin.
2. Confirmez l’éditeur, la version prise en charge, l’architecture et l’empreinte de la clé de signature.
3. Employez un fichier de source dédié et un trousseau de portée limitée.
4. Examinez les noms des paquets et les changements de dépendances avant l’installation.
5. Documentez la désactivation de la source et la migration ou la suppression de ses paquets.

Ne recopiez pas d’anciennes instructions qui désactivent le contrôle des signatures ou transmettent un script distant non audité à un shell privilégié.

:::single-choice{#package-repositories-third-party-risk}
Pourquoi l’ajout d’un dépôt tiers élargit-il la frontière de confiance du système ?

::option[Ses paquets et scripts authentifiés peuvent être installés avec les privilèges du système.]{#package-repositories-privileged-install .correct explanation="Faire confiance à la source de signature peut autoriser du code et des actions de cycle de vie qui affectent le système d’exploitation."}
::option[Il empêche le noyau Linux d’appliquer les permissions des fichiers.]{#package-repositories-disable-permissions explanation="La configuration d’un dépôt ne désactive pas les mécanismes normaux de contrôle d’accès du noyau."}
::option[Il convertit tous les paquets natifs en archives de code source.]{#package-repositories-convert-source explanation="L’ajout d’un dépôt modifie les sources de paquets disponibles, et non le format fondamental des paquets existants."}
:::

Entraînez-vous à une installation depuis un dépôt dans [Installation de logiciels sous Linux](https://labex.io/fr/labs/linux-software-installation-on-linux-18005), ou comparez une procédure de la famille Red Hat dans [Interroger et mettre à jour des paquets avec YUM](https://labex.io/fr/labs/rhel-query-and-update-packages-with-yum-in-linux-590869). Pour connaître la syntaxe exacte d’APT, consultez le manuel local `sources.list(5)`.

## Résumé

Vous savez maintenant expliquer comment un dépôt configuré devient une source authentifiée de métadonnées de paquets.

1. Distinguer les index de dépôts des archives de paquets.
2. Utiliser `apt update` pour actualiser le catalogue local.
3. Localiser les définitions de sources APT à une ligne et de style deb822.
4. Limiter la portée des clés de signature et évaluer délibérément la confiance accordée aux tiers.
