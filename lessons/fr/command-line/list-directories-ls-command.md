---
lesson_id: "list-directories-ls-command"
course_id: "command-line"
lang: "fr"
order_index: 4
title: "ls (Lister les Répertoires)"
description: "Apprenez à utiliser les options de ls pour examiner les fichiers, les éléments cachés, les détails, les tailles et l'ordre de tri."
meta_title: "ls (Lister les Répertoires) - Ligne de Commande"
meta_description: "Apprenez la commande Linux ls avec des exemples pour lister les fichiers, les fichiers cachés, le format long, les tailles lisibles, le tri et la combinaison d'options."
meta_keywords: "commande ls, linux ls, lister fichiers linux, lister répertoires, ls -a, ls -l, ls -lh, ls -r, fichiers cachés"
---

Maintenant que nous savons parcourir le système de fichiers, comment découvrir ce qui nous est accessible ? La commande `ls` liste les fichiers et répertoires afin d'examiner l'emplacement actuel ou un autre chemin.

## Utilisation élémentaire de ls

Par défaut, `ls` liste les répertoires et fichiers du répertoire actuel. Vous pouvez aussi lui fournir un chemin pour afficher le contenu d'un autre répertoire.

```bash
$ ls
$ ls /home/pete
```

Vous pouvez également désigner un fichier précis :

```bash
$ ls /etc/hosts
/etc/hosts
```

:::single-choice{#list-another-directory}
Quelle commande liste le contenu de `/home/pete` sans s'y déplacer ?

::option[`ls /home/pete`]{#ls-target-path .correct explanation="Fournir un chemin de répertoire à `ls` affiche son contenu. Le shell reste dans son répertoire de travail actuel."}
::option[`cd /home/pete`]{#cd-target-path explanation="`cd` change le répertoire de travail du shell ; elle ne réalise pas à elle seule la liste demandée."}
::option[`pwd /home/pete`]{#pwd-target-path explanation="`pwd` indique le répertoire de travail actuel et n'accepte pas de destination à lister. Utilisez `ls` avec le chemin."}
:::

## Afficher les fichiers cachés

Tous les fichiers d'un répertoire ne sont pas visibles par défaut. Sous Linux, les noms qui commencent par un point (`.`) sont cachés. Affichez-les avec l'option `-a`, pour « all ».

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

Les fichiers pointés sont masqués par défaut et contiennent souvent une configuration, comme `.bashrc`.

:::single-choice{#show-hidden-files}
Quelle commande inclut les fichiers cachés dans la liste ?

::option[`ls -l`]{#long-format explanation="L'option `-l` ajoute des colonnes détaillées, mais n'inclut pas à elle seule les noms cachés."}
::option[`ls -r`]{#reverse-order explanation="L'option `-r` inverse l'ordre de tri ; elle ne change pas l'inclusion des fichiers cachés."}
::option[`ls -a`]{#all-files .correct explanation="L'option `-a` signifie « all » ; `ls` inclut donc les noms qui commencent par un point."}
:::

## Obtenir des informations détaillées

L'option essentielle `-l` sélectionne le format long. Il affiche les permissions, le nombre de liens, le propriétaire, le groupe, la taille, l'heure de modification et le nom.

```bash
$ ls -l
```

Voici un exemple de sortie :

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

Pour des tailles plus faciles à lire, ajoutez `-h` :

```bash
$ ls -lh
```

:::single-choice{#show-readable-file-details}
Quelle commande affiche les détails au format long avec des tailles lisibles ?

::option[`ls -la`]{#long-all explanation="Cette commande combine le format long et les fichiers cachés ; elle ne demande pas d'unités de taille lisibles."}
::option[`ls -lh`]{#long-human-readable .correct explanation="`-l` sélectionne le format long et `-h` rend les tailles plus lisibles. Ces options se combinent dans une commande."}
::option[`ls -ltr`]{#long-time-reverse explanation="Cette commande combine format long, tri par date de modification et ordre inverse, sans l'option de taille `-h`."}
:::

## Inverser l'ordre de tri

L'option `-r` liste les fichiers et répertoires dans l'ordre inverse.

```bash
$ ls -r
```

Vous pouvez trier par date de modification avec `-t`, puis inverser ce tri avec `-r` :

```bash
$ ls -lt
$ ls -ltr
```

:::single-choice{#show-newest-files-last}
Quelle commande trie par date de modification, puis place les éléments les plus récents en dernier ?

::option[`ls -ltr`]{#time-reversed .correct explanation="`-t` trie par date de modification, tandis que `-r` inverse cet ordre. Ensemble, ils placent les éléments anciens avant les récents."}
::option[`ls -lt`]{#time-default explanation="Cette commande trie par date de modification en conservant l'ordre récent d'abord ; elle ne place pas les plus récents en dernier."}
::option[`ls -lr`]{#reverse-name-order explanation="Cette commande utilise le format long et inverse le tri par nom. Sans `-t`, la date de modification ne détermine pas l'ordre."}
:::

## Combiner les options de commande

Les commandes possèdent des options, aussi appelées indicateurs, qui ajoutent des fonctions. Comme avec `-a` et `-l`, vous pouvez les réunir dans `ls -la`. Leur ordre n'a souvent pas d'importance : `ls -al` fonctionne de la même façon.

```bash
$ ls -la
```

Combinaisons utiles :

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

## Options courantes de ls

- `-a` : afficher tous les fichiers, y compris les fichiers cachés ;
- `-l` : employer le format long ;
- `-h` : afficher des tailles lisibles avec `-l` ;
- `-r` : inverser l'ordre de tri ;
- `-t` : trier par date de modification ;
- `-S` : trier par taille de fichier ;
- `-d` : lister le répertoire lui-même plutôt que son contenu.

:::single-choice{#list-directory-entry-itself}
Quelle commande liste l'entrée du répertoire `projects/` au lieu de son contenu ?

::option[`ls -d projects/`]{#directory-entry .correct explanation="L'option `-d` demande à `ls` d'afficher l'entrée du répertoire elle-même plutôt que d'en ouvrir le contenu."}
::option[`ls projects/`]{#directory-contents explanation="Sans `-d`, fournir le chemin d'un répertoire à `ls` affiche les éléments qu'il contient."}
::option[`cd projects/`]{#change-to-directory explanation="`cd` change le répertoire de travail ; elle ne liste pas l'entrée demandée."}
:::

Certains systèmes affichent les sorties de `ls` dans des couleurs qui dépendent du type de fichier. Ce comportement provient souvent d'un alias ou d'un réglage d'environnement ; les couleurs peuvent donc varier.

Pour vous exercer, essayez le laboratoire **[Commande Linux ls : lister le contenu](https://labex.io/fr/labs/linux-linux-ls-command-content-listing-219205)**. Vous y utiliserez `ls` pour analyser le contenu de fichiers et répertoires, afficher les éléments cachés, obtenir des tailles lisibles et modifier le tri.

## Résumé

Vous savez maintenant utiliser `ls` pour examiner le contenu des répertoires et contrôler son affichage.

1. Lister le répertoire actuel ou un autre chemin.
2. Inclure les fichiers cachés.
3. Afficher des informations détaillées avec des tailles lisibles.
4. Trier les éléments par date de modification dans l'ordre inverse.
5. Lister l'entrée d'un répertoire sans afficher son contenu.
