---
index: 1
lang: "fr"
title: "Répertoire /dev"
meta_title: "/dev directory - Périphériques"
meta_description: "Découvrez le répertoire /dev sous Linux, où les fichiers de périphérique sont stockés. Comprenez les nœuds de périphérique et comment interagir avec eux. Explorez /dev avec ls. Guide du débutant Linux."
meta_keywords: "/dev directory, fichiers de périphérique Linux, nœuds de périphérique, tutoriel Linux, ls /dev, débutant Linux, guide Linux"
---

## Lesson Content

Lorsque vous connectez un périphérique à votre machine, il a généralement besoin d'un pilote de périphérique pour fonctionner correctement. Vous pouvez interagir avec les pilotes de périphérique via des fichiers de périphérique ou des nœuds de périphérique ; ce sont des fichiers spéciaux qui ressemblent à des fichiers ordinaires. Puisque ces fichiers de périphérique sont comme des fichiers ordinaires, vous pouvez utiliser des programmes tels que `ls`, `cat`, etc., pour interagir avec eux. Ces fichiers de périphérique sont généralement stockés dans le répertoire `/dev`. Allez-y et utilisez `ls` sur le répertoire `/dev` de votre système ; vous verrez un grand nombre de fichiers de périphérique qui se trouvent sur votre système.

```bash
ls /dev
```

Certains de ces périphériques que vous avez déjà utilisés et avec lesquels vous avez interagi, comme `/dev/null`. Rappelez-vous que lorsque nous envoyons une sortie à `/dev/null`, le noyau sait que ce périphérique prend toutes nos entrées et les jette simplement, donc rien n'est retourné.

Autrefois, si vous vouliez ajouter un périphérique à votre système, vous ajoutiez le fichier de périphérique dans `/dev` et l'oubliiez probablement. Eh bien, répétez cela plusieurs fois, et vous pouvez voir où il y avait un problème. Le répertoire `/dev` serait encombré de fichiers de périphériques statiques de périphériques que vous avez depuis longtemps mis à niveau, cessé d'utiliser, etc. Les périphériques sont également assignés des fichiers de périphérique dans l'ordre où le noyau les trouve. Ainsi, si à chaque fois que vous redémarriez votre système, les périphériques pouvaient avoir des fichiers de périphérique différents selon le moment où ils ont été découverts.

Heureusement, nous n'utilisons plus cette méthode. Maintenant, nous avons quelque chose que nous utilisons pour ajouter et supprimer dynamiquement les périphériques qui sont actuellement utilisés sur le système, et nous en discuterons dans les leçons à venir.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des périphériques matériels et de leur interaction avec le système Linux :

1. **[Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour explorer, identifier et inspecter les périphériques matériels dans un environnement Linux. Vous acquerrez une expérience pratique avec de puissants utilitaires en ligne de commande pour comprendre comment le système d'exploitation interagit avec les composants physiques.

Ce laboratoire vous aidera à appliquer les concepts d'interaction des périphériques dans des scénarios réels et à renforcer votre confiance dans la gestion du matériel sous Linux.

## Quiz Question

Où les fichiers de périphérique sont-ils stockés sur le système ?

## Quiz Answer

/dev
