---
index: 3
lang: "fr"
title: "cd (Changer de répertoire)"
meta_title: "cd (Changer de répertoire) - Ligne de commande"
meta_description: "Apprenez à utiliser la commande 'cd' sous Linux pour naviguer dans les répertoires. Comprenez les chemins absolus, relatifs et les raccourcis utiles. Commencez votre parcours Linux !"
meta_keywords: "commande cd, changer de répertoire, chemins Linux, chemin absolu, chemin relatif, tutoriel Linux, Linux débutant, navigation Linux"
---

## Lesson Content

Maintenant que vous savez où vous êtes, voyons si nous pouvons nous déplacer un peu dans le système de fichiers. N'oubliez pas que nous devrons nous orienter en utilisant des chemins. Il existe deux façons différentes de spécifier un chemin : avec des chemins absolus et relatifs.

- Chemin absolu : C'est le chemin à partir du répertoire racine. La racine est le chef. Le répertoire racine est généralement représenté par une barre oblique (`/`). Chaque fois que votre chemin commence par `/`, cela signifie que vous partez du répertoire racine. Par exemple, `/home/pete/Desktop`.

- Chemin relatif : C'est le chemin à partir de votre position actuelle dans le système de fichiers. Si j'étais à l'emplacement `/home/pete/Documents` et que je voulais accéder à un répertoire à l'intérieur de `Documents` appelé `taxes`, je n'ai pas besoin de spécifier tout le chemin depuis la racine comme `/home/pete/Documents/taxes` ; je peux simplement aller à `taxes/` à la place.

Maintenant que vous savez comment fonctionnent les chemins, nous avons juste besoin de quelque chose pour nous aider à changer le répertoire souhaité. Heureusement, nous avons `cd` ou « change directory » pour cela.

```bash
cd /home/pete/Pictures
```

J'ai donc maintenant changé mon emplacement de répertoire pour `/home/pete/Pictures`.

Maintenant, à partir de ce répertoire, j'ai un dossier à l'intérieur appelé `Hawaii`. Je peux naviguer vers ce dossier avec :

```bash
cd Hawaii
```

Remarquez comment j'ai juste utilisé le nom du dossier ? C'est parce que j'étais déjà dans `/home/pete/Pictures`.

Il peut devenir assez fatigant de naviguer avec des chemins absolus et relatifs tout le temps. Heureusement, il existe des raccourcis pour vous aider.

- `.` (répertoire actuel) : C'est le répertoire dans lequel vous vous trouvez actuellement.
- `..` (répertoire précédent) : Vous emmène au répertoire au-dessus de votre répertoire actuel.
- `~` (répertoire personnel) : Ce répertoire correspond par défaut à votre « répertoire personnel », tel que `/home/pete`.
- `-` (répertoire précédent) : Cela vous ramènera au répertoire précédent où vous étiez juste avant.

```bash
cd .
cd ..
cd ~
cd -
```

Essayez-les !

## Exercise

1. Exécutez la commande `cd` sans aucun drapeau. Où vous emmène-t-elle ?

Pour une pratique concrète de la commande `cd`, essayez ce laboratoire interactif :

- [Linux cd Command: Directory Changing](https://labex.io/fr/labs/linux-linux-cd-command-directory-changing-209733)

## Quiz Question

Si vous êtes dans `/home/pete/Pictures` et que vous voulez aller dans `/home/pete`, quel est un bon raccourci à utiliser ?

## Quiz Answer

cd ..
