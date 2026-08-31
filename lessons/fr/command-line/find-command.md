---
lesson_id: "find-command"
course_id: "command-line"
lang: "fr"
order_index: 14
title: "find"
description: "Apprenez à rechercher dans des arborescences par nom, type, taille et date, puis à agir sur des résultats vérifiés."
meta_title: "find - Ligne de commande"
meta_description: "Apprenez la commande Linux find avec des exemples pour rechercher par nom, type, taille, date de modification et exécuter des actions sur les fichiers correspondants."
meta_keywords: "commande linux find, commande find, trouver fichiers linux, find par nom, find par type, find par taille, find mtime, find exec"
---

La commande `find` parcourt une arborescence et teste chaque entrée selon des critères comme son nom, son type, sa taille ou sa date de modification.

## Choisir où rechercher

La syntaxe élémentaire est :

```bash
find [PATH] [EXPRESSION]
```

Le chemin choisit le point de départ et l'expression sélectionne les entrées situées dessous, ou agit sur elles.

Cette commande recherche dans `/home` et ses descendants les entrées nommées `puppies.jpg` :

```bash
$ find /home -name puppies.jpg
```

La récursivité est le comportement par défaut. Utilisez `.` comme point de départ pour rechercher dans l'arborescence du répertoire actuel.

:::single-choice{#search-current-tree}
Quelle commande recherche dans le répertoire actuel et ses descendants les entrées nommées `notes.txt` ?

::option[`find . -name notes.txt`]{#find-current-notes .correct explanation="Le point choisit le répertoire actuel comme départ, et `-name` teste le nom de base de chaque entrée."}
::option[`find / -name notes.txt`]{#find-root-notes explanation="Le chemin de départ `/` lance la recherche depuis la racine du système de fichiers, une portée beaucoup plus large."}
::option[`find notes.txt .`]{#find-operands-reversed explanation="`find` attend les chemins de départ avant l'expression ; cet ordre n'exprime pas la recherche demandée."}
:::

## Rechercher par nom et par type

Le test `-name` accepte un nom de base exact ou un motif de type shell. Placez les jokers entre guillemets afin que le shell actuel les transmette inchangés à `find` :

```bash
$ find . -name "*.txt"
```

Sans guillemets, le shell peut développer `*.txt` dans le répertoire actuel avant le démarrage de `find`. Utilisez `-iname` à la place de `-name` pour ignorer la casse.

Ajoutez `-type d` pour choisir les répertoires ou `-type f` pour les fichiers ordinaires :

```bash
$ find /home -type d -name MyFolder
```

Les deux tests doivent être vrais : l'entrée doit être un répertoire dont le nom de base est `MyFolder`.

:::single-choice{#find-text-regular-files}
Quelle commande trouve sous le répertoire actuel les fichiers ordinaires dont le nom se termine par `.txt` ?

::option[`find . -type f -name "*.txt"`]{#text-files .correct explanation="`-type f` sélectionne les fichiers ordinaires, tandis que `find` évalue le motif `-name` cité pour chaque entrée."}
::option[`find . -type d -name "*.txt"`]{#text-directories explanation="Le motif est correctement cité, mais `-type d` sélectionne des répertoires plutôt que des fichiers ordinaires."}
::option[`find . -type f -name *.txt`]{#unquoted-text-files explanation="Le joker non cité peut être développé par le shell actuel avant l'exécution de `find`, ce qui change l'expression voulue."}
:::

## Rechercher par taille et date de modification

Avec `-size`, `+` signifie supérieur à l'unité indiquée et `-` inférieur :

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

La majuscule `M` représente des unités de 1 048 576 octets, et le `k` minuscule des unités de 1 024 octets. `find` arrondit la taille à l'unité choisie avant la comparaison ; le comportement aux limites dépend donc de ces unités.

`-mtime` teste le nombre de périodes complètes de 24 heures écoulées depuis la modification :

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` correspond à une valeur inférieure à 7, et `-mtime +30` à une valeur supérieure à 30. Ces tests utilisent des périodes complètes de 24 heures, pas les limites de minuit du calendrier.

:::single-choice{#find-recent-regular-files}
Quelle commande trouve sous `.` les fichiers ordinaires dont l'âge de modification est inférieur à sept périodes complètes de 24 heures ?

::option[`find . -type f -mtime -7`]{#recent-files .correct explanation="`-type f` sélectionne les fichiers ordinaires et `-mtime -7` les âges inférieurs à sept périodes complètes de 24 heures."}
::option[`find . -type f -mtime +7`]{#older-than-seven explanation="Le signe plus sélectionne les âges supérieurs à sept unités ; il recherche donc des fichiers plus anciens."}
::option[`find . -type d -mtime -7`]{#recent-directories explanation="Le test temporel est récent, mais `-type d` limite les résultats aux répertoires."}
:::

## Afficher les résultats et agir dessus

Sans action, GNU `find` affiche les chemins correspondants. Vous pouvez écrire explicitement `-print` pour rendre l'action claire :

```bash
$ find . -name "*.log" -print
```

`-exec` exécute une autre commande pour les correspondances :

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

Dans la forme `\;`, `{}` est remplacé par un chemin correspondant à chaque invocation. Le point-virgule termine l'action `-exec` et est échappé afin que le shell le transmette à `find`.

Avant une action destructive comme `-delete` ou une commande `-exec` qui modifie des fichiers, exécutez les mêmes tests avec `-print` et inspectez tous les résultats. Un chemin de départ plus étroit et `-maxdepth N` peuvent aussi limiter la recherche.

:::single-choice{#verify-before-delete}
Vous préparez une commande `find` susceptible de supprimer ensuite d'anciens fichiers `.log`. Que devez-vous faire d'abord ?

::option[Ajouter immédiatement `-delete` et vérifier quels fichiers disparaissent.]{#delete-first explanation="La suppression n'est pas une prévisualisation sûre et ne possède pas d'annulation intégrée. Vérifiez tout l'ensemble avant de l'ajouter."}
::option[Exécuter les mêmes tests avec `-print` et inspecter chaque résultat.]{#print-first .correct explanation="Une liste en lecture seule vérifie le point de départ et les tests avant l'introduction d'une action destructive."}
::option[Commencer à `/` pour ne manquer aucun journal.]{#root-first explanation="Un départ à `/` élargit la portée et peut inclure des chemins sans rapport ou protégés. Choisissez le point de départ pertinent le plus étroit."}
:::

:::single-choice{#run-ls-for-each-match}
Dans `find . -name "*.log" -exec ls -l {} \;`, que représente `{}` ?

::option[Le chemin actuellement correspondant, fourni à `ls -l`.]{#match-placeholder .correct explanation="Dans cette forme de `-exec`, `find` remplace `{}` par la correspondance actuelle avant d'invoquer `ls -l`."}
::option[Le répertoire depuis lequel `find` a été lancé.]{#starting-placeholder explanation="Le répertoire de départ est le point situé au début de la commande ; les accolades jouent un autre rôle dans `-exec`."}
::option[Le point-virgule qui termine l'expression `-exec`.]{#terminator-placeholder explanation="Le point-virgule échappé termine l'action `-exec` ; les accolades sont l'espace réservé au chemin."}
:::

Les messages de permission refusée signifient généralement que le compte actuel ne peut pas parcourir une partie de l'arborescence. Préférez un départ plus étroit et pertinent ; n'ajoutez des privilèges qu'après avoir compris et voulu l'accès élargi.

Pour vous exercer, essayez **[Commande Linux find : rechercher des fichiers](https://labex.io/fr/labs/linux-linux-find-command-file-searching-219191)** et **[Découvrir les ressources système essentielles](https://labex.io/fr/labs/linux-discover-critical-system-resources-388032)**.

## Résumé

Vous savez maintenant construire des expressions `find` ciblées et vérifier leurs résultats avant d'agir.

1. Choisir le point de départ utile le plus étroit.
2. Citer les motifs de noms et les combiner avec des tests de type.
3. Filtrer par taille ou périodes complètes de 24 heures.
4. Limiter la profondeur de récursion si nécessaire.
5. Afficher et inspecter les correspondances avant toute action destructive.
