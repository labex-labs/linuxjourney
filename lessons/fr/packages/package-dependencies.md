---
lesson_id: "package-dependencies"
course_id: "packages"
lang: "fr"
order_index: 4
title: "Dépendances des paquets"
description: "Découvrez comment les métadonnées des paquets expriment les fonctionnalités requises, les versions, les conflits et les relations entre bibliothèques partagées."
meta_title: "Dépendances des paquets - Paquets"
meta_description: "Découvrez les dépendances des paquets Linux, les bibliothèques partagées et la manière dont la gestion des paquets prévient les installations incohérentes."
meta_keywords: "dépendances des paquets Linux, bibliothèques partagées, paquets Linux, gestion des paquets, installation de logiciels Linux, tutoriel Linux, Linux débutant"
---

Une dépendance de paquet indique qu’un paquet a besoin d’un autre paquet, d’une fonctionnalité ou d’une version compatible pour être installé ou fonctionner. Les gestionnaires de paquets qui connaissent les dépôts emploient ces métadonnées pour calculer un ensemble cohérent de changements au lieu de traiter chaque archive isolément.

## Relations de dépendances

Les métadonnées d’un paquet peuvent exprimer plus qu’un simple nom obligatoire. Selon le format de la distribution, les relations peuvent comprendre :

- les dépendances obligatoires ;
- des contraintes de version minimale, maximale ou exacte ;
- des solutions de remplacement, où l’un des fournisseurs possibles satisfait l’exigence ;
- des recommandations ou des suggestions dont la sémantique est moins contraignante ;
- des conflits, des ruptures ou des remplacements ;
- des fonctionnalités virtuelles fournies par plusieurs paquets.

Ces règles permettent au solveur de choisir un ensemble de versions compatible avec les dépôts configurés, l’architecture et l’état installé. Une solution peut nécessiter des mises à niveau, des suppressions ou un choix entre plusieurs fournisseurs ; examinez donc la transaction proposée avant de l’approuver.

:::single-choice{#package-dependencies-solver-role}
Que cherche à produire un solveur de dépendances qui connaît les dépôts ?

::option[Un ensemble cohérent de versions de paquets et de changements nécessaires.]{#package-dependencies-consistent-set .correct explanation="Le solveur évalue les relations déclarées entre les paquets installés et disponibles."}
::option[Un nouveau compte utilisateur pour chaque application installée.]{#package-dependencies-user-account explanation="La création d’un compte peut être une action du cycle de vie d’un paquet, mais ce n’est pas le but de la résolution des dépendances."}
::option[Une copie compressée de chaque fichier du dépôt.]{#package-dependencies-compressed-repository explanation="Le solveur sélectionne des métadonnées et des paquets ; il n’archive pas tout le dépôt."}
:::

## Bibliothèques partagées comme dépendances

Une bibliothèque partagée contient du code compilé que plusieurs programmes peuvent charger à l’exécution. Le partage réduit la duplication des implémentations et permet aux distributions de mettre à jour une bibliothèque commune indépendamment, mais les programmes dépendent d’une interface binaire applicative, ou ABI, compatible.

Sur les systèmes Linux reposant sur ELF, un exécutable peut enregistrer le nom d’une bibliothèque nécessaire, par exemple un SONAME. L’éditeur de liens dynamique trouve une bibliothèque installée correspondante au démarrage du programme. Les métadonnées du paquet représentent généralement cette exigence comme une dépendance envers le paquet ou la fonctionnalité qui fournit la bibliothèque compatible.

:::single-choice{#package-dependencies-shared-library}
Qu’est-ce qu’une bibliothèque partagée ?

::option[Du code compilé que plusieurs programmes peuvent charger et utiliser.]{#package-dependencies-library-code .correct explanation="Une bibliothèque partagée fournit des interfaces binaires réutilisables au lieu d’intégrer une implémentation distincte dans chaque programme."}
::option[Une liste de dépôts partagée entre des distributions sans rapport.]{#package-dependencies-shared-repository explanation="La configuration des dépôts et le code exécutable d’une bibliothèque sont des notions différentes."}
::option[Un fichier texte contenant l’historique du shell de chaque utilisateur.]{#package-dependencies-shared-history explanation="L’historique du shell est une donnée utilisateur et non une dépendance de bibliothèque d’un programme."}
:::

## Compatibilité des versions et de l’ABI

La présence d’un fichier dont le nom ressemble à celui de la bibliothèque ne suffit pas. L’ABI requise, l’architecture, les symboles et parfois la version minimale doivent correspondre. Le remplacement manuel d’une bibliothèque de la distribution peut briser tous les programmes qui en dépendent, même si son nom paraît correct.

Les mainteneurs de paquets encodent les relations entre bibliothèques et coordonnent les transitions lorsqu’une ABI change. Laissez le gestionnaire de paquets contrôler les bibliothèques natives ; employez des mécanismes pris en charge d’installation parallèle, de conteneur, d’environnement ou de construction pour les logiciels qui exigent une version incompatible.

:::single-choice{#package-dependencies-filename-insufficient}
Pourquoi un programme peut-il encore échouer lorsqu’un fichier de bibliothèque portant un nom semblable existe ?

::option[Linux n’autorise qu’un seul exécutable à employer chaque bibliothèque.]{#package-dependencies-one-consumer explanation="L’un des objectifs fondamentaux des bibliothèques partagées est leur utilisation par plusieurs processus et programmes."}
::option[Les dépendances des paquets ne s’appliquent qu’avant le premier démarrage du système.]{#package-dependencies-boot-only explanation="Les dépendances restent pertinentes pendant l’installation, les mises à niveau et l’exécution."}
::option[L’ABI ou l’architecture de la bibliothèque peut ne pas répondre aux exigences du programme.]{#package-dependencies-abi-mismatch .correct explanation="L’édition de liens à l’exécution dépend d’interfaces binaires et d’une architecture machine compatibles, et non seulement du nom du fichier."}
:::

## États de dépendances cassés

Un problème de dépendances peut provenir d’un mélange de dépôts, d’opérations interrompues, d’archives installées manuellement, de versions retenues, de fichiers supprimés ou de logiciels tiers incompatibles. N’y répondez pas en supprimant les fichiers de la base des paquets ou en forçant aveuglément une installation.

Commencez par lire les diagnostics du gestionnaire de paquets, n’actualisez que les métadonnées des dépôts de confiance, examinez les versions retenues ou épinglées et vérifiez la réparation proposée. Un installateur de bas niveau peut décompresser une archive sans récupérer toutes ses dépendances ; un outil de dépôt de niveau supérieur est généralement plus sûr pour une installation ordinaire, car il résout toute la transaction.

:::single-choice{#package-dependencies-low-level-limit}
Quelle est une limite courante de l’installation d’un paquet local avec un outil d’archives de bas niveau ?

::option[Il peut ne pas récupérer ni résoudre toutes les dépendances manquantes dans les dépôts.]{#package-dependencies-no-repository-resolution .correct explanation="Les outils de bas niveau gèrent les archives et les bases de paquets, mais peuvent laisser la récupération des dépendances à un gestionnaire de niveau supérieur."}
::option[Il recompile toujours le noyau Linux depuis les sources.]{#package-dependencies-recompile-kernel explanation="L’installation d’une archive de paquet n’entraîne pas nécessairement la reconstruction du noyau."}
::option[Il empêche le paquet de contenir des bibliothèques partagées.]{#package-dependencies-no-libraries explanation="Une archive de paquet peut contenir des bibliothèques quel que soit l’outil qui l’installe."}
:::

Utilisez [Gérer les bibliothèques partagées sous Linux](https://labex.io/fr/labs/comptia-manage-shared-libraries-in-linux-590867) pour examiner les relations à l’exécution, puis comparez-les aux métadonnées des paquets dans [Gérer des paquets avec RPM](https://labex.io/fr/labs/rhel-managing-packages-with-rpm-in-linux-590868).

## Résumé

Vous savez maintenant expliquer la résolution des dépendances des paquets.

1. Reconnaître les relations obligatoires, alternatives, versionnées et conflictuelles.
2. Relier les paquets de bibliothèques partagées aux exigences d’ABI à l’exécution.
3. Considérer les noms de fichiers comme une preuve moins solide que l’architecture et la compatibilité des interfaces.
4. Examiner une transaction complète du gestionnaire de paquets avant d’appliquer une réparation.
