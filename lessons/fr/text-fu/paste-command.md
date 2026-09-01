---
lesson_id: "paste-command"
course_id: "text-fu"
lang: "fr"
order_index: 7
title: "paste"
description: "Apprenez à fusionner des lignes correspondantes ou à sérialiser des lignes avec des délimiteurs configurables."
meta_title: "paste - Text-Fu"
meta_description: "Utilisez la commande Linux paste pour fusionner les lignes de plusieurs fichiers avec le délimiteur de votre choix."
meta_keywords: "commande paste Linux, fusionner lignes, délimiteur, traitement de texte"
---

`paste` combine des lignes en colonnes. Par défaut, il prend une ligne de chaque fichier, les joint par une tabulation et recommence jusqu'à la fin de toutes les entrées.

## Fusionner des fichiers côte à côte

```bash
$ printf 'alice\nbob\n' > names.txt
$ printf 'admin\nviewer\n' > roles.txt
```

Fournissez ensuite les deux fichiers à `paste` :

```bash
$ paste names.txt roles.txt
alice	admin
bob	viewer
```

L'espacement est une tabulation. Contrairement à `cat`, qui écrit des fichiers complets à la suite, `paste` combine leurs lignes correspondantes.

:::single-choice{#paste-corresponding-lines} `first.txt` contient `A` puis `B`, et `second.txt` contient `1` puis `2`. Que produit `paste first.txt second.txt` par défaut ?

::option[`A`, `B`, `1` et `2` sur quatre lignes.]{#paste-concatenated-files explanation="Cela correspondrait à une concaténation ; `paste` combine les lignes correspondantes."}
::option[Les quatre valeurs sur une ligne sans séparateur.]{#paste-one-line-no-separator explanation="La sérialisation exige `-s` et le séparateur par défaut est une tabulation."}
::option[`A` avec `1`, puis `B` avec `2`, séparés par des tabulations.]{#paste-parallel-result .correct explanation="Le mode parallèle prend une ligne de chaque fichier pour chaque ligne de sortie."}
:::

## Choisir un délimiteur

`-d LIST` remplace la tabulation :

```bash
$ paste -d ':' names.txt roles.txt
alice:admin
bob:viewer
```

Citez les délimiteurs ayant un sens pour le shell. `paste` peut parcourir plusieurs caractères, mais un seul suffit souvent à deux colonnes.

:::single-choice{#paste-colon-delimiter} Quelle commande joint les lignes correspondantes de `names.txt` et `roles.txt` avec un deux-points ?

::option[`paste -d ':' names.txt roles.txt`]{#paste-colon-files .correct explanation="`-d` remplace la tabulation par le deux-points fourni."}
::option[`paste -s ':' names.txt roles.txt`]{#paste-serial-colon-operand explanation="`-s` sélectionne le mode série et `:` serait traité comme un chemin."}
::option[`paste names.txt ':' roles.txt`]{#paste-colon-file-operand explanation="Sans `-d`, chaque opérande est un fichier d'entrée."}
:::

## Sérialiser les lignes d'un fichier

`-s` joint les lignes de chaque fichier en une seule ligne :

```bash
$ printf 'The\nquick\nbrown\nfox\n' > words.txt
$ paste -s words.txt
The	quick	brown	fox
```

Combinez `-s` et `-d` pour choisir le séparateur :

```bash
$ paste -s -d ' ' words.txt
The quick brown fox
```

Avec plusieurs fichiers, chacun devient sa propre ligne de sortie.

:::single-choice{#paste-serialize-with-spaces} Quelle commande joint toutes les lignes de `words.txt` en une ligne séparée par des espaces ?

::option[`paste -d ' ' words.txt`]{#paste-parallel-one-file explanation="En mode parallèle, un seul fichier conserve une ligne de sortie par ligne d'entrée."}
::option[`paste -s words.txt roles.txt`]{#paste-two-serial-files explanation="Cette forme sérialise deux fichiers séparément avec des tabulations."}
::option[`paste -s -d ' ' words.txt`]{#paste-serial-spaces .correct explanation="`-s` sérialise les lignes et `-d ' '` insère des espaces."}
:::

## Gérer des entrées de longueurs différentes

`paste` continue jusqu'à la fin du fichier le plus long ; les valeurs absentes deviennent des champs vides :

```bash
$ printf 'A\nB\nC\n' > letters.txt
$ printf '1\n2\n' > numbers.txt
$ paste -d ':' letters.txt numbers.txt
A:1
B:2
C:
```

:::single-choice{#paste-unequal-files} Que se passe-t-il lorsqu'un fichier se termine avant un autre en mode parallèle ?

::option[`paste` utilise des champs vides jusqu'à la fin de l'entrée la plus longue.]{#paste-empty-fields .correct explanation="Le mode parallèle continue jusqu'à épuisement de tous les fichiers."}
::option[`paste` s'arrête et abandonne les lignes restantes.]{#paste-stop-shortest explanation="La commande continue jusqu'à l'entrée la plus longue."}
::option[`paste` reprend le fichier court depuis le début.]{#paste-repeat-shorter explanation="Une entrée épuisée fournit des champs vides ; elle ne boucle pas."}
:::

## Lire une entrée depuis stdin

Utilisez `-` comme opérande :

```bash
$ printf 'admin\nviewer\n' | paste -d ':' names.txt -
alice:admin
bob:viewer
```

:::single-choice{#paste-stdin-operand} Dans `producer | paste names.txt -`, que signifie l'opérande `-` ?

::option[Écrire le résultat sur stderr.]{#paste-write-stderr explanation="Le tiret désigne ici une source d'entrée."}
::option[Supprimer les délimiteurs.]{#paste-remove-delimiter explanation="Le délimiteur se contrôle avec `-d`."}
::option[Lire cette colonne depuis stdin.]{#paste-read-stdin .correct explanation="Le tiret demande à `paste` d'utiliser son entrée standard à cette position."}
:::

Pour vous exercer :

1. **[Traitement de texte simple](https://labex.io/fr/labs/linux-simple-text-processing-18004)** - Manipulez du texte avec `tr`, `col`, `join` et `paste`.

## Résumé

Vous savez désormais combiner des entrées ligne par ligne avec un alignement prévisible.

1. Fusionner les lignes correspondantes de plusieurs fichiers.
2. Remplacer la tabulation avec `-d`.
3. Sérialiser les lignes d'un fichier avec `-s`.
4. Interpréter les champs vides des entrées plus courtes.
5. Utiliser `-` pour une entrée provenant de stdin.
