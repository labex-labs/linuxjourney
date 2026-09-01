---
lesson_id: "pipe-tee-redirect"
course_id: "text-fu"
lang: "fr"
order_index: 4
title: "pipe et tee"
description: "Découvrez comment les pipelines relient des commandes et comment tee sauvegarde un flux tout en le transmettant."
meta_title: "pipe et tee - Text-Fu"
meta_description: "Apprenez à enchaîner des commandes avec un tube Linux et à copier leur sortie vers l'écran et un fichier avec tee."
meta_keywords: "pipe Linux, tee, pipeline, stdout, stdin, redirection, ligne de commande"
---

Les pipelines relient de petites commandes afin que les données circulent sans fichier intermédiaire. `tee` peut copier une partie de ce flux dans un fichier tout en continuant à le transmettre.

## Relier des commandes avec |

Si une liste est trop longue :

```bash
$ ls -la /etc
```

Placez `|` entre les commandes pour relier stdout de celle de gauche à stdin de celle de droite :

```bash
$ ls -la /etc | less
```

Le shell démarre les commandes et établit la connexion. Elles peuvent fonctionner en parallèle : `less` commence à lire avant que `ls` ait tout produit.

:::single-choice{#pipe-stream-connection} Dans `ls -la /etc | less`, quels flux `|` relie-t-il par défaut ?

::option[Stdin de `ls` à stdout de `less`.]{#pipe-reversed-streams explanation="Cela inverse producteur et consommateur ; les données vont de la sortie gauche vers l'entrée droite."}
::option[Stderr de `ls` aux deux flux de `less`.]{#pipe-stderr-both explanation="Un tube ordinaire ne relie pas stderr de la commande gauche."}
::option[Stdout de `ls` à stdin de `less`.]{#pipe-stdout-stdin .correct explanation="Un pipeline relie le descripteur 1 de gauche au descripteur 0 de droite."}
:::

## Garder stderr séparé

Un simple `|` ne transporte que stdout. Stderr conserve sa destination, souvent le terminal :

```bash
$ find /etc -name "*.conf" | less
```

Les chemins trouvés traversent le tube, tandis que les erreurs d'autorisation restent au terminal. Redirigez-les séparément si nécessaire :

```bash
$ find /etc -name "*.conf" 2> find-errors.log | less
```

:::single-choice{#pipe-left-stderr} Dans `find /etc -name "*.conf" | less`, où va normalement stderr de `find` sans autre redirection ?

::option[Dans `less`, avec stdout.]{#pipe-errors-to-less explanation="Le tube ordinaire ne relie que stdout."}
::option[Dans un fichier `stderr`.]{#pipe-errors-to-file explanation="Aucune redirection ne crée ce fichier."}
::option[Vers sa destination existante, généralement le terminal.]{#pipe-errors-terminal .correct explanation="Le descripteur 2 n'étant pas modifié, les diagnostics restent au terminal."}
:::

## Copier un flux avec tee

`tee` lit stdin, en écrit une copie dans chaque fichier nommé et reproduit les mêmes données sur stdout :

```bash
$ ls | tee listing.txt
```

`listing.txt` reçoit la liste et stdout de `tee` reste relié au terminal. Par défaut, `tee` crée ou tronque le fichier.

:::single-choice{#tee-display-and-save} Quelle commande affiche la sortie de `generate-report` et remplace aussi `report.txt` par cette sortie ?

::option[`generate-report > report.txt`]{#redirect-report-only explanation="Cette redirection écrit le fichier mais ne garde pas de copie pour le terminal."}
::option[`generate-report | tee report.txt`]{#tee-report .correct explanation="`tee` copie stdin dans `report.txt` et sur sa sortie standard."}
::option[`tee generate-report | report.txt`]{#tee-operands-reversed explanation="Cette forme traite `generate-report` comme destination et `report.txt` comme commande."}
:::

Utilisez `-a` pour ajouter au lieu de remplacer :

```bash
$ date | tee -a activity.log
```

:::single-choice{#tee-append-log} Quelle commande affiche la date et l'ajoute à `activity.log` ?

::option[`date | tee -a activity.log`]{#tee-append-activity .correct explanation="`-a` fait ajouter `tee` au fichier tout en copiant l'entrée sur stdout."}
::option[`date | tee activity.log`]{#tee-replace-activity explanation="Sans `-a`, `tee` remplace le fichier."}
::option[`date > activity.log`]{#redirect-replace-activity explanation="Cette forme remplace le fichier et n'affiche aucune copie."}
:::

## Sauvegarder un résultat intermédiaire

Placez `tee` au milieu d'un pipeline :

```bash
$ ls -la /etc | tee etc-listing.txt | grep "conf"
```

Ce pipeline produit la liste complète, l'enregistre dans `etc-listing.txt`, puis transmet le même flux à `grep`, qui n'affiche que les lignes contenant `conf`. Le fichier reçoit donc les données avant filtrage ; placez `tee` après `grep` pour ne conserver que les correspondances.

:::single-choice{#tee-before-filter-result} Que contient `all.txt` après `produce | tee all.txt | grep error` ?

::option[Seulement les lignes retenues par `grep`.]{#tee-filtered-only explanation="`tee` précède `grep` et écrit donc l'entrée non filtrée."}
::option[Seulement stderr de `produce`.]{#tee-producer-stderr explanation="Le tube transporte stdout, pas stderr."}
::option[Toute la sortie standard produite avant filtrage.]{#tee-complete-intermediate .correct explanation="`tee` sauvegarde tout ce qu'il reçoit avant de le transmettre à `grep`."}
:::

Pour vous exercer :

1. **[Rediriger les entrées et sorties sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Manipulez les flux avec les opérateurs et `tee`.
2. **[Contrôle de séquence et pipeline](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Utilisez les pipelines et les outils de traitement de texte.
3. **[Redirection des flux de données](https://labex.io/fr/labs/linux-data-stream-redirection-17995)** - Combinez les flux standard et `/dev/null`.

## Résumé

Vous savez désormais relier des commandes et préserver certains points d'un flux.

1. Relier stdout d'une commande à stdin d'une autre.
2. Rediriger stderr séparément.
3. Copier une entrée vers un fichier et stdout avec `tee`.
4. Ajouter avec `tee -a`.
5. Positionner `tee` avant ou après un filtre selon le besoin.
