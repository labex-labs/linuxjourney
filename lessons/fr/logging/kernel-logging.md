---
lang: "fr"
title: "Journalisation du noyau"
meta_title: "Journalisation du noyau - Logging"
meta_description: "Apprenez la journalisation du noyau Linux avec dmesg et kern.log. Comprenez les messages de démarrage et les problèmes matériels. Explorez les journaux du noyau pour des informations système."
meta_keywords: "dmesg, kern.log, journalisation Linux, messages du noyau, journal de démarrage, tutoriel Linux, guide du débutant"
---

## Lesson Content

### /var/log/dmesg

Au moment du démarrage, votre système enregistre des informations sur le tampon circulaire du noyau. Cela nous montre des informations sur les pilotes matériels, les informations du noyau et l'état pendant le démarrage, entre autres choses. Ce fichier journal se trouve à l'adresse `/var/log/dmesg` et est réinitialisé à chaque démarrage. Vous ne verrez peut-être pas son utilité maintenant, mais si vous rencontriez un jour des problèmes lors du démarrage ou un problème matériel, `dmesg` est le meilleur endroit où chercher. Vous pouvez également consulter ce journal à l'aide de la commande `dmesg`.

### /var/log/kern.log

Un autre journal que vous pouvez utiliser pour afficher les informations du noyau est le fichier `/var/log/kern.log`. Celui-ci enregistre les informations et les événements du noyau sur votre système ; il enregistre également la sortie de `dmesg`.

## Exercise

Regardez vos journaux `dmesg` et `kern`. Quelles différences remarquez-vous ?

## Quiz Question

Quelle commande peut être utilisée pour afficher les messages de démarrage du noyau ?

## Quiz Answer

dmesg
