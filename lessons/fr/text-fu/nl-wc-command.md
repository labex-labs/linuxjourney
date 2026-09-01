---
lesson_id: "nl-wc-command"
course_id: "text-fu"
lang: "fr"
order_index: 15
title: "wc et nl"
description: "Apprenez à compter lignes, mots, octets ou caractères avec wc et à numéroter les lignes avec nl."
meta_title: "wc et nl - Text-Fu"
meta_description: "Utilisez les commandes Linux wc et nl pour compter le texte et ajouter des numéros de ligne."
meta_keywords: "commande wc, commande nl, compter mots Linux, numéros de ligne, traitement texte"
---

`wc` compte les propriétés d'un flux de texte, tandis que `nl` écrit l'entrée avec des numéros de ligne. Les deux lisent des fichiers ou stdin et écrivent sur stdout.

## Lire la sortie par défaut de wc

Sans option de comptage, `wc` affiche les nombres de retours à la ligne, de mots et d'octets, puis le nom du fichier :

```bash
$ printf 'red blue\ngreen\n' > colors.txt
$ wc colors.txt
 2  3 15 colors.txt
```

De gauche à droite : 2 retours à la ligne, 3 mots séparés par des blancs et 15 octets. Une dernière ligne sans retour final n'est pas comptée par `wc -l`, qui compte les caractères de nouvelle ligne.

:::single-choice{#wc-default-columns} Dans la sortie par défaut de `wc file.txt`, que représentent les trois premiers nombres ?

::option[Lignes, mots et octets, dans cet ordre.]{#wc-lines-words-bytes .correct explanation="`wc` indique par défaut retours à la ligne, mots et octets avant le nom."}
::option[Octets, mots et lignes, dans cet ordre.]{#wc-bytes-words-lines explanation="Ce sont les mêmes mesures dans le mauvais ordre ; les lignes viennent d'abord."}
::option[Fichiers, caractères et paragraphes.]{#wc-files-characters-paragraphs explanation="Les colonnes par défaut ne comptent ni fichiers ni paragraphes ; la troisième mesure les octets."}
:::

## Demander un seul comptage

- `-l` : retours à la ligne.
- `-w` : mots.
- `-c` : octets.
- `-m` : caractères selon la locale.

```bash
$ wc -w colors.txt
3 colors.txt
```

Avec stdin et sans opérande de fichier, le libellé est normalement omis :

```bash
$ printf 'one two\n' | wc -w
2
```

Octets et caractères coïncident en ASCII mais peuvent différer en UTF-8. Avec stdin sans nom de fichier, `wc` omet normalement le libellé.

:::single-choice{#wc-word-count-only} Quelle commande ne donne que le nombre de mots de `essay.txt` ?

::option[`wc -l essay.txt`]{#wc-lines-essay explanation="`-l` compte les retours à la ligne."}
::option[`wc -w essay.txt`]{#wc-words-essay .correct explanation="`-w` sélectionne le comptage des mots."}
::option[`wc -c essay.txt`]{#wc-bytes-essay explanation="`-c` compte les octets."}
:::

:::single-choice{#wc-characters-not-bytes} Quelle option demande à `wc` de compter les caractères plutôt que les octets selon la locale ?

::option[`-m`]{#wc-character-option .correct explanation="`-m` compte les caractères, qui peuvent occuper plusieurs octets."}
::option[`-c`]{#wc-byte-option explanation="`-c` compte les octets."}
::option[`-w`]{#wc-word-option explanation="`-w` compte les mots."}
:::

Avec plusieurs fichiers, `wc` affiche un résultat par fichier et une ligne `total`. GNU `wc -L` indique la largeur d'affichage maximale d'une ligne.

## Numéroter les lignes non vides avec nl

Si `notes.txt` contient une deuxième ligne vide :

```text
alpha

beta
```

```bash
$ nl notes.txt
	 1	alpha

	 2	beta
```

Par défaut, `nl` numérote les lignes non vides du corps. Il préserve la ligne vide sans la numéroter et ne modifie pas le fichier.

:::single-choice{#nl-default-blank-lines} Comment `nl notes.txt` traite-t-il par défaut les lignes vides du corps ?

::option[Il les omet entièrement.]{#nl-omit-blank explanation="La ligne vide reste dans la sortie, mais sans numéro."}
::option[Il les préserve sans numéro.]{#nl-preserve-unnumbered .correct explanation="Le style par défaut numérote les lignes non vides et reproduit les vides sans numéro."}
::option[Il les numérote comme les autres.]{#nl-number-blank-default explanation="La numérotation de toutes les lignes exige un style tel que `-ba`."}
:::

## Numéroter chaque ligne

Le style de corps `a` choisi avec `-ba` numérote tout :

```bash
$ nl -ba notes.txt
	 1	alpha
	 2
	 3	beta
```

`-w 3` fixe la largeur du champ numérique et `-s ': '` change le séparateur.

:::single-choice{#nl-number-all-lines} Quelle commande numérote toutes les lignes du corps de `notes.txt`, y compris les vides ?

::option[`nl -w 3 notes.txt`]{#nl-width-three explanation="Cette option ne change que la largeur du nombre."}
::option[`nl -ba notes.txt`]{#nl-body-all .correct explanation="`-b` choisit le style du corps et `a` numérote toutes les lignes."}
::option[`wc -l notes.txt`]{#wc-lines-notes explanation="Cette commande compte les retours à la ligne sans reproduire le texte numéroté."}
:::

Pour vous exercer :

1. **[Commande Linux wc : compter du texte](https://labex.io/fr/labs/linux-linux-wc-command-text-counting-219200)** - Comptez mots, lignes et caractères.
2. **[Commande Linux nl : numéroter les lignes](https://labex.io/fr/labs/linux-linux-nl-command-line-numbering-210988)** - Ajoutez des numéros aux lignes.
3. **[Comptage et tri de mots](https://labex.io/fr/labs/linux-word-count-and-sorting-388125)** - Combinez comptage et tri pour analyser du texte.

## Résumé

Vous savez mesurer un flux et ajouter des numéros visibles sans modifier la source.

1. Interpréter les colonnes lignes, mots et octets de `wc`.
2. Choisir un comptage avec `-l`, `-w`, `-c` ou `-m`.
3. Distinguer octets et caractères.
4. Numéroter les lignes non vides avec `nl`.
5. Numéroter aussi les lignes vides avec `nl -ba`.
