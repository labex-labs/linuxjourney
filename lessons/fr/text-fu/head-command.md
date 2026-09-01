---
lesson_id: "head-command"
course_id: "text-fu"
lang: "fr"
order_index: 8
title: "head"
description: "Apprenez à afficher un nombre contrôlé de lignes ou d'octets au début d'une entrée."
meta_title: "head - Text-Fu"
meta_description: "Utilisez la commande Linux head et l'option head -n pour consulter le début d'un fichier."
meta_keywords: "commande head, Linux head, début fichier, head -n, ligne de commande"
---

`head` affiche le début d'un fichier ou d'un flux. Il sert à vérifier des en-têtes, prévisualiser des données structurées ou échantillonner une sortie.

## Afficher les dix premières lignes

Sans option de comptage, `head` affiche les 10 premières lignes de chaque fichier :

```bash
$ head events.log
```

Le fichier n'est pas modifié. S'il comporte moins de 10 lignes, elles sont toutes affichées.

:::single-choice{#head-default-lines} Que produit `head events.log` par défaut ?

::option[Les 10 dernières lignes, ou toutes si le fichier est plus court.]{#head-last-ten explanation="La fin d'une entrée relève de `tail` ; `head` part du début."}
::option[Les 10 premières lignes, ou toutes si le fichier est plus court.]{#head-first-ten .correct explanation="Sans option de comptage, `head` sélectionne au plus les dix premières lignes."}
::option[Seulement la première ligne.]{#head-first-one explanation="Une seule ligne exige `-n 1` ; la valeur par défaut est dix."}
:::

## Choisir un nombre de lignes

Utilisez `-n NUMBER` :

```bash
$ head -n 15 events.log
```

GNU `head` accepte aussi `-15`, mais `-n 15` rend le sens plus explicite.

:::single-choice{#head-five-lines} Quelle commande affiche les cinq premières lignes de `report.txt` ?

::option[`head -c 5 report.txt`]{#head-five-bytes explanation="`-c` compte les octets et peut s'arrêter au milieu d'une ligne."}
::option[`head -n 5 report.txt`]{#head-report-five .correct explanation="`-n` sélectionne un nombre de lignes, ici cinq."}
::option[`tail -n 5 report.txt`]{#tail-five-lines explanation="Cette commande affiche les cinq dernières lignes."}
:::

## Choisir un nombre d'octets

Utilisez `-c NUMBER` pour compter des octets :

```bash
$ head -c 20 archive.bin
```

La sortie peut finir au milieu d'une ligne ou d'un caractère multioctet. Préférez les lignes pour le texte ordinaire.

:::single-choice{#head-first-bytes} Quelle commande écrit les 100 premiers octets de `payload.bin` sur stdout ?

::option[`head -c 100 payload.bin`]{#head-hundred-bytes .correct explanation="`-c` sélectionne un nombre d'octets, ici les cent premiers disponibles."}
::option[`head -n 100 payload.bin`]{#head-hundred-lines explanation="`-n` compte les lignes, pas les octets."}
::option[`cut -c 100 payload.bin`]{#cut-hundredth-character explanation="Cette forme sélectionne la position 100 sur chaque ligne."}
:::

## Lire stdin et plusieurs fichiers

Sans fichier, `head` lit stdin :

```bash
$ generate-report | head -n 5
```

Avec plusieurs fichiers, il ajoute normalement un en-tête :

```bash
$ head -n 2 january.txt february.txt
==> january.txt <==
...

==> february.txt <==
...
```

`-q` supprime ces en-têtes et `-v` en affiche un même pour un seul fichier.

:::single-choice{#head-pipeline-preview} Dans `generate-report | head -n 5`, que lit `head` ?

::option[Stdout de `generate-report` par stdin.]{#head-pipe-input .correct explanation="Le tube relie stdout du producteur à stdin de `head`, qui en choisit cinq lignes."}
::option[Les cinq premiers noms du répertoire courant.]{#head-directory-names explanation="Aucune commande ne liste le répertoire."}
::option[Cinq octets d'un fichier `generate-report`.]{#head-producer-file explanation="La partie gauche est une commande et `-n` compte les lignes."}
:::

:::single-choice{#head-suppress-filename-headers} Quelle option supprime les en-têtes de noms lorsque `head` lit plusieurs fichiers ?

::option[`-v`]{#head-verbose explanation="`-v` force les en-têtes, même avec un fichier."}
::option[`-c`]{#head-byte-option explanation="`-c` change l'unité en octets."}
::option[`-q`]{#head-quiet .correct explanation="L'option quiet `-q` empêche l'affichage des libellés de fichiers."}
:::

Pour vous exercer :

1. **[Commande Linux head : afficher le début d'un fichier](https://labex.io/fr/labs/linux-linux-head-command-file-beginning-display-214302)** - Affichez les premières lignes et modifiez leur nombre.
2. **[Consulter les journaux et fichiers de configuration](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Naviguez efficacement dans des fichiers texte.
3. **[Détection rapide des menaces](https://labex.io/fr/labs/linux-rapid-threat-detection-387930)** - Analysez rapidement des entrées de journaux.

## Résumé

Vous savez prévisualiser le début de fichiers et de sorties de commandes.

1. Utiliser les dix premières lignes par défaut.
2. Choisir un nombre de lignes avec `-n`.
3. Choisir des octets avec `-c`.
4. Lire stdin dans un pipeline.
5. Contrôler les en-têtes pour plusieurs fichiers.
