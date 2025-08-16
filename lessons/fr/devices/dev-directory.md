---
lang: "fr"
title: "Répertoire /dev"
description: "Découvrez le répertoire /dev sous Linux, où les fichiers de périphérique sont stockés. Comprenez les nœuds de périphérique et comment interagir avec eux. Explorez /dev avec ls. Guide pour débutants Linux."
keywords: "répertoire /dev, fichiers de périphérique Linux, nœuds de périphérique, tutoriel Linux, ls /dev, débutant Linux, guide Linux"
---

## Lesson Content

Lorsque vous connectez un périphérique à votre machine, il a généralement besoin d'un pilote de périphérique pour fonctionner correctement. Vous pouvez interagir avec les pilotes de périphérique via des fichiers de périphérique ou des nœuds de périphérique ; ce sont des fichiers spéciaux qui ressemblent à des fichiers ordinaires. Puisque ces fichiers de périphérique sont comme des fichiers ordinaires, vous pouvez utiliser des programmes tels que `ls`, `cat`, etc., pour interagir avec eux. Ces fichiers de périphérique sont généralement stockés dans le répertoire `/dev`. Allez-y et `ls` le répertoire `/dev` sur votre système ; vous verrez une grande quantité de fichiers de périphérique qui se trouvent sur votre système.

```bash
ls /dev
```

Certains de ces périphériques, vous les avez déjà utilisés et avec lesquels vous avez interagi, comme `/dev/null`. Rappelez-vous quand nous envoyons la sortie à `/dev/null`, le noyau sait que ce périphérique prend toutes nos entrées et les jette simplement, donc rien n'est retourné.

Autrefois, si vous vouliez ajouter un périphérique à votre système, vous ajoutiez le fichier de périphérique dans `/dev` et l'oubliiez probablement. Eh bien, répétez cela plusieurs fois, et vous pouvez voir où il y avait un problème. Le répertoire `/dev` serait encombré de fichiers de périphérique statiques de périphériques que vous avez depuis longtemps mis à niveau, cessé d'utiliser, etc. Les périphériques se voient également attribuer des fichiers de périphérique dans l'ordre où le noyau les trouve. Ainsi, si chaque fois que vous redémarriez votre système, les périphériques pouvaient avoir des fichiers de périphérique différents selon le moment où ils ont été découverts.

Heureusement, nous n'utilisons plus cette méthode. Maintenant, nous avons quelque chose que nous utilisons pour ajouter et supprimer dynamiquement les périphériques qui sont actuellement utilisés sur le système, et nous en discuterons dans les leçons à venir.

## Exercise

Consultez le contenu du répertoire `/dev`. Reconnaissez-vous des périphériques familiers ?

## Quiz Question

Où les fichiers de périphérique sont-ils stockés sur le système ?

## Quiz Answer

/dev
