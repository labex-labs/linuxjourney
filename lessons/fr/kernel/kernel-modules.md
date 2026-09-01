---
lesson_id: "kernel-modules"
course_id: "kernel"
lang: "fr"
order_index: 6
title: "Modules du noyau"
description: "Découvrez comment examiner, charger, configurer et retirer sans risque les modules propres à une version du noyau Linux."
meta_title: "Modules du noyau - Noyau"
meta_description: "Découvrez les modules du noyau Linux et apprenez à les répertorier, charger et décharger avec lsmod, modinfo et modprobe."
meta_keywords: "modules noyau Linux, modprobe, lsmod, modinfo, gestion noyau, charger module, décharger module"
---

Un module chargeable est du code privilégié qui peut étendre le noyau actif avec un pilote, un système de fichiers, une fonction réseau ou un autre sous-système. Les modules évitent d'intégrer chaque fonction facultative dans une seule image du noyau, mais leur chargement agrandit la surface d'attaque de confiance.

## Répertorier et examiner les modules

Affichez les modules actuellement chargés :

```bash
$ lsmod
```

La sortie provient d'un état du noyau comme `/proc/modules` et comprend le nom, la taille et un nombre d'utilisations ou des dépendances. Un nombre apparemment nul ne prouve pas que la suppression est sûre ; un pilote peut encore posséder des périphériques actifs ou participer à l'état d'un sous-système.

Examinez un module disponible pour le noyau actif avec :

```bash
$ modinfo NOM_DU_MODULE
```

`modinfo` peut afficher le nom du fichier, les alias, paramètres, la licence, la description et les informations de signature. Considérez ces métadonnées comme descriptives, pas comme une preuve de confiance ou de compatibilité avec la charge.

:::single-choice{#kernel-modules-lsmod-purpose} Qu'affiche `lsmod` ?

::option[Tous les paquets de modules disponibles dans les dépôts distants.]{#kernel-modules-repository-list explanation="L'inventaire des dépôts exige des requêtes du gestionnaire de paquets."}
::option[Uniquement les pilotes compilés directement dans l'image du noyau.]{#kernel-modules-builtins explanation="Les fonctions intégrées ne sont pas des modules chargeables et n'apparaissent normalement pas dans lsmod."}
::option[Les modules actuellement chargés dans le noyau actif.]{#kernel-modules-loaded-list .correct explanation="La liste reflète l'état réel des modules ainsi que les informations de dépendances et d'utilisation."}
:::

## Charger avec `modprobe`

Chargez un module par son nom :

```bash
$ sudo modprobe NOM_DU_MODULE
```

`modprobe` consulte les index de dépendances, alias et configurations du noyau actif sous `/lib/modules/$(uname -r)/`. Il charge les dépendances requises et transmet les paramètres configurés. `insmod` insère au contraire un seul fichier de module indiqué directement sans offrir la même résolution des dépendances.

Avant le chargement, confirmez l'origine du module, la politique de signature, la compatibilité avec la version du noyau, les paramètres, l'association matérielle attendue et le retour arrière. Secure Boot ou le verrouillage du noyau peut rejeter les modules non signés ; forcer du code incompatible risque un plantage ou une compromission.

:::single-choice{#kernel-modules-modprobe-dependencies} Pourquoi préfère-t-on normalement `modprobe` à l'emploi direct d'`insmod` ?

::option[Il exécute le module entièrement dans l'espace utilisateur non privilégié.]{#kernel-modules-modprobe-userspace explanation="Le module inséré s'exécute comme code privilégié du noyau."}
::option[Il garantit que chaque module tiers est signé et sûr.]{#kernel-modules-modprobe-guarantee explanation="L'application des signatures dépend des règles et une signature valide ne prouve pas l'absence de défauts."}
::option[Il résout les alias, les dépendances et la configuration des modules.]{#kernel-modules-modprobe-resolves .correct explanation="Modprobe emploie l'arborescence indexée des modules de la version exacte active."}
:::

## Paramètres des modules et chargement au démarrage

Les règles persistantes de paramètres et d'alias se placent dans un fichier `.conf` sous `/etc/modprobe.d/` :

```text
options example_module mode=careful
```

Cette ligne influence la manière dont modprobe charge le module ; elle ne demande pas à elle seule son chargement au démarrage. Une simple liste de modules à charger au démarrage se place couramment sous `/etc/modules-load.d/` :

```text
example_module
```

Les alias matériels déclenchent souvent un chargement automatique sans liste explicite. Pour les modules nécessaires pendant le démarrage précoce, mettez à jour l'initramfs selon la procédure documentée de la distribution après les changements de configuration.

:::single-choice{#kernel-modules-options-versus-load} Que fait une ligne `options` dans `/etc/modprobe.d/` ?

::option[Elle garantit à elle seule le chargement du module à chaque démarrage.]{#kernel-modules-options-autoload explanation="Les demandes de chargement au démarrage emploient un autre mécanisme, comme la configuration modules-load ou les alias de périphériques."}
::option[Elle définit les paramètres employés lors du chargement du module nommé.]{#kernel-modules-options-parameters .correct explanation="Modprobe applique les arguments clé-valeur configurés pendant l'insertion."}
::option[Elle compile le module pour chaque version de noyau installée.]{#kernel-modules-options-compiles explanation="La configuration ne construit pas de modules binaires."}
:::

## Liste noire et limites

Une configuration modprobe peut contenir :

```text
blacklist example_module
```

La liste noire supprime normalement le chargement automatique au moyen des alias du module. Elle ne décharge pas un module déjà actif, ne le retire pas d'un initramfs et n'empêche pas nécessairement un chargement explicite par son nom exact ou comme dépendance. Le renforcement de la sécurité exige une combinaison adaptée à la menace : disponibilité du module, application des signatures, contenu de l'initramfs, paramètres de démarrage et règles.

:::single-choice{#kernel-modules-blacklist-effect} Que supprime principalement une ligne modprobe `blacklist` élémentaire ?

::option[Le chargement automatique par les alias du module.]{#kernel-modules-blacklist-aliases .correct explanation="La directive n'interdit pas universellement toutes les voies par lesquelles le code peut être ou devenir chargé."}
::option[L'exécution de chaque programme utilisateur portant un nom semblable.]{#kernel-modules-blacklist-user-programs explanation="La configuration modprobe s'applique à la résolution des modules du noyau."}
::option[Tout le code du noyau compilé dans l'image.]{#kernel-modules-blacklist-builtins explanation="Une fonction intégrée ne peut ni être déchargée, ni bloquée comme module."}
:::

## Retirer un module sans risque

Demandez son retrait avec :

```bash
$ sudo modprobe -r NOM_DU_MODULE
```

Modprobe peut retirer les dépendances désormais inutilisées lorsqu'il convient. Le noyau refuse l'opération lorsque le suivi ordinaire des références indique que le module est occupé, mais ne vous fiez pas à ce seul contrôle. Arrêtez les services, démontez les systèmes de fichiers, détachez les périphériques, mettez le réseau au repos et confirmez un autre pilote ou une voie de récupération avant de retirer le code qui prend en charge du matériel actif.

Ne forcez jamais le déchargement d'un module sur un système à préserver. Des bogues de retrait ou une activité encore en cours peuvent faire planter le noyau ou corrompre des données.

:::single-choice{#kernel-modules-remove-command} Quelle commande demande le retrait, tenant compte des dépendances, d'un module nommé ?

::option[`lsmod -r NOM_DU_MODULE`]{#kernel-modules-lsmod-remove explanation="Lsmod est un outil d'affichage en lecture seule et ne retire rien."}
::option[`uname -r NOM_DU_MODULE`]{#kernel-modules-uname-remove explanation="Uname indique des informations sur le noyau et ne gère pas les modules."}
::option[`modprobe -r NOM_DU_MODULE`]{#kernel-modules-modprobe-remove .correct explanation="Le mode de retrait tient compte des relations de dépendances indexées autour du module demandé."}
:::

Utilisez [Gérer les modules du noyau sous Linux](https://labex.io/fr/labs/comptia-manage-kernel-modules-in-linux-590865) pour vous exercer avec les modules désignés comme sûrs par le laboratoire.

## Résumé

Vous savez maintenant gérer les modules en respectant leur risque au niveau du noyau.

1. Employer `lsmod` pour l'état réel et `modinfo` pour les métadonnées disponibles.
2. Employer `modprobe` pour un chargement tenant compte des alias et dépendances.
3. Distinguer les paramètres modprobe des demandes de chargement au démarrage.
4. Considérer la liste noire comme une règle limitée plutôt qu'un blocage absolu.
5. Mettre chaque consommateur au repos avant `modprobe -r`.
