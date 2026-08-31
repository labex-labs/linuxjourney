---
lesson_id: "man-command"
course_id: "command-line"
lang: "fr"
order_index: 16
title: "man"
description: "Apprenez à ouvrir, parcourir et rechercher les pages de manuel installées, ainsi qu'à choisir leur section."
meta_title: "man - Ligne de commande"
meta_description: "Apprenez la commande Linux man avec des exemples pour lire les pages de manuel, rechercher dans les pages man, comprendre les sections et trouver les options des commandes."
meta_keywords: "commande man, pages man linux, manuel de commande, man ls, sections man, recherche page man, aide ligne de commande"
---

De nombreuses commandes, interfaces, configurations et outils d'administration Linux possèdent une documentation de référence installée appelée pages de manuel, ou pages man. La commande `man` recherche et affiche ces pages.

## Ouvrir une page de manuel

Fournissez un nom de sujet à `man`. Par exemple, ouvrez la page de `ls` avec :

```bash
$ man ls
```

Les pages de manuel contiennent généralement un synopsis, une description, des options, des fichiers associés et des renvois, même si leurs sections exactes varient.

:::single-choice{#open-ls-manual}
Quelle commande ouvre la page de manuel installée de `ls` ?

::option[`help ls`]{#help-ls explanation="`help` documente les commandes intégrées à Bash et n'ouvre normalement pas le manuel du programme externe `ls`."}
::option[`man ls`]{#manual-ls-page .correct explanation="`man` recherche le sujet `ls` dans la base des manuels et affiche la page correspondante."}
::option[`ls --help`]{#ls-usage explanation="Cette commande demande à `ls` son propre résumé d'utilisation ; elle n'ouvre pas la page de manuel installée."}
:::

## Parcourir et rechercher une page

Sur de nombreux systèmes, `man` affiche les pages dans une visionneuse comme `less`. Lorsqu'une page est ouverte, utilisez les flèches ou les touches de pagination, ainsi que :

- `/motif` suivi d'Entrée pour rechercher vers l'avant ;
- `n` pour répéter dans le même sens ;
- `N` pour répéter dans le sens opposé ;
- `q` pour quitter.

La visionneuse peut varier selon le système ou l'environnement ; ces touches ne sont donc pas garanties partout. Elles s'appliquent à la configuration courante avec `less`.

:::single-choice{#search-man-page}
Dans une page de manuel ouverte avec `less`, qu'est-ce qui lance une recherche vers l'avant de `--recursive` ?

::option[Saisir `?--recursive` puis Entrée.]{#backward-man-search explanation="Le point d'interrogation lance une recherche vers l'arrière, dans le sens opposé à celui demandé."}
::option[Saisir `/--recursive` puis Entrée.]{#forward-man-search .correct explanation="La barre oblique lance une recherche vers l'avant dans `less`, et Entrée soumet le motif."}
::option[Saisir `n--recursive` puis Entrée.]{#repeat-man-search explanation="La touche `n` répète une recherche existante ; elle n'introduit pas ainsi un nouveau motif."}
:::

:::single-choice{#leave-man-page}
Dans une page de manuel ouverte avec la visionneuse habituelle, quelle touche revient au shell ?

::option[`G`]{#man-page-end explanation="Le `G` majuscule va à la fin de la page dans `less`, sans fermer la visionneuse."}
::option[`n`]{#next-man-match explanation="La touche `n` répète la recherche la plus récente et laisse la page ouverte."}
::option[`q`]{#quit-man .correct explanation="La touche `q` quitte la visionneuse habituelle et rend le contrôle au shell."}
:::

## Choisir une section du manuel

Le manuel est organisé en sections numérotées. Les sections courantes comprennent :

- `1` : commandes utilisateur ;
- `2` : appels système ;
- `3` : fonctions de bibliothèque ;
- `5` : formats de fichiers ;
- `8` : commandes d'administration système.

Un même sujet peut apparaître dans plusieurs sections. Placez la section avant le sujet pour en choisir une :

```bash
$ man 5 passwd
$ man 1 passwd
```

La première commande ouvre la page du format de fichier `passwd` en section 5 ; la seconde, celle de la commande utilisateur en section 1. Une référence comme `passwd(5)` suit la même notation `sujet(section)`.

:::single-choice{#open-passwd-file-format}
Quelle commande ouvre la page de section 5 qui documente le format du fichier `passwd` ?

::option[`man passwd 5`]{#section-after-topic explanation="Dans cette forme, la section se place avant le sujet ; cet ordre ne demande pas `passwd(5)`."}
::option[`man 5 passwd`]{#passwd-format-page .correct explanation="Placer la section `5` avant `passwd` sélectionne précisément la page du format de fichier."}
::option[`man 1 passwd`]{#passwd-command-page explanation="La section 1 contient les commandes utilisateur ; cette forme choisit donc la page de la commande `passwd`."}
:::

## Lorsqu'une page manque

Tous les noms de commandes ne possèdent pas une page installée séparément. Si `man` ne trouve aucune entrée :

- exécutez `type NAME` pour savoir comment Bash résout le nom ;
- utilisez `help NAME` s'il s'agit d'une commande intégrée à Bash ;
- essayez `NAME --help` si un programme externe suit cette convention ;
- vérifiez si votre distribution propose un paquet de documentation séparé.

:::single-choice{#missing-builtin-manual}
`type cd` indique que `cd` est intégrée à Bash et aucune page séparée n'est disponible. Quelle commande faut-il essayer ensuite ?

::option[`whatis cd`]{#whatis-missing-cd explanation="`whatis` résume les entrées de la base des manuels ; elle ne peut pas fournir une page dédiée absente pour la commande intégrée."}
::option[`file cd`]{#file-cd-name explanation="`file` classe des objets du système de fichiers, alors qu'ici `cd` est résolue comme commande intégrée et non comme chemin."}
::option[`help cd`]{#builtin-cd-help .correct explanation="La commande intégrée `help` de Bash fournit la documentation du shell pour `cd`."}
:::

## Résumé

Vous savez maintenant localiser et parcourir la documentation man installée.

1. Ouvrir une page par son nom de sujet.
2. Rechercher et se déplacer dans une page avec la visionneuse habituelle.
3. Quitter la visionneuse et revenir au shell.
4. Choisir une section numérotée du manuel.
5. Choisir une autre source d'aide lorsqu'une page est indisponible.
