---
lesson_id: "sort-command"
course_id: "text-fu"
lang: "fr"
order_index: 12
title: "sort"
description: "Apprenez à ordonner des lignes selon leur valeur lexicale, numérique ou celle d'un champ choisi."
meta_title: "sort - Text-Fu"
meta_description: "Utilisez la commande Linux sort pour trier des fichiers texte, inverser l'ordre et comparer des nombres."
meta_keywords: "commande sort Linux, sort -r, sort -n, tri texte, ligne de commande"
---

`sort` lit des lignes complètes, les ordonne selon les règles choisies et écrit le résultat sur stdout. Il ne modifie pas l'entrée sans opération de sortie explicite.

## Trier des lignes complètes

Avec `animals.txt` :

```text
dog
cow
cat
elephant
bird
```

```bash
$ sort animals.txt
bird
cat
cow
dog
elephant
```

L'ordre dépend de la locale, qui influe sur la casse, les accents et la ponctuation. Pour une collation reproductible par octets :

```bash
$ LC_ALL=C sort animals.txt
```

:::single-choice{#sort-lines-ascending} Que fait `sort animals.txt` sans option de clé ou numérique ?

::option[Il ordonne les lignes complètes selon la locale courante.]{#sort-locale-lines .correct explanation="Par défaut, `sort` compare les lignes entières selon les règles de collation actives."}
::option[Il trie les mots dans chaque ligne sans déplacer les lignes.]{#sort-words-within-lines explanation="Chaque ligne constitue un enregistrement ; ses mots ne sont pas réarrangés."}
::option[Il réécrit automatiquement `animals.txt`.]{#sort-auto-rewrite explanation="Le résultat va sur stdout et l'entrée reste inchangée."}
:::

## Inverser le résultat

```bash
$ sort -r animals.txt
elephant
dog
cow
cat
bird
```

:::single-choice{#sort-reverse-order} Quelle commande trie `animals.txt` dans l'ordre inverse ?

::option[`sort -n animals.txt`]{#sort-numeric-animals explanation="`-n` demande une comparaison numérique."}
::option[`sort -u animals.txt`]{#sort-unique-animals explanation="`-u` supprime les clés dupliquées."}
::option[`sort -r animals.txt`]{#sort-reverse-animals .correct explanation="`-r` inverse l'ordre défini par les autres règles."}
:::

## Comparer des nombres

L'ordre lexical place normalement `10` avant `2`. Utilisez `-n` :

```bash
$ printf '10\n2\n30\n' | sort -n
2
10
30
```

`sort -nr scores.txt` combine comparaison numérique et ordre décroissant.

:::single-choice{#sort-numbers-descending} Quelle commande trie les lignes numériques de `scores.txt` de la plus grande à la plus petite ?

::option[`sort -n scores.txt`]{#sort-numeric-ascending explanation="Le tri numérique est croissant sans `-r`."}
::option[`sort -nr scores.txt`]{#sort-numeric-reverse .correct explanation="`-n` compare les nombres et `-r` inverse le résultat."}
::option[`sort -r scores.txt`]{#sort-lexical-reverse explanation="Cette forme inverse la collation textuelle sans demander de comparaison numérique."}
:::

## Trier selon un champ

`-k START[,END]` choisit une clé. Les champs sont séparés par des blancs, sauf délimiteur défini avec `-t` :

```bash
$ printf 'alice:30\nbob:8\ncarol:20\n' | sort -t ':' -k 2,2n
bob:8
carol:20
alice:30
```

`-t ':'` définit les champs, `-k 2,2` borne la clé au deuxième et `n` la compare numériquement. Sans `,2`, une clé commençant au champ 2 continue normalement jusqu'à la fin.

:::single-choice{#sort-second-colon-field} Quelle commande trie `users.txt` numériquement selon son seul deuxième champ séparé par `:` ?

::option[`sort -n -k 1,1 users.txt`]{#sort-first-blank-field explanation="Cette forme utilise les blancs et le premier champ."}
::option[`cut -d ':' -f 2 users.txt`]{#cut-second-user-field explanation="`cut` extrait le champ sans trier les enregistrements."}
::option[`sort -t ':' -k 2,2n users.txt`]{#sort-colon-field-two .correct explanation="Le deux-points délimite les champs, `2,2` borne la clé et `n` la compare numériquement."}
:::

## Supprimer les doublons et enregistrer la sortie

`-u` ne produit qu'une ligne pour chaque clé de comparaison égale :

```bash
$ sort -u names.txt
```

Cette forme trie et supprime les doublons selon les règles choisies. Pour supprimer seulement des doublons adjacents d'une entrée déjà triée, utilisez `uniq`.

```bash
$ sort names.txt > names-sorted.txt
```

N'exécutez pas `sort names.txt > names.txt` : le shell tronquerait l'entrée. GNU `sort` peut gérer le même chemin avec :

```bash
$ sort -o names.txt names.txt
```

Conservez une sauvegarde ou vérifiez un résultat séparé si les données comptent.

:::single-choice{#sort-safe-same-file} Sous GNU/Linux, quelle commande demande à `sort` de réécrire sûrement `names.txt` sans troncature préalable du shell ?

::option[`sort -o names.txt names.txt`]{#sort-output-same-file .correct explanation="GNU `sort` gère la sortie `-o` après la lecture nécessaire ; le shell ne pré-tronque pas l'entrée."}
::option[`sort names.txt > names.txt`]{#sort-redirection-same-file explanation="Le shell tronque le fichier avant le lancement de `sort`."}
::option[`sort -u names.txt`]{#sort-unique-stdout explanation="Cette forme écrit sur stdout et laisse le fichier inchangé."}
:::

Pour vous exercer :

1. **[Commande Linux sort : trier du texte](https://labex.io/fr/labs/linux-linux-sort-command-text-sorting-219196)** - Triez des lignes dans différents ordres.
2. **[Comptage et tri de mots](https://labex.io/fr/labs/linux-word-count-and-sorting-388125)** - Analysez des fréquences et ordonnez les résultats.

## Résumé

Vous savez choisir les règles de comparaison et la destination d'un texte trié.

1. Trier des lignes sous une locale explicite si nécessaire.
2. Inverser avec `-r`.
3. Comparer des nombres avec `-n`.
4. Borner une clé avec `-t` et `-k`.
5. Supprimer les doublons ou enregistrer sans tronquer l'entrée.
