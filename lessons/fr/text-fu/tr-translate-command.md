---
lesson_id: "tr-translate-command"
course_id: "text-fu"
lang: "fr"
order_index: 13
title: "tr (traduire)"
description: "Apprenez à traduire, supprimer et compresser des ensembles de caractères dans un flux d'entrée standard."
meta_title: "tr (traduire) - Text-Fu"
meta_description: "Découvrez la commande Linux tr pour traduire, supprimer ou compresser des caractères et employer des classes."
meta_keywords: "commande tr Linux, tr -d, tr -s, caractères, classes, traitement texte"
---

`tr`, abréviation de translate, traduit, supprime ou compresse les caractères lus sur stdin. Il n'accepte pas de fichier d'entrée ordinaire : utilisez un tube ou une redirection.

```bash
tr [OPTIONS] SET1 [SET2]
```

`tr` agit sur des ensembles de caractères, pas sur des mots ni des expressions régulières générales.

## Traduire des caractères

Avec deux ensembles, les caractères de `SET1` correspondent par position à ceux de `SET2` :

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

Vous pouvez aussi traduire un seul caractère :

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

Ou associer plusieurs caractères par position :

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Citez les ensembles afin que le shell les transmette inchangés. Les caractères absents de `SET1` sont conservés.

:::single-choice{#tr-map-characters} Que produit `printf '%s\n' 'abc123' | tr 'abc' 'ABC'` ?

::option[`ABCABC`]{#tr-uppercase-digits explanation="Les chiffres ne font pas partie de l'ensemble source et restent inchangés."}
::option[`ABC123`]{#tr-uppercase-abc .correct explanation="`a`, `b` et `c` correspondent aux caractères de même position dans `ABC`."}
::option[`abc123ABC`]{#tr-append-set explanation="`tr` traduit les caractères correspondants ; il n'ajoute pas l'ensemble de destination."}
:::

## Supprimer des caractères

`-d` retire chaque caractère correspondant :

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Les classes de caractères décrivent des groupes définis par la locale :

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

Supprimer les retours à la ligne joint les lignes sans séparateur :

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

Les classes décrivent des groupes selon la locale. Supprimer les retours à la ligne joint les lignes sans ajouter de séparateur.

:::single-choice{#tr-delete-digits} Quelle commande retire tous les chiffres de stdin sans toucher aux autres caractères ?

::option[`tr -d '[:digit:]'`]{#tr-delete-digit-class .correct explanation="`-d` supprime tous les membres de la classe des chiffres."}
::option[`tr -s '[:digit:]'`]{#tr-squeeze-digits explanation="`-s` réduit les répétitions mais conserve un caractère par série."}
::option[`tr '[:digit:]'`]{#tr-one-set-no-delete explanation="Une traduction exige normalement un second ensemble ; cette forme ne demande pas une suppression."}
:::

## Compresser les caractères répétés

`-s SET` remplace chaque série d'un caractère indiqué par une seule occurrence :

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

Vous pouvez aussi compresser les retours à la ligne répétés :

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

Un ensemble contenant un espace ordinaire ne compresse ni tabulations ni retours à la ligne.

:::single-choice{#tr-squeeze-spaces} Quelle commande réduit chaque série d'espaces ordinaires de stdin à un espace ?

::option[`tr -s ' '`]{#tr-squeeze-space .correct explanation="`-s` compresse les répétitions des membres de l'ensemble fourni."}
::option[`tr -d ' '`]{#tr-delete-space explanation="`-d` supprimerait tous les espaces."}
::option[`tr ' ' ''`]{#tr-empty-destination explanation="Un ensemble vide n'est pas la méthode claire et portable ; employez `-s`."}
:::

## Employer des classes de caractères et des compléments

Classes courantes : `[:lower:]`, `[:upper:]`, `[:digit:]`, `[:alpha:]`, `[:alnum:]`, `[:space:]` et `[:punct:]`.

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

`-c` complète le premier ensemble ; combiné à `-d`, il conserve seulement les catégories voulues :

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

`-c` complète `SET1`, donc désigne tout caractère qui n'en fait pas partie. Avec `-d`, la seconde commande conserve uniquement les caractères alphanumériques ; elle retire aussi le retour à la ligne.

:::single-choice{#tr-keep-alphanumeric} Que fait `tr -cd '[:alnum:]'` à stdin ?

::option[Il supprime les caractères alphanumériques.]{#tr-delete-alnum explanation="Le complément inverse la cible de `-d` ; l'ensemble alphanumérique est conservé."}
::option[Il supprime tout caractère non alphanumérique.]{#tr-delete-nonalnum .correct explanation="`-c` complète l'ensemble et `-d` supprime ce complément."}
::option[Il convertit lettres et chiffres en majuscules.]{#tr-uppercase-alnum explanation="Aucun ensemble de destination n'effectue ici de changement de casse."}
:::

## Construire des transformations de flux

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

Pour une entrée tabulée simple, traduisez les tabulations en virgules :

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

Comme `tr` lit stdin, un fichier peut être fourni avec `<` :

```bash
$ tr '[:lower:]' '[:upper:]' < names.txt
```

Enchaînez plusieurs `tr` lorsque les étapes sont plus claires séparément. Pour sauvegarder, redirigez stdout vers un autre fichier ; une redirection vers l'entrée la tronquerait avant lecture.

:::single-choice{#tr-read-file-input} Quelle commande fait lire `names.txt` sur stdin et convertit les minuscules en majuscules ?

::option[`tr names.txt '[:lower:]' '[:upper:]'`]{#tr-file-operand explanation="`tr` n'accepte pas ainsi un nom de fichier d'entrée ordinaire."}
::option[`tr -d '[:lower:]' < names.txt`]{#tr-delete-lowercase explanation="Cette forme lit le fichier mais supprime les minuscules."}
::option[`tr '[:lower:]' '[:upper:]' < names.txt`]{#tr-input-redirection .correct explanation="Le shell ouvre le fichier sur stdin et `tr` associe les classes de casse."}
:::

Pour vous exercer :

1. **[Commande Linux tr : traduction de caractères](https://labex.io/fr/labs/linux-linux-tr-command-character-translating-219198)** - Traduisez, supprimez et compressez des caractères avec des classes.

## Résumé

Vous savez transformer des flux de caractères avec `tr`.

1. Associer les caractères de deux ensembles.
2. Supprimer avec `-d`.
3. Compresser les répétitions avec `-s`.
4. Utiliser classes et compléments avec discernement.
5. Fournir l'entrée par stdin et non comme opérande de fichier.
