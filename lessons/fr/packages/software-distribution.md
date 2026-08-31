---
lesson_id: "software-distribution"
course_id: "packages"
lang: "fr"
order_index: 1
title: "Distribution des logiciels"
description: "Découvrez comment les projets en amont, les mainteneurs des distributions, les paquets et leurs formats forment une chaîne d’approvisionnement logicielle Linux."
meta_title: "Distribution des logiciels - Paquets"
meta_description: "Comprenez la distribution des logiciels Linux, les gestionnaires de paquets et les formats tels que .deb et .rpm."
meta_keywords: "distribution logicielle Linux, gestionnaire de paquets, .deb, .rpm, apprendre Linux, cours Linux gratuit, ressources Linux, ligne de commande Linux, installation de logiciels"
---

Les logiciels Linux sont couramment livrés sous forme de paquets gérés par des outils propres à chaque distribution. Un paquet rassemble des fichiers installables et des métadonnées afin que le système puisse suivre les versions, les dépendances, la propriété, les sommes de contrôle et les actions de cycle de vie.

## Contenu d’un paquet

Un paquet binaire peut contenir des exécutables, des bibliothèques, de la documentation, une configuration par défaut, des définitions de services et d’autres ressources. Il transporte également des métadonnées telles que :

- le nom et la version du paquet ;
- l’architecture cible et le contexte de la distribution ;
- les dépendances et les conflits déclarés ;
- les listes de fichiers et les informations d’intégrité ;
- les scripts ou déclencheurs facultatifs employés pendant les opérations du cycle de vie.

Tous les paquets ne sont pas des applications interactives. Un paquet peut fournir une bibliothèque, un composant du noyau, des données linguistiques, des polices, des symboles de débogage ou des métadonnées qui dépendent d’un ensemble d’autres paquets.

:::single-choice{#software-distribution-package-metadata}
Quelle information relève normalement des métadonnées d’un paquet plutôt que d’un exécutable applicatif ?

::option[Les instructions du processeur qui mettent en œuvre l’application.]{#software-distribution-executable-code explanation="Les instructions compilées appartiennent au contenu utile du paquet, et non aux métadonnées de dépendances."}
::option[Les relations de dépendances déclarées.]{#software-distribution-dependencies .correct explanation="Les paquets décrivent leurs exigences ou leurs conflits afin que les outils de gestion puissent raisonner sur l’installation."}
::option[Le document non enregistré de l’utilisateur actuellement ouvert en mémoire.]{#software-distribution-user-document explanation="Les données d’exécution de l’utilisateur ne font pas partie des métadonnées du paquet distribué."}
:::

## Rôles du projet en amont et de la distribution

Un projet en amont développe et publie le code source d’origine. Les mainteneurs d’une distribution Linux adaptent ensuite certaines versions à cette distribution. Leur travail peut comprendre l’examen des licences, l’application de correctifs d’intégration ou de sécurité, la définition des instructions de construction, la division du résultat en paquets, la déclaration des dépendances, l’exécution de tests et la maintenance des mises à jour.

L’infrastructure de construction de la distribution produit des paquets pour les versions et architectures prises en charge. Les outils du dépôt publient des métadonnées et des signatures que les clients peuvent vérifier. Les responsabilités exactes varient : certains projets en amont publient leurs propres paquets, tandis que les distributions peuvent les construire indépendamment à partir du code source.

:::single-choice{#software-distribution-maintainer-role}
Quelle tâche incombe couramment au mainteneur d’un paquet de distribution ?

::option[Adapter le code source en amont aux règles de construction et de dépendances de la distribution.]{#software-distribution-maintainer-integrates .correct explanation="Les mainteneurs adaptent les logiciels aux politiques, aux constructions, aux dépendances et aux environnements pris en charge par la distribution."}
::option[Choisir le mot de passe du compte local de chaque utilisateur.]{#software-distribution-maintainer-passwords explanation="Les données d’authentification locales sont sans rapport avec la maintenance des paquets."}
::option[Planifier l’exécution de chaque processus installé sur un processeur.]{#software-distribution-maintainer-scheduler explanation="Après l’installation, l’ordonnanceur du noyau en cours d’exécution gère l’utilisation du processeur."}
:::

## Formats courants de paquets natifs

Deux formats natifs largement utilisés sont :

- `.deb`, employé par Debian et les distributions qui en dérivent, notamment Ubuntu et Linux Mint ;
- `.rpm`, employé par Fedora, Red Hat Enterprise Linux et de nombreuses distributions apparentées.

Il existe d’autres formats natifs et multiplateformes. Une extension de fichier correspondante ne garantit pas à elle seule la compatibilité : l’architecture du paquet, la version de la distribution, les versions des bibliothèques, les politiques, les signatures et les dépendances comptent également.

:::single-choice{#software-distribution-debian-format}
Quel format de paquet natif Debian et Ubuntu utilisent-ils ?

::option[`.deb`]{#software-distribution-format-deb .correct explanation="Les outils de la famille Debian emploient le format d’archive `.deb`."}
::option[`.rpm`]{#software-distribution-format-rpm explanation="RPM est natif de Fedora, RHEL et des familles de distributions apparentées."}
::option[`.tar`]{#software-distribution-format-tar explanation="Une archive tar est un conteneur généraliste qui ne fournit pas à lui seul les métadonnées et la sémantique du cycle de vie d’un paquet Debian."}
:::

## Importance d’une distribution gérée

Un gestionnaire de paquets enregistre l’état installé et coordonne les changements entre les paquets. Une installation depuis les dépôts de confiance de la distribution fournit généralement une résolution cohérente des dépendances, la vérification des signatures, des mises à jour de sécurité et une suppression propre. Une copie manuelle de binaire ou une installation depuis les sources peut convenir, mais n’entre pas automatiquement dans ce cycle de vie géré.

La confiance dépend toujours de la configuration des dépôts et des clés de signature. Un paquet valide du point de vue cryptographique prouve son association avec une clé de confiance, mais pas qu’un logiciel tiers arbitraire est sûr ou adapté. Privilégiez si possible les dépôts de la distribution et évaluez toute source externe avant de lui accorder des privilèges d’installation.

:::single-choice{#software-distribution-package-manager-benefit}
Quel est l’un des avantages d’une installation depuis un dépôt de paquets de confiance ?

::option[Le gestionnaire peut suivre les versions et résoudre les dépendances déclarées.]{#software-distribution-managed-lifecycle .correct explanation="Les métadonnées du dépôt et les enregistrements de l’état installé permettent de coordonner l’installation, les mises à jour et la suppression."}
::option[Chaque programme installé devient insensible aux failles de sécurité.]{#software-distribution-no-vulnerabilities explanation="La gestion des paquets facilite les mises à jour, mais ne peut garantir l’absence de défauts."}
::option[Tous les paquets de toutes les distributions deviennent interchangeables.]{#software-distribution-universal-compatibility explanation="Les paquets natifs restent liés à des formats, versions, architectures et environnements de dépendances."}
:::

Utilisez l’atelier [Gérer des paquets avec RPM](https://labex.io/fr/labs/rhel-managing-packages-with-rpm-in-linux-590868) pour examiner les métadonnées et l’intégrité des paquets, ou [Construire un logiciel depuis le code source](https://labex.io/fr/labs/comptia-build-software-from-source-code-in-linux-590853) pour comparer une construction depuis les sources aux paquets gérés.

## Résumé

Vous savez maintenant identifier les principaux éléments de la distribution des logiciels Linux.

1. Distinguer le contenu utile d’un paquet de ses métadonnées.
2. Distinguer le développement en amont de l’intégration par la distribution.
3. Associer `.deb` et `.rpm` à leurs familles de distributions.
4. Évaluer la compatibilité et la confiance au-delà de l’extension du nom de fichier.
