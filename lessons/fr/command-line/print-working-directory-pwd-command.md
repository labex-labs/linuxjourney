---
lesson_id: "print-working-directory-pwd-command"
course_id: "command-line"
lang: "fr"
order_index: 2
title: "pwd (Afficher le répertoire de travail)"
description: "Apprenez à utiliser pwd pour connaître votre emplacement actuel dans le système de fichiers Linux."
meta_title: "pwd (Afficher le répertoire de travail) - Ligne de commande"
meta_description: "Apprenez la commande Linux pwd, ce que signifie afficher le répertoire de travail, et comment les chemins absolus montrent votre emplacement actuel dans le système de fichiers."
meta_keywords: "commande pwd, linux pwd, afficher répertoire de travail, répertoire courant linux, chemin absolu, système de fichiers linux, arbre des répertoires"
---

Sous Linux, les fichiers et répertoires sont organisés selon une hiérarchie appelée système de fichiers. Avant de vous y déplacer avec assurance, vous devez savoir où vous vous trouvez. La commande `pwd` répond à cette question en affichant le répertoire de travail actuel.

## L'arborescence des répertoires sous Linux

Tout le système de fichiers part d'un unique répertoire supérieur appelé répertoire racine, représenté par une barre oblique (`/`). À partir de cette racine, l'arborescence se ramifie en sous-répertoires, qui peuvent eux-mêmes contenir des fichiers et d'autres sous-répertoires.

Voici un exemple simplifié de cette structure :

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

:::single-choice{#identify-root-subdirectories}
Dans l'arborescence ci-dessus, quelle est la relation de `home` et `etc` avec `/` ?

::option[Ce sont des sous-répertoires qui partent de `/`.]{#root-subdirectories .correct explanation="Ces deux répertoires apparaissent directement sous `/` dans l'arborescence. Le système de fichiers se ramifie en sous-répertoires à partir de sa racine."}
::option[Ce sont des fichiers stockés dans le répertoire `bin`.]{#files-inside-bin explanation="L'arborescence place `home` et `etc` au même niveau que `bin`, pas à l'intérieur. Dans cet exemple, il s'agit de répertoires et non de fichiers."}
::option[Ce sont d'autres noms du répertoire racine.]{#alternate-root-names explanation="Linux possède une seule racine de système de fichiers, représentée par `/`. `home` et `etc` sont des répertoires situés dessous."}
:::

## Comprendre les chemins de fichiers

L'emplacement d'un fichier ou d'un répertoire est décrit par son chemin. Un chemin est une suite de répertoires qui mène d'un point de départ à une destination précise.

Par exemple, si le répertoire `/home` contient un dossier `pete`, qui contient lui-même un dossier `Movies`, le chemin complet est :

```plaintext
/home/pete/Movies
```

Un chemin qui commence par `/` est absolu, car il part du répertoire racine. Un chemin comme `Movies` est relatif, car il dépend de votre emplacement actuel.

:::single-choice{#recognize-absolute-path}
Pourquoi `/home/pete/Movies` est-il un chemin absolu ?

::option[Il contient plusieurs noms de répertoires séparés par `/`.]{#contains-directories explanation="Les chemins absolus comme relatifs peuvent contenir plusieurs noms. Le type dépend du point de départ, pas du nombre de noms."}
::option[Il se termine par un répertoire nommé `Movies`.]{#ends-with-movies explanation="Le nom de la destination ne détermine pas si le chemin est absolu. Un chemin absolu se reconnaît à son départ depuis la racine."}
::option[Il part de la racine avec un `/` initial.]{#starts-at-root .correct explanation="Un chemin absolu commence au répertoire racine. La barre oblique initiale indique ce point de départ."}
:::

## Que signifie pwd sous Linux ?

`pwd` signifie « print working directory », c'est-à-dire afficher le répertoire de travail. Votre répertoire de travail est celui où se trouve actuellement le shell. Les commandes qui utilisent des chemins relatifs partent de cet emplacement.

:::single-choice{#expand-pwd-name}
Que signifie `pwd` ?

::option[Print working directory]{#print-working-directory .correct explanation="Le nom décrit exactement l'action de la commande : elle affiche le répertoire de travail actuel du shell."}
::option[Present working directory]{#present-working-directory explanation="Dans la langue courante, on peut parler du répertoire présent, mais ce n'est pas le développement de `pwd`."}
::option[Print whole directory]{#print-whole-directory explanation="`pwd` indique le chemin du répertoire actuel ; elle n'affiche pas tout son contenu."}
:::

## Utiliser la commande pwd

Pour connaître votre répertoire actuel, tapez `pwd` et appuyez sur Entrée.

```bash
$ pwd
/home/pete
```

La sortie est un chemin absolu. Dans cet exemple, le shell se trouve dans le répertoire personnel de l'utilisateur `pete`.

La sortie exacte peut différer sur votre système, car votre nom d'utilisateur, votre répertoire personnel et votre emplacement peuvent être autres. `pwd` ne fait qu'afficher une information ; elle ne change pas le répertoire de travail. À l'inverse, `cd` change le répertoire où se trouve le shell.

:::single-choice{#check-location-without-changing-it}
Quelle action vérifie votre répertoire actuel sans le modifier ?

::option[Exécuter `cd` et lire le répertoire dans lequel la commande se déplace.]{#run-cd explanation="`cd` change le répertoire de travail ; elle ne répond pas au besoin de vérifier l'emplacement sans le modifier."}
::option[Saisir `/home/pete` et utiliser ce chemin comme commande.]{#run-path explanation="Un chemin absolu désigne un emplacement, mais le chemin seul n'est pas la commande qui indique le répertoire actuel."}
::option[Exécuter `pwd` et lire le chemin absolu affiché.]{#run-pwd .correct explanation="`pwd` indique l'emplacement actuel du shell sans le déplacer. Vous pouvez donc l'utiliser sans risque pour confirmer où vous êtes."}
:::

## Pourquoi pwd est utile

Utilisez `pwd` lorsque :

- vous suivez des instructions et devez confirmer votre emplacement ;
- une commande a échoué à cause d'un chemin incorrect ;
- vous avez parcouru plusieurs répertoires et ne savez plus où vous êtes ;
- vous voulez copier le chemin actuel dans une autre commande.

Par exemple :

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

Vous savez ainsi que `app.py` et `README.md` se trouvent dans `/home/pete/projects`.

Pour consolider votre compréhension de la navigation dans le système de fichiers et de votre emplacement actuel, essayez ces laboratoires :

1. **[Commande Linux pwd : afficher un répertoire](https://labex.io/fr/labs/linux-linux-pwd-command-directory-displaying-209734)** — Découvrez précisément la commande `pwd` et entraînez-vous à retrouver votre répertoire actuel.
2. **[Navigation dans les répertoires Linux](https://labex.io/fr/labs/linux-directory-navigation-387844)** — Parcourez différents répertoires pour approfondir votre compréhension des chemins et de la structure du système de fichiers.
3. **[Commande Linux cd : changer de répertoire](https://labex.io/fr/labs/linux-linux-cd-command-directory-changing-209733)** — Apprenez plusieurs façons de changer de répertoire avec `cd` et d'explorer l'arborescence.

## Résumé

Vous savez maintenant utiliser `pwd` pour connaître votre emplacement actuel dans le système de fichiers Linux.

1. Reconnaître la racine de l'arborescence.
2. Distinguer un chemin absolu d'un chemin relatif.
3. Expliquer la signification de `pwd` et ce qu'elle affiche.
4. Vérifier le répertoire de travail sans le modifier.
