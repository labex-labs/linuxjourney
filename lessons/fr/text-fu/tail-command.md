---
index: 9
lang: "fr"
title: "tail"
meta_title: "tail - Maîtrise du texte"
meta_description: "Apprenez à utiliser la commande `tail` sous Linux pour visualiser la fin des fichiers et surveiller les journaux. Découvrez `tail -f` pour les mises à jour en temps réel. Commencez votre parcours Linux !"
meta_keywords: "commande tail, tail Linux, tail -f, visualiser les journaux, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Similaire à la commande `head`, la commande `tail` vous permet de voir les 10 dernières lignes d'un fichier par défaut.

```bash
tail /var/log/syslog
```

Comme avec `head`, vous pouvez changer le nombre de lignes que vous souhaitez voir.

```bash
tail -n 10 /var/log/syslog
```

Une autre excellente option que vous pouvez utiliser est l'indicateur `-f` (follow) ; cela suivra le fichier au fur et à mesure qu'il grandit. Essayez et voyez ce qui se passe.

```bash
tail -f /var/log/syslog
```

Votre fichier `syslog` changera continuellement pendant que vous interagissez avec votre système, et en utilisant `tail -f`, vous pouvez voir tout ce qui est ajouté à ce fichier.

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la commande `tail` et de ses applications :

1. **[Commande Linux tail : Affichage de la fin d'un fichier](https://labex.io/fr/labs/linux-linux-tail-command-file-end-display-214303)** - Apprenez la commande Linux `tail` pour visualiser et surveiller la fin des fichiers texte, y compris l'option `-f` pour les mises à jour en temps réel.
2. **[Visualisation des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Entraînez-vous à utiliser `tail` (ainsi que `cat` et `more`) pour visualiser et naviguer efficacement dans les fichiers journaux et de configuration, ce qui est crucial pour la surveillance du système.
3. **[Détection rapide des menaces](https://labex.io/fr/labs/linux-rapid-threat-detection-387930)** - Appliquez vos connaissances de `tail` pour extraire et analyser rapidement les entrées de journal récentes, simulant une détection rapide des menaces dans un contexte de cybersécurité.

Ces laboratoires vous aideront à appliquer les concepts de visualisation et de surveillance du contenu des fichiers dans des scénarios réels et à renforcer votre confiance avec la commande `tail`.

## Quiz Question

Quel est l'indicateur utilisé pour suivre un fichier dans `tail` ?

## Quiz Answer

-f
