---
lesson_id: "cut-command"
course_id: "text-fu"
lang: "fr"
order_index: 6
title: "cut"
description: "Apprenez à sélectionner des positions de caractères ou des champs délimités sur chaque ligne avec cut."
meta_title: "cut - Text-Fu"
meta_description: "Utilisez la commande Linux cut pour extraire des caractères ou des champs avec des délimiteurs personnalisés."
meta_keywords: "commande cut, traitement de texte Linux, extraire texte, champs, délimiteur"
---

`cut` sélectionne des positions de caractères ou des champs sur chaque ligne. Il convient surtout aux textes de structure régulière dont les délimiteurs et positions sont connus.

```bash
$ printf 'name\trole\nalice\tadmin\nbob\tviewer\n' > team.tsv
```

Ici, `printf` transforme `\t` en tabulation et `\n` en retour à la ligne.

## Sélectionner des positions de caractères

Utilisez `-c LIST` ; les positions commencent à 1 :

```bash
$ cut -c 1 team.tsv
n
a
b
```

La liste peut contenir des positions individuelles et des plages :

```bash
$ cut -c 1-4 team.tsv
name
alic
bob
$ cut -c 1,3 team.tsv
nm
ai
bb
```

Espaces, tabulations et ponctuation occupent aussi des positions. Chaque ligne est traitée séparément.

:::single-choice{#cut-first-character}
Quelle commande affiche le premier caractère de chaque ligne de `names.txt` ?

::option[`cut -c 1 names.txt`]{#cut-character-one .correct explanation="`-c` sélectionne les positions de caractères et 1 désigne la première."}
::option[`cut -f 1 names.txt`]{#cut-field-one explanation="`-f` sélectionne le premier champ séparé par une tabulation."}
::option[`cut -d 1 names.txt`]{#cut-delimiter-one explanation="`-d` définit un délimiteur et doit accompagner une sélection de champs."}
:::

## Sélectionner des champs séparés par des tabulations

`-f LIST` sélectionne les champs ; le délimiteur par défaut est la tabulation :

```bash
$ cut -f 2 team.tsv
role
admin
viewer
```

Une liste peut prendre des formes comme `1`, `1,3`, `2-4`, `-3` ou `2-`.

:::single-choice{#cut-second-tab-field}
Quelle commande affiche le deuxième champ de chaque ligne de `team.tsv` ?

::option[`cut -c 2 team.tsv`]{#cut-second-character explanation="Cette forme sélectionne le deuxième caractère."}
::option[`cut -f 2 team.tsv`]{#cut-second-field .correct explanation="Sans `-d`, le mode champ emploie une tabulation et `-f 2` choisit le deuxième champ."}
::option[`cut -d 2 team.tsv`]{#cut-delimiter-two explanation="Cette forme tente d'utiliser `2` comme délimiteur sans choisir de champ."}
:::

## Choisir un délimiteur personnalisé

Employez `-d CHARACTER` avec `-f` :

```bash
$ printf 'alice;admin\nbob;viewer\n' > team.txt
$ cut -d ';' -f 1 team.txt
alice
bob
```

Le délimiteur est ici un caractère. Citez `;`, car il possède un sens de contrôle dans le shell.

:::single-choice{#cut-semicolon-role-field}
Quelle commande affiche le deuxième champ délimité par un point-virgule dans `team.txt` ?

::option[`cut -d ':' -f 2 team.txt`]{#cut-colon-second explanation="Cette forme cherche des deux-points, pas des points-virgules."}
::option[`cut -d ';' -f 2 team.txt`]{#cut-semicolon-second .correct explanation="Le point-virgule cité devient le délimiteur et `-f 2` choisit le second champ."}
::option[`cut -c 2 -f ';' team.txt`]{#cut-mixed-options explanation="Cette forme mélange les modes caractère et champ avec des arguments invalides."}
:::

## Gérer les lignes sans délimiteur

En mode champ, `cut` reproduit normalement une ligne sans délimiteur. `-s` la supprime :

```bash
$ printf 'alice;admin\nheader\nbob;viewer\n' | cut -s -d ';' -f 2
admin
viewer
```

Cela ne suffit pas à analyser un CSV général, qui peut contenir délimiteurs cités, retours à la ligne et échappements. Utilisez alors un outil compatible CSV.

:::single-choice{#cut-suppress-undelimited}
Que fait `-s` avec `cut -d ':' -f 1` ?

::option[Il trie les champs sélectionnés.]{#cut-s-sort explanation="`cut` ne trie pas et `-s` ne concerne pas l'ordre."}
::option[Il regroupe les délimiteurs consécutifs.]{#cut-s-squeeze explanation="Les champs vides restent des positions significatives."}
::option[Il supprime les lignes dépourvues du délimiteur choisi.]{#cut-s-suppress .correct explanation="En mode champ, `-s` empêche la reproduction des lignes non délimitées."}
:::

## Lire depuis stdin

Sans fichier, ou avec `-` comme opérande, `cut` lit stdin :

```bash
$ printf 'red:1\nblue:2\n' | cut -d ':' -f 1
red
blue
```

:::single-choice{#cut-pipeline-input}
Dans `generate-data | cut -d ':' -f 1`, où `cut` lit-il son entrée ?

::option[Dans stdout de `generate-data`, par le tube.]{#cut-pipe-stdin .correct explanation="Le tube relie stdout du producteur à stdin de `cut`."}
::option[Dans un fichier nommé `generate-data`.]{#cut-pipe-file explanation="`generate-data` est exécutée comme commande de gauche."}
::option[Dans le flux stderr de `cut`.]{#cut-pipe-stderr explanation="Un tube ordinaire alimente stdin depuis stdout de la commande précédente."}
:::

Pour vous exercer :

1. **[Commande Linux cut : découpage de texte](https://labex.io/fr/labs/linux-linux-cut-command-text-cutting-219187)** - Extrayez des colonnes et champs de fichiers texte.
2. **[Contrôle de séquence et pipeline](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Combinez `cut`, `grep`, `wc`, `sort` et `uniq`.

## Résumé

Vous savez maintenant sélectionner des positions prévisibles avec `cut`.

1. Sélectionner des caractères ou des plages.
2. Extraire les champs tabulés avec `-f`.
3. Fournir un délimiteur avec `-d`.
4. Supprimer les lignes non délimitées si nécessaire.
5. Lire du texte structuré depuis un fichier ou stdin.
