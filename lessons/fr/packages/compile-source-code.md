---
lesson_id: "compile-source-code"
course_id: "packages"
lang: "fr"
order_index: 7
title: "Compiler le code source"
description: "Découvrez comment vérifier, configurer, construire, tester, préparer et suivre un logiciel compilé depuis son code source."
meta_title: "Compiler le code source - Paquets"
meta_description: "Apprenez à compiler du code source sous Linux avec configure et make, puis à préparer et suivre proprement l’installation obtenue."
meta_keywords: "compiler depuis le code source, construire du code source, compilation Linux, make install, checkinstall, build-essential, script configure, makefile, tutoriel Linux"
---

La construction depuis les sources peut fournir une version ou une fonctionnalité absente des dépôts configurés, mais elle vous transfère le travail d’intégration, de mise à jour et de confiance normalement assuré par la distribution. Préférez un paquet pris en charge par la distribution lorsqu’il répond au besoin.

## Vérifier et lire avant de construire

Obtenez le code source depuis le canal authentifié de publication du projet en amont. Vérifiez sa signature ou sa somme de contrôle par une voie de confiance, puis examinez l’archive avant de l’extraire dans un répertoire intermédiaire sans privilèges. Lisez les fichiers tels que `README`, `INSTALL`, `SECURITY` et la documentation de construction du projet.

Les instructions de construction sont du code exécutable. Un script `configure`, une définition de construction, un test ou un greffon de compilateur peut exécuter des commandes arbitraires en tant que votre utilisateur. Ne construisez pas de code source non fiable et n’exécutez pas la construction elle-même avec `sudo`.

:::single-choice{#compile-source-code-build-privilege} Pourquoi l’étape de compilation doit-elle normalement s’exécuter sans `sudo` ?

::option[Les compilateurs refusent de produire du code machine pour l’utilisateur root.]{#compile-source-code-root-compiler explanation="Les compilateurs peuvent s’exécuter en tant que root, mais cela augmente inutilement le risque."}
::option[`sudo` supprime automatiquement chaque fichier objet produit.]{#compile-source-code-sudo-delete explanation="L’élévation des privilèges ne supprime pas intrinsèquement les résultats de construction."}
::option[La logique de construction peut exécuter des commandes arbitraires et n’a généralement besoin d’aucun privilège système.]{#compile-source-code-unprivileged-build .correct explanation="Une construction sans privilèges limite les conséquences des erreurs ou d’instructions malveillantes."}
:::

## Installer les prérequis de construction

Sur un système de développement de la famille Debian, un point de départ courant est :

```bash
$ sudo apt install build-essential
```

Cette commande installe un compilateur de base et des outils de construction, mais pas toutes les dépendances nécessaires à chaque projet. Les projets peuvent aussi exiger des environnements d’exécution de langages, des générateurs, des outils de systèmes de construction, des en-têtes de développement ou des versions précises de bibliothèques. Installez les prérequis depuis des dépôts de confiance et distinguez les dépendances de construction de celles nécessaires à l’exécution.

:::single-choice{#compile-source-code-build-essential-scope} Que fournit `build-essential` sur un système de la famille Debian ?

::option[Un ensemble de base d’outils courants de compilation et de construction.]{#compile-source-code-baseline-tools .correct explanation="Il fournit des outils fondamentaux, mais ne peut anticiper toutes les bibliothèques et tous les générateurs propres aux projets."}
::option[Chaque dépendance de chaque projet source.]{#compile-source-code-all-dependencies explanation="Les projets déclarent des exigences supplémentaires, parfois liées à une version précise."}
::option[La garantie que le code source téléchargé est digne de confiance.]{#compile-source-code-trust-guarantee explanation="L’installation des outils n’authentifie pas une publication source distincte."}
:::

## Configurer et construire

Un projet traditionnel de style Autoconf emploie :

```bash
$ ./configure --prefix=/usr/local
$ make
```

`configure` examine l’environnement et génère les fichiers de construction selon les options choisies. `make` lit les règles de dépendances et de commandes, généralement dans un `Makefile`, puis crée les cibles demandées.

Cette séquence n’est pas universelle. Les projets peuvent employer CMake, Meson, Ninja, des outils propres à un langage ou des scripts personnalisés. Suivez la documentation de la version exacte au lieu d’exécuter `./configure` uniquement par habitude. Un répertoire de construction distinct de l’arborescence source peut isoler les fichiers générés lorsque le système de construction le permet.

:::single-choice{#compile-source-code-make-role} Dans la procédure traditionnelle, que fait `make` ?

::option[Il enregistre chaque résultat dans la base des paquets de la distribution.]{#compile-source-code-make-package-db explanation="La compilation seule ne crée aucun enregistrement de propriété dans la base native des paquets."}
::option[Il télécharge automatiquement une publication source authentifiée.]{#compile-source-code-make-download explanation="L’acquisition et la vérification de la source précèdent la construction locale, sauf définition explicite contraire du projet."}
::option[Il exécute les règles applicables de la description de construction.]{#compile-source-code-make-rules .correct explanation="Make évalue les dépendances et exécute les commandes nécessaires pour mettre les cibles sélectionnées à jour."}
:::

## Tester avant l’installation

Exécutez la cible de test documentée par le projet, par exemple :

```bash
$ make check
```

La cible réelle peut être `test`, `check` ou une commande distincte. Analysez les échecs au lieu d’installer un résultat non testé. Les tests peuvent nécessiter un accès réseau, des services, du matériel particulier ou une isolation ; examinez-les avant leur exécution comme tout autre code de construction.

:::single-choice{#compile-source-code-test-failure} Que faut-il faire lorsque la suite de tests documentée échoue ?

::option[Exécuter immédiatement la même installation en tant que root.]{#compile-source-code-install-after-failure explanation="Les privilèges ne résolvent pas une erreur de justesse inconnue et en augmentent les conséquences."}
::option[Supprimer la base du gestionnaire de paquets pour éviter les conflits.]{#compile-source-code-delete-database explanation="La base native est sans rapport avec la résolution d’un échec de test du code source et ne doit pas être supprimée."}
::option[Analyser l’échec avant d’installer le résultat.]{#compile-source-code-investigate-tests .correct explanation="Un test en échec peut révéler des dépendances incompatibles, un défaut de construction ou des hypothèses sur l’environnement."}
:::

## Préparer et suivre l’installation

`sudo make install` peut copier directement des fichiers dans les préfixes système sans les enregistrer dans la base native des paquets. Les cibles de désinstallation sont facultatives et parfois incomplètes, tandis que des mises à niveau ultérieures peuvent écraser ou abandonner des fichiers.

Préférez l’une de ces méthodes contrôlées :

- construire un paquet natif officiel avec les outils de la distribution ;
- installer sous un préfixe clairement séparé tel que `/usr/local` lorsque la politique le permet ;
- préparer les fichiers dans une racine de paquet temporaire avec un mécanisme pris en charge tel que `DESTDIR` ;
- employer un préfixe utilisateur sans privilèges, un environnement isolé ou un conteneur selon le besoin.

`checkinstall` peut créer un paquet simple pour certaines procédures `make install`, mais il n’est pas universel et ne remplace pas une recette de paquet de qualité, examinée pour la distribution. Ne le considérez jamais comme une règle absolue. Avant toute copie privilégiée, examinez la liste des fichiers préparés, leur propriété, leurs permissions, leurs chemins ainsi que le plan de désinstallation ou de mise à niveau.

:::single-choice{#compile-source-code-destdir-purpose} Quel est le but d’une installation intermédiaire prise en charge avec `DESTDIR` ?

::option[Placer les fichiers destinés à l’installation sous une racine temporaire afin de les examiner ou de les empaqueter.]{#compile-source-code-stage-root .correct explanation="La préparation sépare la collecte des fichiers de leur écriture immédiate dans le préfixe du système actif."}
::option[Transformer le compilateur en dépôt de paquets distant.]{#compile-source-code-destdir-repository explanation="La variable redirige les chemins d’installation et ne publie pas de métadonnées de dépôt."}
::option[Ignorer la compilation et télécharger des binaires inconnus à la place.]{#compile-source-code-destdir-download explanation="La préparation intervient après la construction et ne la remplace pas par un téléchargement binaire externe."}
:::

Utilisez [Construire un logiciel depuis le code source sous Linux](https://labex.io/fr/labs/comptia-build-software-from-source-code-in-linux-590853) dans un environnement jetable pour vous exercer sans mélanger des fichiers expérimentaux à un système de production.

## Résumé

Vous savez maintenant traiter la construction depuis les sources comme une chaîne d’approvisionnement logicielle contrôlée.

1. Authentifier la source et considérer ses instructions comme du code exécutable à examiner.
2. Installer les prérequis explicites depuis des dépôts de confiance.
3. Configurer, construire et tester sans privilèges inutiles.
4. Préparer et examiner les résultats avant l’installation système.
5. Suivre les fichiers installés au moyen d’un paquet natif ou d’un préfixe isolé choisi délibérément.
