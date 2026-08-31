---
lesson_id: "change-directory-cd-command"
course_id: "command-line"
lang: "fr"
order_index: 3
title: "cd (Changer de répertoire)"
description: "Apprenez à utiliser cd avec des chemins et des raccourcis pour parcourir le système de fichiers Linux."
meta_title: "cd (Changer de répertoire) - Ligne de commande"
meta_description: "Apprenez la commande Linux cd avec des exemples de chemins absolus, chemins relatifs, raccourcis vers le répertoire personnel, répertoires parents et navigation vers le répertoire précédent."
meta_keywords: "commande cd, commande linux cd, changer de répertoire, cd répertoire parent, cd home, cd répertoire précédent, chemin absolu, chemin relatif"
---

Pour parcourir le système de fichiers Linux, vous indiquez votre destination à l'aide de chemins. La commande principale est `cd`, abréviation de « change directory », qui modifie le répertoire de travail actuel du shell.

La destination doit être un répertoire et non un fichier ordinaire. Si elle n'existe pas, si son nom est mal saisi ou si vous n'avez pas la permission d'y entrer, `cd` signale une erreur au lieu de changer d'emplacement.

La syntaxe élémentaire est :

```bash
cd [DIRECTORY]
```

## Comprendre les chemins

Un chemin peut être absolu ou relatif.

- **Chemin absolu** : chemin complet qui part du répertoire racine (`/`), par exemple `/home/pete/Desktop`.
- **Chemin relatif** : chemin fondé sur l'emplacement actuel. Si vous vous trouvez dans `/home/pete/Documents` et souhaitez accéder au sous-répertoire `taxes`, vous pouvez utiliser `taxes/`.

:::single-choice{#recognize-absolute-cd-path}
Quelle affirmation décrit correctement un chemin absolu ?

::option[Il part du répertoire actuellement utilisé par le shell.]{#begins-at-current-directory explanation="Un chemin qui dépend de l'emplacement actuel du shell est relatif ; il ne part pas nécessairement de la racine."}
::option[Il ne contient que le nom du répertoire final, sans ses parents.]{#contains-final-name-only explanation="Un nom de destination seul est normalement interprété par rapport au répertoire actuel. Un chemin absolu inclut son parcours depuis `/`."}
::option[Il part du répertoire racine, représenté par `/`.]{#begins-at-root .correct explanation="Un chemin absolu commence à la racine du système de fichiers. Le `/` initial rend son point de départ indépendant du répertoire actuel."}
:::

## Utiliser la commande cd

Pour accéder à un répertoire précis avec un chemin absolu, saisissez :

```bash
$ cd /home/pete/Pictures
```

Cette commande vous place directement dans `Pictures`.

Confirmez votre emplacement avec `pwd` :

```bash
$ pwd
/home/pete/Pictures
```

:::single-choice{#verify-changed-directory}
Quelle commande confirme l'emplacement actuel du shell après `cd` ?

::option[`cd`]{#cd-command explanation="`cd` change le répertoire actuel, mais n'affiche normalement pas le chemin complet obtenu. Utilisez `pwd` pour le confirmer."}
::option[`ls`]{#ls-command explanation="`ls` affiche le contenu d'un répertoire. Elle aide à inspecter un emplacement, mais `pwd` indique l'emplacement lui-même."}
::option[`pwd`]{#pwd-command .correct explanation="`pwd` affiche le répertoire de travail actuel et permet de vérifier où `cd` a déplacé le shell."}
:::

## Accéder à un sous-répertoire

Si vous vous trouvez déjà dans un répertoire et voulez ouvrir l'un de ses sous-répertoires, utilisez un chemin relatif. Par exemple, si `/home/pete/Pictures` contient un dossier `Hawaii` :

```bash
$ cd Hawaii
```

Seul le nom du dossier suffit puisque vous vous trouvez déjà dans son parent, `/home/pete/Pictures`.

## Raccourcis de navigation essentiels

Les chemins complets peuvent être fastidieux. Le shell fournit plusieurs raccourcis :

- `.` (répertoire actuel) : représente le répertoire où vous vous trouvez ;
- `..` (répertoire parent) : remonte d'un niveau vers le répertoire qui contient le répertoire actuel ;
- `~` (répertoire personnel) : représente votre répertoire personnel, par exemple `/home/pete` ;
- `-` (répertoire précédent) : revient au dernier répertoire visité.

Utilisez-les avec `cd` :

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

:::single-choice{#move-to-parent-directory}
Depuis `/home/pete/Pictures`, quelle commande mène à `/home/pete` ?

::option[`cd .`]{#cd-current explanation="`.` représente le répertoire actuel ; cette commande laisse donc le shell dans `/home/pete/Pictures`."}
::option[`cd -`]{#cd-previous explanation="`-` revient au répertoire de travail précédent, qui n'est pas nécessairement le parent. Utilisez `..` pour remonter d'un niveau."}
::option[`cd ..`]{#cd-parent .correct explanation="`..` représente le parent du répertoire actuel. Le parent de `Pictures` est `/home/pete`."}
:::

:::single-choice{#return-to-previous-directory}
Quelle commande revient au répertoire utilisé juste avant le répertoire actuel ?

::option[`cd -`]{#previous-directory .correct explanation="`cd -` revient au répertoire de travail précédent, qui peut se trouver n'importe où dans le système de fichiers."}
::option[`cd ..`]{#parent-directory explanation="`cd ..` remonte au répertoire parent. Le parent et le répertoire précédent ne sont pas toujours identiques."}
::option[`cd ~`]{#home-directory explanation="`cd ~` ouvre votre répertoire personnel ; cette commande ne mémorise pas le répertoire visité juste avant."}
:::

Expérimentez avec ces raccourcis pour gagner en efficacité.

## Exemples pratiques de cd

Accédez à votre répertoire personnel :

```bash
$ cd
```

`cd` sans argument de répertoire vous ramène également au répertoire personnel.

Remontez de deux niveaux :

```bash
$ cd ../..
```

Accédez à un répertoire dont le nom contient des espaces en le plaçant entre guillemets :

```bash
$ cd "Vacation Photos"
```

:::single-choice{#enter-directory-with-spaces}
Quelle commande traite `Vacation Photos` comme un seul nom de répertoire ?

::option[`cd Vacation Photos`]{#unquoted-directory-name explanation="Sans guillemets, le shell transmet `Vacation` et `Photos` comme deux arguments au lieu d'un seul nom."}
::option[`"cd Vacation Photos"`]{#quote-entire-command explanation="Placer toute la ligne entre guillemets la transforme en un unique nom de commande. La commande doit rester hors des guillemets du chemin."}
::option[`cd "Vacation Photos"`]{#quote-directory-name .correct explanation="Les guillemets regroupent les deux mots en un seul argument de chemin pour `cd`."}
:::

Revenez au répertoire précédent :

```bash
$ cd -
/home/pete/Documents
```

Pour consolider votre maîtrise de la navigation, essayez ces laboratoires :

1. **[Commande Linux cd : changer de répertoire](https://labex.io/fr/labs/linux-linux-cd-command-directory-changing-209733)** — Apprenez différentes méthodes pour changer de répertoire, comprendre les chemins et explorer l'arborescence.
2. **[Navigation dans les répertoires Linux](https://labex.io/fr/labs/linux-directory-navigation-387844)** — Testez vos connaissances des commandes essentielles en parcourant plusieurs répertoires.
3. **[Créer la structure d'un nouveau projet](https://labex.io/fr/labs/linux-setting-up-a-new-project-structure-387859)** — Créez une structure de projet et parcourez-la avec des commandes comme `mkdir` et `cd`.

## Résumé

Vous savez maintenant utiliser `cd` pour parcourir les répertoires avec des chemins complets et les raccourcis du shell.

1. Distinguer les chemins absolus des chemins relatifs.
2. Changer de répertoire et vérifier le résultat avec `pwd`.
3. Accéder aux répertoires parent, personnel et précédent.
4. Ouvrir des répertoires dont le nom contient des espaces.
5. Reconnaître les erreurs courantes de chemin et de permission.
