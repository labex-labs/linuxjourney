---
index: 11
lang: "fr"
title: "mv (Déplacer)"
meta_title: "mv (Déplacer) - Ligne de commande"
meta_description: "Un guide complet sur la commande mv sous Linux. Apprenez à utiliser la commande bash mv pour déplacer et renommer des fichiers et des répertoires, utilisez des options comme linux mv -t, et évitez les écrasements accidentels."
meta_keywords: "commande mv, commande mv sous linux, linux mv, bash mv, mv -r linux, linux mv -t, déplacer fichiers, renommer fichiers, ligne de commande linux"
---

## Lesson Content

La commande `mv`, abréviation de "move" (déplacer), est un utilitaire fondamental dans tout environnement Linux. Elle sert deux objectifs principaux : renommer des fichiers ou des répertoires et les déplacer vers un emplacement différent. Sa fonctionnalité est à bien des égards similaire à celle de la commande `cp`.

### Renommer des fichiers et des répertoires

L'une des utilisations les plus courantes de la `mv command in linux` est le renommage. La syntaxe est simple : vous spécifiez l'ancien nom et le nouveau nom.

Pour renommer un fichier :

```bash
mv ancien_fichier nouveau_fichier
```

Cette même logique s'applique au renommage des répertoires :

```bash
mv ancien_nom_repertoire nouveau_nom_repertoire
```

### Déplacer des fichiers et des répertoires

L'autre fonction principale de la commande `mv` est de déplacer des éléments d'un emplacement à un autre.

Pour déplacer un seul fichier dans un répertoire différent :

```bash
mv fichier2 /home/pete/Documents
```

Vous pouvez également déplacer plusieurs fichiers à la fois. Il suffit de lister tous les fichiers sources suivis du répertoire cible :

```bash
mv fichier_1 fichier_2 /un_repertoire
```

Une option utile pour cela est `linux mv -t`, qui vous permet de spécifier le répertoire cible en premier. Cela peut être plus clair lors du déplacement de nombreux fichiers.

```bash
mv -t /un_repertoire fichier_1 fichier_2
```

Contrairement à la commande `cp`, vous n'avez pas besoin de l'indicateur `-r` pour déplacer un répertoire. La commande `bash mv` gère les répertoires par défaut. Bien que certains utilisateurs recherchent `mv -r linux`, cette option n'est pas nécessaire pour déplacer des répertoires avec `mv`.

### Options importantes pour la commande mv

Par défaut, si vous déplacez un fichier vers une destination où un fichier portant le même nom existe déjà, `mv` l'écrasera sans avertissement. Pour éviter toute perte de données accidentelle, vous pouvez utiliser les options suivantes :

- **-i (interactif)** : Il s'agit d'une fonctionnalité de sécurité cruciale. Elle vous demandera une confirmation avant d'écraser tout fichier existant.

  ```bash
  mv -i fichier_source repertoire_destination
  ```

- **-b (backup)** : Si vous avez l'intention d'écraser un fichier mais souhaitez conserver l'ancienne version, cette option crée une sauvegarde du fichier de destination. La sauvegarde est généralement renommée avec un suffixe tilde (`~`).

  ```bash
  mv -b fichier1 repertoire_avec_fichier1
  ```

- **-v (verbose)** : Cette option fait en sorte que la commande `mv` affiche ce qu'elle fait, montrant chaque fichier en cours de déplacement ou de renommage.

  ```bash
  mv -v fichier1 fichier2 /un_repertoire
  ```

Maîtriser la `mv command` est essentiel pour une gestion efficace des fichiers sur la ligne de commande.

## Exercise

La pratique rend parfait ! L'expérience pratique est cruciale pour maîtriser les commandes Linux comme `mv`. Ces laboratoires vous aideront à consolider votre compréhension du déplacement et du renommage des fichiers et des répertoires dans un environnement réel :

1. **[Commande mv Linux : Déplacement et renommage de fichiers](https://labex.io/fr/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Entraînez-vous à utiliser la commande `mv` pour déplacer et renommer des fichiers et des répertoires, y compris la compréhension de ses diverses options et comportements.
2. **[Organisation des fichiers et des répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)** - Appliquez vos connaissances de `mv` (ainsi que `cp` et `rm`) dans un défi pratique pour organiser une structure de projet, déplacer des fichiers et nettoyer des répertoires.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des fichiers et des répertoires à l'aide de la commande `mv`.

## Quiz Question

En utilisant la commande `mv`, comment renommeriez-vous un fichier nommé `cat` en `dog` ? Veuillez fournir la commande complète. Note : La réponse est sensible à la casse et doit être saisie en anglais en minuscules.

## Quiz Answer

mv cat dog
