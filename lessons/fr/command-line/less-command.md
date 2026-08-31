---
lesson_id: "less-command"
course_id: "command-line"
lang: "fr"
order_index: 8
title: "less"
description: "Apprenez à parcourir, rechercher et suivre interactivement de longs fichiers texte avec less."
meta_title: "less - Ligne de commande"
meta_description: "Apprenez la commande Linux less avec des exemples pour visualiser de gros fichiers, défiler, rechercher, aller à une ligne, suivre les logs et quitter less."
meta_keywords: "commande less, linux less, voir gros fichier linux, rechercher dans less, quitter less, less -N, less +F, visualiseur texte linux"
---

Lorsqu'un fichier texte est trop long pour tenir sur un écran, `less` permet de le lire sans envoyer tout son contenu défiler dans le terminal. Son nom a inspiré l'ancienne plaisanterie Unix « less is more », car `more` est une autre visionneuse paginée.

## Ouvrir un fichier

Démarrez la visionneuse en lui fournissant un nom de fichier :

```bash
$ less /home/pete/Documents/text1
```

Tant que `less` est actif, les touches contrôlent la visionneuse au lieu de lancer les commandes ordinaires du shell. Vous revenez au shell lorsque vous quittez la visionneuse.

:::single-choice{#open-long-file}
Quelle commande ouvre `/var/log/syslog` dans une visionneuse interactive ?

::option[`less /var/log/syslog`]{#page-log .correct explanation="`less` ouvre le fichier dans une visionneuse qui permet de le parcourir, d'y rechercher du texte, puis de revenir au shell."}
::option[`cat /var/log/syslog`]{#print-log explanation="`cat` envoie tout le fichier sur la sortie standard d'un coup ; elle ne fournit pas de commandes de pagination interactives."}
::option[`file /var/log/syslog`]{#classify-log explanation="`file` indique un type de contenu probable ; elle n'ouvre pas le journal pour une lecture interactive."}
:::

## Naviguer dans less

Lorsque la visionneuse est ouverte :

- utilisez `Haut`, `Bas`, `Page précédente` et `Page suivante` pour avancer par lignes ou écrans ;
- appuyez sur `g` pour aller au début ;
- appuyez sur `G` pour aller à la fin ;
- appuyez sur `u` pour remonter d'un demi-écran ou sur `d` pour descendre d'un demi-écran ;
- appuyez sur `h` pour ouvrir l'aide intégrée.

:::single-choice{#jump-to-file-end}
Quelle touche va directement à la fin d'un fichier dans `less` ?

::option[`g`]{#lowercase-g explanation="Le `g` minuscule va au début du fichier. La majuscule produit le déplacement opposé."}
::option[`G`]{#uppercase-g .correct explanation="Le `G` majuscule va à la fin de l'entrée. La commande est sensible à la casse."}
::option[`h`]{#help-key explanation="La touche `h` ouvre l'aide de la visionneuse ; elle ne va pas à la fin du fichier."}
:::

## Rechercher dans less

Tapez `/`, puis un motif et Entrée pour rechercher vers l'avant. Commencez par `?` pour rechercher vers l'arrière.

- `/search_term` : rechercher `search_term` vers l'avant ;
- `?search_term` : rechercher `search_term` vers l'arrière ;
- `n` : répéter la recherche dans le même sens ;
- `N` : répéter la recherche dans le sens opposé.

:::single-choice{#repeat-search-direction}
Après une recherche vers l'avant de `error`, quelle touche répète la recherche dans le même sens ?

::option[`n`]{#same-search .correct explanation="Le `n` minuscule répète la dernière recherche dans son sens initial, ici vers l'avant."}
::option[`N`]{#opposite-search explanation="Le `N` majuscule répète la recherche dans le sens opposé ; après une recherche vers l'avant, il parcourt les correspondances vers l'arrière."}
::option[`g`]{#search-to-start explanation="La touche `g` va au début de l'entrée ; elle ne répète pas une recherche."}
:::

## Quitter less

Appuyez sur `q` pour quitter `less` et revenir à l'invite du shell.

:::single-choice{#quit-less}
Quelle touche quitte `less` et revient au shell ?

::option[`q`]{#less-quit .correct explanation="La commande `q` ferme la visionneuse et rétablit l'invite du shell."}
::option[`h`]{#less-help explanation="La touche `h` ouvre l'aide dans `less` ; elle ne revient pas directement au shell."}
::option[`G`]{#less-end explanation="Le `G` majuscule va à la fin de l'entrée, mais laisse la visionneuse ouverte."}
:::

## Démarrer less avec des options

Des options et commandes initiales peuvent modifier le démarrage :

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N` : afficher les numéros de ligne ;
- `+G` : ouvrir à la fin du fichier ;
- `+F` : suivre le nouveau contenu à mesure qu'il est ajouté, comme `tail -f`.

Pendant le suivi avec `+F`, appuyez sur `Ctrl+C` pour arrêter le suivi et revenir à la navigation normale, puis sur `q` pour quitter. Utilisez `-i` pour ignorer la casse sauf si le motif contient une majuscule, ou `-I` pour l'ignorer quelle que soit la casse du motif.

Une commande peut aussi envoyer sa sortie à `less` par un tube :

```bash
$ dmesg | less
```

:::single-choice{#follow-growing-log}
Quelle commande ouvre `/var/log/syslog` et suit le nouveau contenu à son arrivée ?

::option[`less +F /var/log/syslog`]{#follow-log .correct explanation="La commande initiale `+F` active le mode de suivi ; `less` affiche donc le contenu ajouté au journal."}
::option[`less +G /var/log/syslog`]{#open-at-log-end explanation="La commande initiale `+G` ouvre le fichier à la fin, mais ne suit pas le contenu ajouté ensuite."}
::option[`less -N /var/log/syslog`]{#number-log-lines explanation="L'option `-N` affiche les numéros de ligne ; elle n'active pas le suivi continu."}
:::

Pour vous exercer à parcourir et rechercher du texte système, essayez ces laboratoires :

1. **[Commande Linux less : pagination de fichiers](https://labex.io/fr/labs/linux-linux-less-command-file-paging-214301)** — Apprenez à lire et parcourir efficacement des fichiers avec `less`, notamment avec la recherche, les numéros de ligne et les motifs.
2. **[Afficher les journaux et fichiers de configuration Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** — Utilisez `cat`, `more` et `less` pour consulter et parcourir des journaux et configurations.

## Résumé

Vous savez maintenant utiliser `less` pour examiner de longs fichiers sans inonder le terminal.

1. Ouvrir un fichier ou la sortie d'une commande transmise par un tube.
2. Atteindre différentes parties de l'entrée.
3. Rechercher vers l'avant ou l'arrière et répéter une recherche.
4. Afficher les numéros de ligne ou suivre un contenu croissant.
5. Quitter sans risque et revenir au shell.
