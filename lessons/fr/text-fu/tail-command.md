---
lesson_id: "tail-command"
course_id: "text-fu"
lang: "fr"
order_index: 9
title: "tail"
description: "Apprenez à consulter la fin d'une entrée et à suivre un fichier lorsque du contenu y est ajouté."
meta_title: "tail - Text-Fu"
meta_description: "Utilisez la commande Linux tail pour voir la fin d'un fichier et suivre un journal en temps réel avec tail -f."
meta_keywords: "commande tail, Linux tail, tail -f, journaux, surveillance fichiers"
---

`tail` affiche la fin d'un fichier ou d'un flux. Il peut aussi rester actif et montrer les données ajoutées, ce qui est utile pour observer des journaux.

## Afficher les dix dernières lignes

Sans option de comptage, `tail` affiche les 10 dernières lignes :

```bash
$ tail application.log
```

Si le fichier est plus court, toutes ses lignes sont affichées sans le modifier.

:::single-choice{#tail-default-lines} Que montre `tail application.log` par défaut ?

::option[Au plus les 10 premières lignes.]{#tail-first-ten explanation="Le début est sélectionné par `head` ; `tail` part de la fin."}
::option[Toutes les lignes ajoutées après son lancement.]{#tail-follow-only explanation="Le suivi continu exige `-f` ; un simple `tail` affiche un instantané puis se termine."}
::option[Au plus les 10 dernières lignes.]{#tail-last-ten .correct explanation="Sans option, `tail` choisit les dix dernières lignes disponibles."}
:::

## Choisir un nombre de lignes ou d'octets

```bash
$ tail -n 20 application.log
```

Utilisez `-c NUMBER` lorsque vous avez besoin des derniers octets :

```bash
$ tail -c 100 payload.bin
```

`-n` choisit les dernières lignes, `-c` les derniers octets. Le mode octet peut commencer au milieu d'une ligne ou d'un caractère encodé.

:::single-choice{#tail-twenty-lines} Quelle commande affiche les 20 dernières lignes de `application.log` ?

::option[`tail -n 20 application.log`]{#tail-twenty-end .correct explanation="`-n` choisit un nombre de lignes, que `tail` prend à la fin."}
::option[`head -n 20 application.log`]{#head-twenty-start explanation="Cette commande choisit les lignes du début."}
::option[`tail -c 20 application.log`]{#tail-twenty-bytes explanation="`-c` choisit 20 octets, pas 20 lignes."}
:::

## Commencer à une ligne donnée

Avec un préfixe `+`, `tail -n +N` commence à la ligne N :

```bash
$ tail -n +5 report.txt
```

Cette commande saute quatre lignes et commence à la cinquième, ce qui permet notamment de retirer un nombre connu d'en-têtes.

:::single-choice{#tail-start-line-five} Quelle commande affiche `report.txt` à partir de la ligne 5 ?

::option[`tail -n +5 report.txt`]{#tail-from-five .correct explanation="`+5` demande à `tail` de commencer à la ligne 5 et de poursuivre jusqu'à la fin."}
::option[`tail -n 5 report.txt`]{#tail-final-five explanation="Sans plus, cette forme choisit les cinq dernières lignes."}
::option[`head -n +5 report.txt`]{#head-plus-five explanation="Ce n'est pas la forme de départ à une ligne de `tail`."}
:::

## Suivre les données ajoutées

Avec `-f`, `tail` affiche la fin actuelle et reste actif :

```bash
$ tail -f application.log
```

Appuyez sur `Ctrl+C` pour l'interrompre. Le suivi montre seulement le nouveau contenu ; il ne garantit pas la santé de l'application ni que tous les événements utilisent ce fichier.

:::single-choice{#tail-follow-file} Quelle commande montre la fin actuelle de `application.log` puis attend les ajouts ?

::option[`tail -f application.log`]{#tail-follow-app .correct explanation="`-f` maintient `tail` actif et affiche les données ajoutées."}
::option[`tail -n 0 application.log`]{#tail-zero-lines explanation="Sans option de suivi, elle n'affiche rien puis se termine."}
::option[`less application.log`]{#less-log explanation="Cette forme ouvre un paginateur, pas le mode de suivi de `tail`."}
:::

## Suivre un journal renouvelé par son nom

La rotation peut renommer l'ancien fichier et en recréer un au chemin initial. GNU `tail -F` suit le nom et réessaie, ce qui lui permet de rouvrir le fichier :

```bash
$ tail -F application.log
```

Employez `-f` pour suivre le fichier actuellement ouvert et `-F` lorsqu'un journal nommé doit tourner. D'autres implémentations peuvent différer.

:::single-choice{#tail-follow-rotated-name} Sous GNU/Linux, quelle option convient au suivi de `application.log` lors d'une rotation par renommage et recréation ?

::option[`-n`]{#tail-rotation-lines explanation="`-n` modifie le nombre de lignes, pas le suivi d'un chemin remplacé."}
::option[`-c`]{#tail-rotation-bytes explanation="`-c` choisit les octets et ne gère pas la rotation."}
::option[`-F`]{#tail-follow-name .correct explanation="GNU `-F` suit le nom et réessaie afin de rouvrir un journal remplacé."}
:::

Sans fichier, `tail` lit stdin. Avec plusieurs fichiers, il ajoute par défaut des en-têtes, comme `head`.

Pour vous exercer :

1. **[Commande Linux tail : afficher la fin d'un fichier](https://labex.io/fr/labs/linux-linux-tail-command-file-end-display-214303)** - Consultez et suivez la fin de fichiers avec `-f`.
2. **[Consulter les journaux et fichiers de configuration](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Naviguez efficacement dans les journaux.
3. **[Détection rapide des menaces](https://labex.io/fr/labs/linux-rapid-threat-detection-387930)** - Analysez rapidement des entrées récentes.

## Résumé

Vous savez inspecter la fin d'un fichier et observer son nouveau contenu.

1. Afficher les dix dernières lignes par défaut.
2. Choisir un nombre de lignes ou d'octets.
3. Commencer à une ligne avec `-n +N`.
4. Suivre les ajouts avec `-f` et arrêter avec `Ctrl+C`.
5. Utiliser GNU `-F` pour un journal soumis à rotation.
