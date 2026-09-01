---
lesson_id: "expand-unexpand-command"
course_id: "text-fu"
lang: "fr"
order_index: 10
title: "expand et unexpand"
description: "Découvrez comment les taquets de tabulation contrôlent la conversion entre tabulations et espaces."
meta_title: "expand et unexpand - Text-Fu"
meta_description: "Mettez en forme du texte sous Linux en convertissant les tabulations en espaces et inversement avec expand et unexpand."
meta_keywords: "expand, unexpand, tabulations Linux, espaces, formatage texte"
---

Une tabulation mémorise un déplacement jusqu'au prochain taquet, pas un nombre fixe d'espaces visibles. Sa largeur dépend de la colonne courante et des taquets. `expand` et `unexpand` convertissent tabulations et espaces en tenant compte de ces positions.

## Convertir les tabulations en espaces

`expand` remplace chaque tabulation par les espaces nécessaires pour atteindre le taquet approprié et écrit sur stdout :

```bash
$ expand sample.txt
```

Par défaut, les taquets reviennent toutes les 8 colonnes. Une tabulation en colonne 1 ne devient donc pas le même nombre d'espaces qu'en colonne 6.

:::single-choice{#expand-default-tab-stops} Avec les réglages par défaut, comment `expand` remplace-t-il une tabulation ?

::option[Il insère assez d'espaces pour atteindre le prochain taquet.]{#expand-next-stop .correct explanation="`expand` préserve l'alignement en calculant les espaces requis depuis la colonne courante."}
::option[Il insère toujours exactement huit espaces.]{#expand-eight-spaces explanation="Les taquets sont espacés de huit colonnes, mais le nombre d'espaces dépend de la position."}
::option[Il retire la tabulation sans rien ajouter.]{#expand-remove-tab explanation="Il la remplace par des espaces pour préserver l'alignement."}
:::

## Choisir les taquets de tabulation

`-t NUMBER` place les taquets à l'intervalle choisi :

```bash
$ expand -t 4 sample.txt
```

GNU `expand` accepte aussi une liste de positions séparées par des virgules. `-i` limite la conversion aux tabulations précédant le premier caractère non blanc.

:::single-choice{#expand-four-column-stops} Quelle commande convertit les tabulations avec des taquets toutes les quatre colonnes ?

::option[`expand -i 4 sample.txt`]{#expand-initial-four explanation="`-i` limite la conversion aux tabulations initiales et ne prend pas 4 comme intervalle."}
::option[`unexpand -t 4 sample.txt`]{#unexpand-tabs-four explanation="`unexpand` réalise la conversion inverse."}
::option[`expand -t 4 sample.txt`]{#expand-tabs-four .correct explanation="`-t 4` demande des taquets toutes les quatre colonnes."}
:::

## Enregistrer le résultat en sécurité

`expand` ne modifie pas son entrée. Redirigez vers un autre chemin :

```bash
$ expand sample.txt > result.txt
```

N'utilisez pas `expand sample.txt > sample.txt` : le shell tronque la destination avant que `expand` ne la lise. Vérifiez le fichier séparé avant de remplacer volontairement l'original.

:::single-choice{#expand-safe-output-file} Quelle commande sauvegarde le résultat sans tronquer `sample.txt` avant sa lecture ?

::option[`expand sample.txt > sample.txt`]{#expand-same-file explanation="Le shell tronque `sample.txt` avant de lancer `expand`."}
::option[`expand sample.txt > result.txt`]{#expand-separate-result .correct explanation="Les chemins diffèrent ; la création de `result.txt` ne détruit pas la source."}
::option[`> sample.txt expand result.txt`]{#expand-leading-redirection explanation="Cette forme tronque toujours `sample.txt` et n'exprime pas la conversion voulue."}
:::

## Convertir les espaces en tabulations

`unexpand` remplace les espaces admissibles par des tabulations en préservant l'alignement. Par défaut, GNU `unexpand` ne traite que les blancs initiaux :

```bash
$ unexpand result.txt
```

Utilisez `-a` pour considérer les blancs appropriés dans toute la ligne :

```bash
$ unexpand -a result.txt
```

`-a` considère les blancs dans toute la ligne. La conversion dépend des colonnes et des taquets ; elle ne remplace pas simplement chaque groupe de huit espaces. Utilisez `-t 4` si le fichier suit une autre convention.

:::single-choice{#unexpand-default-scope} Sans `-a`, quels espaces GNU `unexpand` considère-t-il normalement ?

::option[Tous les groupes d'espaces du fichier.]{#unexpand-every-group explanation="Le traitement de toute la ligne exige `-a` et dépend encore des taquets."}
::option[Seulement les espaces après le dernier mot.]{#unexpand-trailing-blanks explanation="La portée par défaut concerne les blancs initiaux."}
::option[Seulement les blancs avant le premier caractère non blanc.]{#unexpand-initial-blanks .correct explanation="Par défaut, GNU `unexpand` se limite aux blancs en début de ligne."}
:::

:::single-choice{#unexpand-all-blanks} Quelle option demande à GNU `unexpand` de considérer aussi les blancs après le premier caractère non blanc ?

::option[`-i`]{#unexpand-initial-option explanation="Pour `expand`, `-i` limite le travail aux tabulations initiales."}
::option[`-a`]{#unexpand-all-option .correct explanation="`-a` autorise la conversion des blancs appropriés dans toute la ligne."}
::option[`-t`]{#unexpand-tab-list-option explanation="`-t` règle les taquets ; `-a` exprime explicitement la portée complète."}
:::

Sans fichier, les deux commandes lisent stdin. Une conversion aller-retour peut ne pas reconstruire le choix original entre espaces et tabulations, même si l'alignement visible reste identique.

## Résumé

Vous savez convertir tabulations et espaces tout en préservant l'alignement.

1. Développer une tabulation jusqu'au prochain taquet.
2. Régler les taquets avec `-t`.
3. Écrire dans un fichier distinct avant tout remplacement.
4. Convertir par défaut les blancs initiaux avec `unexpand`.
5. Employer `-a` pour considérer toute la ligne.
