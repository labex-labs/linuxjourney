---
lang: "fr"
title: "aide"
meta_title: "aide - Command Line"
meta_description: "Apprenez à utiliser la commande 'help' dans Bash pour une assistance rapide en ligne de commande. Comprenez les commandes intégrées et trouvez les options pour les programmes Linux."
meta_keywords: "commande help Linux, aide Bash, aide ligne de commande, commandes Linux, Linux débutant, tutoriel Linux, tutoriel Bash"
---

## Lesson Content

Linux dispose d'excellents outils intégrés pour vous aider à comprendre comment utiliser une commande ou à vérifier les options disponibles pour une commande. Un outil, `help`, est une commande Bash intégrée qui fournit de l'aide pour d'autres commandes Bash (par exemple, `echo`, `logout`, `pwd`).

```bash
help echo
```

Ceci vous donnera une description et les options que vous pouvez utiliser lorsque vous souhaitez exécuter `echo`. Pour d'autres programmes exécutables, il est conventionnel d'avoir une option appelée `--help` ou quelque chose de similaire.

```bash
echo --help
```

Tous les développeurs qui livrent des exécutables ne se conformeront pas à cette norme, mais c'est probablement votre meilleure chance de trouver de l'aide sur un programme.

## Exercise

Exécutez `help` sur la commande `echo`, la commande `logout` et la commande `pwd`.

## Quiz Question

Comment obtenir une aide rapide en ligne de commande pour les commandes Bash intégrées ?

## Quiz Answer

help
