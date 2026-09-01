---
lesson_id: "join-split-command"
course_id: "text-fu"
lang: "fr"
order_index: 11
title: "join et split"
description: "Apprenez à joindre deux fichiers texte triés par une clé et à découper un fichier en fragments nommés."
meta_title: "join et split - Text-Fu"
meta_description: "Utilisez les commandes Linux join et split pour réunir des enregistrements par clé ou découper de gros fichiers."
meta_keywords: "join Linux, split Linux, joindre fichiers, découper fichier, traitement texte"
---

`join` et `split` résolvent deux problèmes différents. `join` combine des enregistrements liés provenant de deux entrées triées ; `split` divise une entrée en une série de fichiers.

## Joindre deux fichiers par leur premier champ

Par défaut, `join` compare le premier champ séparé par des blancs dans exactement deux fichiers. Avec ces fichiers déjà triés :

`people.txt` :

```text
1 John
2 Jane
3 Mary
```

`surnames.txt` :

```text
1 Doe
2 Doe
3 Sue
```

```bash
$ join people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

La sortie contient une fois la clé commune, puis les autres champs des deux fichiers. `join` traite deux fichiers à la fois, pas une jointure relationnelle à trois opérandes.

:::single-choice{#join-default-key} Sans option de champ, quels enregistrements `join first.txt second.txt` combine-t-il ?

::option[Les lignes dont les premiers champs séparés par des blancs sont égaux.]{#join-first-fields .correct explanation="Par défaut, `join` compare le champ 1 des deux entrées triées."}
::option[Les lignes portant le même numéro physique.]{#join-line-numbers explanation="La correspondance repose sur la valeur des clés, pas sur la position."}
::option[Chaque ligne du premier fichier avec toutes celles du second.]{#join-all-pairs explanation="`join` émet les clés correspondantes, pas un produit cartésien."}
:::

## Trier les clés de jointure

Chaque entrée doit être ordonnée selon sa clé avec des règles compatibles :

```bash
$ LC_ALL=C sort -k 1,1 people-raw.txt > people.txt
$ LC_ALL=C sort -k 1,1 surnames-raw.txt > surnames.txt
$ LC_ALL=C join people.txt surnames.txt
```

La même locale garantit une collation cohérente. Ne redirigez jamais `sort` vers son propre fichier d'entrée, que le shell tronquerait avant la lecture.

:::single-choice{#join-sort-requirement} Quelle préparation `join` exige-t-il normalement ?

::option[Les fichiers doivent avoir exactement le même nombre de lignes.]{#join-equal-line-count explanation="Leurs longueurs peuvent différer ; les clés déterminent les résultats."}
::option[Leurs noms doivent être voisins dans l'ordre alphabétique.]{#join-filename-order explanation="Le contenu doit être trié ; les noms sont sans importance."}
::option[Les deux fichiers doivent être triés selon leurs clés avec un ordre compatible.]{#join-sorted-keys .correct explanation="`join` parcourt des clés ordonnées ; leur tri doit correspondre à sa comparaison."}
:::

## Choisir d'autres champs de jointure

`-1 FIELD` choisit la clé du premier fichier et `-2 FIELD` celle du second. Pour une première entrée comme :

```text
John 1
Jane 2
Mary 3
```

et une seconde comme :

```text
1 Doe
2 Doe
3 Sue
```

après les tris appropriés :

```bash
$ join -1 2 -2 1 people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-t CHARACTER` définit un délimiteur non blanc. `-a 1` ou `-a 2` peut inclure les lignes sans partenaire ; par défaut, seules les clés appariées apparaissent.

:::single-choice{#join-different-fields} Quelles options joignent le champ 2 du premier fichier au champ 1 du second ?

::option[`-1 1 -2 2`]{#join-fields-reversed explanation="Cette forme choisit la correspondance inverse."}
::option[`-1 2 -2 1`]{#join-fields-two-one .correct explanation="`-1 2` choisit le champ 2 du premier et `-2 1` le champ 1 du second."}
::option[`-f 2 -d 1`]{#join-cut-style-options explanation="Ces options ressemblent à celles d'autres outils et ne sélectionnent pas les clés de `join`."}
:::

## Découper par nombre de lignes

`split` écrit des portions consécutives d'une entrée. Ce n'est pas l'inverse d'une jointure par clé.

```bash
$ split large.txt
```

Choisissez le nombre de lignes et le préfixe de sortie avec :

```bash
$ split -l 500 large.txt part-
```

Par défaut, GNU `split` écrit jusqu'à 1000 lignes dans `xaa`, `xab`, etc. La seconde forme crée `part-aa`, `part-ab`, etc., avec au plus 500 lignes.

:::single-choice{#split-lines-with-prefix} Quelle commande découpe `large.txt` en fragments d'au plus 500 lignes préfixés par `part-` ?

::option[`split -b 500 large.txt part-`]{#split-five-hundred-bytes explanation="`-b` compte des octets, pas des lignes."}
::option[`split -l 500 large.txt part-`]{#split-five-hundred-lines .correct explanation="`-l 500` fixe le nombre maximal de lignes et le dernier opérande fournit le préfixe."}
::option[`join -l 500 large.txt part-`]{#join-split-lines explanation="`join` combine des enregistrements et ne découpe pas un fichier."}
:::

## Découper par taille

`-b SIZE` choisit une taille en octets. Pour GNU, `K`, `M` et `G` représentent ici des puissances de 1024 :

```bash
$ split -b 10M archive.bin chunk-
```

Les fragments font 10 Mio, sauf éventuellement le dernier. `split` ne crée ni manifeste ni métadonnées ; conservez l'ordre des suffixes pour une reconstruction par concaténation.

:::single-choice{#split-ten-mebibytes} Quelle commande découpe `archive.bin` en fragments de 10 Mio préfixés par `chunk-` ?

::option[`split -l 10M archive.bin chunk-`]{#split-lines-ten-m explanation="`-l` attend un nombre de lignes, pas une taille binaire."}
::option[`join -b 10M archive.bin chunk-`]{#join-bytes explanation="`join` ne découpe pas une entrée binaire."}
::option[`split -b 10M archive.bin chunk-`]{#split-ten-mib .correct explanation="`-b 10M` fixe 10×1024×1024 octets et `chunk-` est le préfixe."}
:::

Pour vous exercer :

1. **[Commande Linux join : joindre des fichiers](https://labex.io/fr/labs/linux-linux-join-command-file-joining-219193)** - Fusionnez les lignes de deux fichiers triés par un champ commun.
2. **[Traiter des données d'employés](https://labex.io/fr/labs/linux-processing-employees-data-388132)** - Combinez plusieurs sources avec `join` et `awk`.

## Résumé

Vous savez combiner des enregistrements triés ou diviser une entrée en fragments ordonnés.

1. Joindre exactement deux fichiers par clés égales.
2. Trier les entrées de façon cohérente.
3. Choisir les clés avec `-1` et `-2`.
4. Découper par lignes avec `-l`.
5. Découper par octets avec `-b` et un préfixe clair.
