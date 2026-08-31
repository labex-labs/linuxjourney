---
lesson_id: "managing-log-files"
course_id: "logging"
lang: "fr"
order_index: 6
title: "Gérer les fichiers de journaux"
description: "Découvrez comment configurer, tester et vérifier une rotation sûre des journaux texte avec logrotate."
meta_title: "Gérer les fichiers de journaux - Journaux"
meta_description: "Maîtrisez la gestion des journaux Linux avec logrotate : rotation, compression, conservation, permissions et tests sans modification."
meta_keywords: "logrotate, journaux Linux, gestion journaux, rotation journaux, compression, conservation, espace disque"
---

Des journaux texte sans limite peuvent épuiser un système de fichiers, tandis qu'une suppression trop agressive peut retirer des preuves nécessaires à l'exploitation ou à la conformité. `logrotate` applique aux journaux fondés sur des fichiers les règles configurées de taille, temps, compression, propriété et conservation.

## Comprendre la rotation

Une rotation typique renomme le fichier actif, crée son remplaçant, demande éventuellement à l'application de le rouvrir, compresse les anciennes générations et supprime les fichiers qui dépassent la durée de conservation. Ces étapes dépendent de la configuration ; la rotation n'est pas une sauvegarde, car les copies conservées peuvent toujours être supprimées, corrompues ou perdues avec le même hôte.

:::single-choice{#logrotate-not-backup}
Pourquoi la rotation des journaux ne remplace-t-elle pas une sauvegarde ou un archivage ?

::option[Les fichiers tournés restent soumis à la conservation locale et aux défaillances de l'hôte.]{#logrotate-local-retention .correct explanation="La rotation contrôle les générations de travail, mais ne crée pas de copie durable indépendante."}
::option[La rotation ne peut traiter que des fichiers d'images.]{#logrotate-images explanation="L'utilitaire est principalement conçu pour les fichiers de journaux."}
::option[Chaque rotation conserve toutes les générations pour toujours.]{#logrotate-forever explanation="Les règles de conservation suppriment normalement les anciennes générations."}
:::

## Trouver la configuration

Le fichier principal est généralement `/etc/logrotate.conf`, avec des fragments de paquets ou d'applications sous `/etc/logrotate.d/`. Une règle simplifiée peut ressembler à ceci :

```text
/var/log/example/app.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 example adm
}
```

Cette règle demande une évaluation quotidienne, la conservation de sept rotations, une compression retardée d'une génération, la tolérance d'un journal absent ou vide et la création d'un nouveau fichier avec un mode et des propriétaires explicites. La rotation réelle dépend aussi de l'état enregistré et de la manière dont l'ordonnanceur appelle logrotate.

:::single-choice{#logrotate-rotate-seven}
Que précise `rotate 7` ?

::option[Conserver jusqu'à sept générations tournées selon cette règle.]{#logrotate-seven-generations .correct explanation="Les générations plus anciennes sont supprimées lorsque la conservation configurée est dépassée."}
::option[Exécuter l'application sept fois par jour.]{#logrotate-run-seven explanation="La directive contrôle les générations conservées, pas l'exécution de l'application."}
::option[Définir les permissions de chaque fichier tourné au mode 0007.]{#logrotate-mode-seven explanation="Le mode des fichiers se contrôle avec des directives comme `create`."}
:::

## Coordonner avec le processus d'écriture

Après le renommage d'un journal, un démon peut continuer à écrire par son descripteur de fichier encore ouvert. Un script `postrotate` envoie souvent un signal documenté de rechargement ou de réouverture. Validez le comportement exact de l'application et limitez étroitement la portée du script.

`copytruncate` copie un fichier puis tronque l'original sur place lorsqu'une application ne peut pas rouvrir ses journaux. Des écritures peuvent être perdues ou dupliquées pendant cette fenêtre ; il s'agit donc d'un compromis et non d'un réglage universellement sûr.

:::single-choice{#logrotate-open-descriptor}
Pourquoi une application peut-elle avoir besoin d'un signal de réouverture après la rotation ?

::option[Son descripteur ouvert peut toujours référencer le fichier renommé.]{#logrotate-descriptor-renamed .correct explanation="La réouverture fait en sorte que les prochaines écritures utilisent le nouveau chemin actif."}
::option[La compression arrête automatiquement chaque processus applicatif.]{#logrotate-compression-stops explanation="La compression ne gère pas intrinsèquement le cycle de vie du processus d'écriture."}
::option[Le noyau interdit de créer un deuxième fichier de journal.]{#logrotate-kernel-forbids explanation="Plusieurs fichiers peuvent exister ; le problème est l'inode ouvert par le processus d'écriture."}
:::

## Tester avant l'activation

Employez le mode de débogage pour examiner les décisions sans faire tourner les fichiers :

```bash
$ sudo logrotate -d /etc/logrotate.conf
```

La sortie de débogage ne prouve pas que les permissions, scripts, l'espace libre ou la réouverture par l'application réussiront pendant une véritable exécution. Testez une nouvelle règle dans un environnement contrôlé, puis examinez le fichier actif, la génération tournée, la propriété, la compression, la sortie de l'application et l'état de logrotate après l'exécution. `-f` force une rotation et modifie l'état ; ne le confondez pas avec une simulation.

:::single-choice{#logrotate-debug-mode}
Que fournit `logrotate -d` ?

::option[La suppression définitive de tous les journaux expirés.]{#logrotate-debug-delete explanation="Le mode de débogage indique les décisions prévues sans effectuer la rotation."}
::option[Une rotation de production forcée sans tenir compte des règles.]{#logrotate-debug-force explanation="L'option de forçage est `-f` et modifie l'état."}
::option[Une évaluation de diagnostic sans modifier les journaux ni l'état.]{#logrotate-debug-dry .correct explanation="C'est la bonne première étape pour examiner syntaxe et décisions, suivie d'une vérification réelle contrôlée."}
:::

## Tenir compte des autres stockages

Logrotate gère les fichiers nommés par ses règles. Le journal systemd possède sa propre configuration de taille et de conservation, tandis que les bases de données et services distants disposent de contrôles distincts de cycle de vie. Surveillez la capacité du système de fichiers et la santé de la journalisation afin de détecter un processus d'écriture bloqué ou une rotation en échec avant l'épuisement de l'espace.

:::single-choice{#logrotate-journal-retention}
Une règle logrotate applique-t-elle automatiquement la conservation du journal systemd ?

::option[Non, le stockage du journal possède sa propre configuration et ses limites.]{#logrotate-journal-separate .correct explanation="Logrotate ne gère que les chemins sélectionnés par ses règles de fichiers."}
::option[Oui, car tous les journaux partagent un même moteur de conservation.]{#logrotate-all-logs explanation="La rotation des fichiers et la conservation du journal sont des mécanismes distincts."}
::option[Oui, mais seulement lorsqu'aucun journal texte n'existe.]{#logrotate-journal-fallback explanation="La présence de journaux texte ne fusionne pas les deux systèmes de conservation."}
:::

## Résumé

Vous savez maintenant concevoir et vérifier une règle de rotation sans la confondre avec un archivage.

1. Équilibrer les besoins d'espace, d'exploitation et de conservation.
2. Définir générations, compression, propriété et comportement face aux fichiers vides.
3. Se coordonner sans risque avec les applications qui gardent des descripteurs ouverts.
4. Déboguer la configuration avant une véritable rotation contrôlée.
5. Gérer séparément la conservation du journal et des stockages externes.
