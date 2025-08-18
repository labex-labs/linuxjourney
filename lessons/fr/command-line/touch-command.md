---
index: 5
lang: "fr"
title: "touch"
meta_title: "touch - Command Line"
meta_description: "Apprenez à utiliser la commande Linux touch pour créer de nouveaux fichiers et mettre à jour les horodatages. Ce guide convivial pour débutants vous aide à comprendre la gestion des fichiers."
meta_keywords: "commande touch, créer des fichiers, tutoriel Linux, horodatages de fichiers, Linux pour débutants, guide Linux, commandes de base"
---

## Lesson Content

Apprenons à créer des fichiers. Une façon très simple est d'utiliser la commande `touch`. `touch` vous permet de créer de nouveaux fichiers vides.

```bash
touch mysuperduperfile
```

Et voilà, nouveau fichier !

`touch` est également utilisé pour modifier les horodatages sur les fichiers et répertoires existants. Essayez : faites un `ls -l` sur un fichier et notez l'horodatage, puis `touch` ce fichier, et cela mettra à jour l'horodatage.

Il existe de nombreuses autres façons de créer des fichiers qui impliquent d'autres choses comme la redirection et les éditeurs de texte, mais nous y reviendrons dans le cours sur la manipulation de texte.

## Exercise

1. Créez un nouveau fichier.
2. Notez l'horodatage.
3. Touchez le fichier et vérifiez l'horodatage une fois de plus.

## Quiz Question

Comment créez-vous un fichier nommé `myfile` ?

## Quiz Answer

touch myfile
