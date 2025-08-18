---
lang: "fr"
title: "Utilisation du disque"
meta_title: "Utilisation du disque - Le Filesystem"
meta_description: "Apprenez à vérifier l'utilisation du disque et l'espace libre sous Linux à l'aide des commandes df et du. Comprenez leurs différences et quand utiliser chacune d'elles. Tutoriel de gestion de disque Linux."
meta_keywords: "commande df, commande du, utilisation du disque Linux, vérifier l'espace libre, tutoriel Linux, Linux pour débutants, gestion de disque, guide Linux"
---

## Lesson Content

Il existe quelques outils que vous pouvez utiliser pour voir l'utilisation de vos disques :

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

La commande `df` vous montre l'utilisation de vos systèmes de fichiers actuellement montés. L'option `-h` vous donne un format lisible par l'homme. Vous pouvez voir quel est le périphérique et quelle capacité est utilisée et disponible.

Supposons que votre disque est en train de se remplir et que vous voulez savoir quels fichiers ou répertoires occupent cet espace ; pour cela, vous pouvez utiliser la commande **du**.

```bash
du -h
```

Ceci vous montre l'utilisation du disque du répertoire courant dans lequel vous vous trouvez. Vous pouvez jeter un coup d'œil au répertoire racine avec `du -h /`, mais cela peut devenir un peu encombré.

Ces deux commandes sont si similaires dans leur syntaxe qu'il peut être difficile de se souvenir laquelle utiliser. Pour vérifier la quantité d'espace **libre** sur votre **disque**, utilisez `df`. Pour vérifier l'**utilisation du disque**, utilisez `du`.

## Exercise

Examinez l'utilisation de votre disque et l'espace libre avec `du` et `df`.

## Quiz Question

Quelle commande est utilisée pour afficher la quantité d'espace libre sur votre disque ?

## Quiz Answer

df
