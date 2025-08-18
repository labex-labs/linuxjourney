---
index: 18
lang: "fr"
title: "alias"
meta_title: "alias - Command Line"
meta_description: "Apprenez à créer et gérer des alias Linux pour les commandes courantes. Découvrez la configuration d'alias temporaires et permanents dans .bashrc. Améliorez votre efficacité en ligne de commande !"
meta_keywords: "alias Linux, alias bash, commande unalias, .bashrc, tutoriel Linux, ligne de commande, Linux débutant, guide Linux"
---

## Lesson Content

Parfois, taper des commandes peut devenir très répétitif, ou si vous devez taper une longue commande plusieurs fois, il est préférable d'avoir un alias que vous pouvez utiliser pour cela. Pour créer un alias pour une commande, vous spécifiez simplement un nom d'alias et le définissez sur la commande.

```bash
alias foobar='ls -la'
```

Maintenant, au lieu de taper `ls -la`, vous pouvez taper `foobar`, et cela exécutera cette commande — plutôt astucieux. Gardez à l'esprit que cette commande ne sauvegardera pas votre alias après un redémarrage, vous devrez donc ajouter un alias permanent dans :

```plaintext
~/.bashrc
```

ou des fichiers similaires si vous voulez qu'il persiste après un redémarrage.

Vous pouvez supprimer des alias avec la commande `unalias` :

```bash
unalias foobar
```

## Exercise

Create a couple of aliases, then remove them.

## Quiz Question

Quelle commande est utilisée pour créer un alias ?

## Quiz Answer

alias
