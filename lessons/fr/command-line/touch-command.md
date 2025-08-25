---
index: 5
lang: "fr"
title: "touch"
meta_title: "touch - Ligne de commande"
meta_description: "Apprenez à utiliser la commande Linux touch pour créer de nouveaux fichiers et mettre à jour les horodatages. Ce guide convivial pour débutants vous aide à comprendre la gestion des fichiers."
meta_keywords: "commande touch, créer des fichiers, tutoriel Linux, horodatages de fichiers, Linux pour débutants, guide Linux, commandes de base"
---

## Lesson Content

Apprenons à créer des fichiers. Une façon très simple est d'utiliser la commande `touch`. `touch` vous permet de créer de nouveaux fichiers vides.

```bash
touch mysuperduperfile
```

Et voilà, nouveau fichier !

`touch` est également utilisé pour modifier les horodatages des fichiers et répertoires existants. Essayez : faites un `ls -l` sur un fichier et notez l'horodatage, puis `touch` ce fichier, et il mettra à jour l'horodatage.

Il existe de nombreuses autres façons de créer des fichiers qui impliquent d'autres choses comme la redirection et les éditeurs de texte, mais nous y reviendrons dans le cours sur la manipulation de texte.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la création et de la gestion des objets du système de fichiers :

1. **[Commande Linux mkdir : Création de répertoires](https://labex.io/fr/labs/linux-linux-mkdir-command-directory-creating-209739)** - Apprenez à utiliser la commande `mkdir` sous Linux pour créer des répertoires, définir des permissions et organiser votre système de fichiers. Cela vous aidera à comprendre le concept plus large de la création de nouveaux éléments dans le système de fichiers.
2. **[Mise en place d'une nouvelle structure de projet](https://labex.io/fr/labs/linux-setting-up-a-new-project-structure-387859)** - Pratiquez vos compétences en gestion de répertoires Linux en créant une structure de projet spécifique et en y naviguant à l'aide de commandes essentielles comme `mkdir` et `cd`.

Ces laboratoires vous aideront à appliquer les concepts de création et d'organisation du système de fichiers dans des scénarios réels et à renforcer votre confiance avec les commandes Linux.

## Quiz Question

Comment créez-vous un fichier nommé `myfile` ?

## Quiz Answer

touch myfile
