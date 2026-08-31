---
lesson_id: "uniq-unique-command"
course_id: "text-fu"
lang: "fr"
order_index: 14
title: "uniq (unique)"
description: "Apprenez à regrouper, compter ou filtrer les groupes adjacents de lignes identiques avec uniq."
meta_title: "uniq (unique) - Text-Fu"
meta_description: "Utilisez uniq sous Linux pour filtrer les doublons adjacents avec -c, -u et -d, notamment après sort."
meta_keywords: "commande uniq, Linux uniq, doublons, sort uniq, traitement texte"
---

`uniq` compare chaque ligne à la précédente. Il peut regrouper, compter ou sélectionner des séries adjacentes identiques, mais ne cherche pas les doublons séparés dans tout le fichier.

## Regrouper les lignes dupliquées adjacentes

Si `reading.txt` contient :

```plaintext
book
book
paper
paper
article
article
magazine
```

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Une ligne représentative est produite par groupe adjacent. Le fichier d'entrée reste inchangé.

:::single-choice{#uniq-collapse-adjacent}
Que fait `uniq reading.txt` par défaut ?

::option[Il trie tout le fichier puis supprime chaque valeur répétée.]{#uniq-auto-sort explanation="`uniq` préserve l'ordre et ne trie pas ; les copies séparées restent dans des groupes distincts."}
::option[Il affiche une ligne par groupe adjacent de lignes égales.]{#uniq-one-per-group .correct explanation="Par défaut, `uniq` réduit chaque série consécutive identique à une ligne."}
::option[Il supprime directement les doublons de `reading.txt`.]{#uniq-edit-file explanation="Le résultat va sur stdout ; l'entrée n'est pas modifiée."}
:::

## Compter les groupes adjacents

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

Ces nombres sont les longueurs des séries, pas des totaux globaux, sauf si les lignes égales ont été regroupées au préalable.

:::single-choice{#uniq-count-groups}
Que représente le nombre produit par `uniq -c` ?

::option[Le nombre de caractères de chaque ligne.]{#uniq-character-count explanation="Le comptage des caractères relève plutôt de `wc`."}
::option[Le nombre de lignes égales consécutives dans chaque groupe.]{#uniq-consecutive-count .correct explanation="`-c` préfixe chaque groupe adjacent réduit par le nombre de lignes qu'il contenait."}
::option[Le total de lignes correspondantes partout dans le fichier.]{#uniq-global-count explanation="Les copies séparées forment des groupes différents tant que les données ne sont pas triées."}
:::

## Sélectionner les groupes uniques ou répétés

```bash
$ uniq -u reading.txt
magazine
```

Utilisez `-d` pour afficher un représentant de chaque groupe répété :

```bash
$ uniq -d reading.txt
book
paper
article
```

`-u` ne garde que les groupes d'une ligne. `-d` émet une ligne par groupe répété ; GNU `uniq -D` émet toutes les lignes de ces groupes.

:::single-choice{#uniq-only-singletons}
Quelle commande affiche seulement les groupes adjacents présents exactement une fois ?

::option[`uniq -c reading.txt`]{#uniq-count-reading explanation="Cette forme affiche tous les groupes avec leur nombre."}
::option[`uniq -d reading.txt`]{#uniq-duplicate-reading explanation="`-d` choisit les groupes répétés."}
::option[`uniq -u reading.txt`]{#uniq-single-reading .correct explanation="`-u` sélectionne les groupes dont la longueur est exactement un."}
:::

:::single-choice{#uniq-one-per-duplicate-group}
Quelle commande affiche une ligne par groupe adjacent présent plusieurs fois ?

::option[`uniq -d reading.txt`]{#uniq-duplicate-groups .correct explanation="`-d` choisit les groupes répétés et en émet un représentant."}
::option[`uniq -D reading.txt`]{#uniq-all-duplicate-lines explanation="GNU `-D` émet toutes les lignes des groupes répétés."}
::option[`uniq -u reading.txt`]{#uniq-unique-groups explanation="`-u` choisit les groupes unitaires."}
:::

## Regrouper les doublons séparés

Si les valeurs égales ne sont pas voisines, elles forment des groupes distincts :

```plaintext
book
paper
book
paper
article
magazine
article
```

Sur ce fichier, aucune ligne n'est regroupée puisque les voisines diffèrent :

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

Lorsque l'ordre peut changer, triez d'abord :

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

Employez une locale et une politique de comparaison cohérentes. `sort -u reading.txt` peut aussi trier et ne garder qu'une ligne par clé égale.

:::single-choice{#uniq-separated-duplicates}
Des lignes égales sont dispersées dans `reading.txt` et l'ordre peut changer. Quel pipeline produit une copie triée de chaque ligne distincte ?

::option[`sort reading.txt | uniq`]{#sort-then-uniq .correct explanation="Le tri rend les lignes égales adjacentes, puis `uniq` réduit chaque groupe."}
::option[`uniq reading.txt | sort`]{#uniq-before-sort explanation="`uniq` agit avant le regroupement et peut laisser des doublons dans la sortie triée."}
::option[`uniq -c reading.txt | head`]{#uniq-count-head explanation="Cette forme compte les groupes actuels puis limite la sortie."}
:::

Sans fichier, `uniq` lit stdin. GNU propose aussi `-i` pour ignorer la casse, et `-f`, `-s`, `-w` pour limiter la région comparée.

Pour vous exercer :

1. **[Commande Linux uniq : filtrer les doublons](https://labex.io/fr/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Identifiez et analysez les doublons avec `sort` et `uniq`.
2. **[Commande Linux sort : trier du texte](https://labex.io/fr/labs/linux-linux-sort-command-text-sorting-219196)** - Organisez les lignes avant `uniq`.
3. **[Comptage et tri de mots](https://labex.io/fr/labs/linux-word-count-and-sorting-388125)** - Analysez et triez des données textuelles.

## Résumé

Vous savez analyser les groupes adjacents de lignes égales avec `uniq`.

1. Réduire chaque groupe adjacent à une ligne.
2. Compter les occurrences consécutives avec `-c`.
3. Choisir les groupes unitaires avec `-u`.
4. Choisir les groupes répétés avec `-d` ou GNU `-D`.
5. Trier d'abord pour regrouper les doublons séparés.
