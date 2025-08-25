---
index: 9
lang: "fr"
title: "Utilisation du disque"
meta_title: "Utilisation du disque - Le système de fichiers"
meta_description: "Apprenez à vérifier l'utilisation du disque et l'espace libre sous Linux à l'aide des commandes df et du. Comprenez leurs différences et quand utiliser chacune d'elles. Tutoriel de gestion de disque Linux."
meta_keywords: "commande df, commande du, utilisation disque Linux, vérifier espace libre, tutoriel Linux, Linux débutant, gestion disque, guide Linux"
---

## Lesson Content

Il existe quelques outils que vous pouvez utiliser pour visualiser l'utilisation de vos disques :

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

Ces deux commandes sont si similaires dans leur syntaxe qu'il peut être difficile de se souvenir laquelle utiliser. Pour vérifier l'espace **libre** sur votre **disque**, utilisez `df`. Pour vérifier l'**utilisation du disque**, utilisez `du`.

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion et de l'utilisation de l'espace disque sous Linux :

1. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer, formater et monter des systèmes de fichiers, qui sont les structures sous-jacentes rapportées par `df` et `du`.
2. **[Créer et activer un fichier d'échange sous Linux](https://labex.io/fr/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Apprenez à gérer la mémoire virtuelle sur disque, un aspect critique de la gestion des ressources système qui a un impact sur l'espace disque.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des ressources disque.

## Quiz Question

Quelle commande est utilisée pour afficher l'espace libre sur votre disque ?

## Quiz Answer

df
