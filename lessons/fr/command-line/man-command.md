---
index: 16
lang: "fr"
title: "man"
meta_title: "man - Ligne de commande"
meta_description: "Apprenez la commande Linux man avec des exemples pour lire les pages de manuel, rechercher dans les pages man, comprendre les sections et trouver les options des commandes."
meta_keywords: "commande man, pages man linux, manuel de commande, man ls, sections man, recherche page man, aide ligne de commande"
---

## Lesson Content

Sous Linux, presque chaque commande est accompagnée de son propre manuel d'instructions. Ceux-ci sont appelés « pages man » (abréviation de pages de manuel), et ils sont une ressource essentielle pour apprendre à utiliser le système efficacement.

### Comprendre les pages man

Les pages man sont la documentation intégrée pour les commandes Linux, les utilitaires et les appels système. Elles fournissent une description détaillée de ce que fait une commande, ses options disponibles (ou drapeaux), et comment l'utiliser. Elles sont votre première et meilleure source d'aide en ligne de commande.

### Accéder à un manuel avec man

Pour afficher le manuel de n'importe quelle commande, utilisez `man` suivi du nom de la commande. Par exemple, pour lire le manuel de `ls`, tapez :

```bash
$ man ls
```

Cela ouvre la page man de `ls`. Vous pouvez faire défiler avec les flèches, rechercher avec `/`, et appuyer sur `q` pour quitter.

### Trouver des détails sur les options de commande

Les pages man sont particulièrement utiles pour comprendre les options des commandes. Par exemple, si vous avez vu `ls -l` et souhaitez savoir ce que signifie `-l`, ouvrez `man ls` et recherchez `-l`.

Dans une page man :

- Appuyez sur `/` et tapez un terme de recherche pour chercher vers l'avant.
- Appuyez sur `n` pour passer à la correspondance suivante.
- Appuyez sur `N` pour revenir à la correspondance précédente.
- Appuyez sur `q` pour quitter.

### Comprendre les sections des pages man

Les pages de manuel sont organisées en sections numérotées. Les sections courantes incluent :

- `1` : Commandes utilisateur.
- `2` : Appels système.
- `3` : Fonctions de bibliothèque.
- `5` : Formats de fichiers.
- `8` : Commandes d'administration système.

Parfois, le même nom existe dans plus d'une section. Vous pouvez spécifier le numéro de section :

```bash
$ man 5 passwd
$ man 1 passwd
```

### Questions fréquentes

**Pourquoi la sortie de man est-elle si longue ?** Les pages man sont une documentation de référence. Utilisez la recherche dans `man` pour aller directement à la partie dont vous avez besoin.

**Comment quitter man ?** Appuyez sur `q`.

**Que faire s'il n'existe pas de page man ?** Essayez `COMMAND --help`, `help COMMAND`, ou installez le paquet de documentation pour votre distribution.

## Exercise

La pratique est la clé pour maîtriser la ligne de commande. Ces laboratoires pratiques vous aideront à renforcer vos compétences avec les commandes fondamentales. Après les avoir complétés, utilisez la commande `man` pour explorer tout le potentiel de chaque outil.

1. **[Commande Linux ls : Liste du contenu](https://labex.io/fr/labs/linux-linux-ls-command-content-listing-219205)** - Entraînez-vous à lister et analyser le contenu des fichiers et répertoires, puis utilisez `man ls` pour découvrir plus d'options.
2. **[Commande Linux pwd : Affichage du répertoire](https://labex.io/fr/labs/linux-linux-pwd-command-directory-displaying-209734)** - Apprenez la commande `pwd` pour afficher votre répertoire courant, et explorez sa page man pour plus de détails.
3. **[Commande Linux cd : Changement de répertoire](https://labex.io/fr/labs/linux-linux-cd-command-directory-changing-209733)** - Maîtrisez la navigation dans votre système de fichiers avec `cd`, et utilisez `man cd` pour comprendre ses différentes techniques.

Ces laboratoires vous aideront à appliquer les concepts clés dans des scénarios réels et à gagner en confiance avec les commandes Linux essentielles, vous préparant à utiliser efficacement `man` pour approfondir vos connaissances.

## Quiz Question

Comment voir le manuel d'une commande ? (Veuillez répondre en utilisant uniquement le nom de la commande en lettres minuscules anglaises).

## Quiz Answer

man
