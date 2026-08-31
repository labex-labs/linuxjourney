---
lesson_id: "kernel-logging"
course_id: "logging"
lang: "fr"
order_index: 4
title: "Journalisation du noyau"
description: "Découvrez comment interroger les messages actuels et conservés du noyau Linux avec dmesg et journalctl."
meta_title: "Journalisation du noyau - Journaux"
meta_description: "Explorez les journaux du noyau Linux avec dmesg, journalctl et /var/log/kern.log pour analyser le démarrage, les pilotes et le matériel."
meta_keywords: "journal noyau Linux, kern.log, /var/log/kern.log, dmesg, messages démarrage, événements noyau"
---

Le noyau émet des messages concernant le démarrage, les pilotes, les périphériques, les systèmes de fichiers, le réseau, la mémoire et les défaillances. Ces enregistrements peuvent expliquer des symptômes de bas niveau, mais un seul avertissement ne prouve pas que le matériel est défectueux.

## Lire le tampon circulaire du noyau

`dmesg` lit les messages du tampon circulaire du noyau :

```bash
$ dmesg --human
```

Le tampon possède une capacité finie ; les nouveaux messages peuvent donc écraser les plus anciens. Son accès peut aussi être limité aux utilisateurs privilégiés. `dmesg --follow` suit les nouveaux messages sur les implémentations qui le prennent en charge ; arrêtez-le après une reproduction limitée.

:::single-choice{#kernel-log-ring-buffer-limit}
Pourquoi un ancien événement du noyau peut-il être absent de la sortie actuelle de `dmesg` ?

::option[Les événements du noyau ne peuvent contenir qu'un seul caractère.]{#kernel-log-one-character explanation="Les messages du noyau peuvent contenir du texte de diagnostic et des métadonnées ordinaires."}
::option[`dmesg` supprime définitivement chaque ligne après l'avoir affichée.]{#kernel-log-display-deletes explanation="Une lecture normale ne consomme pas tous les messages affichés du noyau."}
::option[Le tampon circulaire fini a pu l'écraser.]{#kernel-log-overwritten .correct explanation="Le tampon en mémoire ne conserve qu'une quantité limitée de données de messages du noyau."}
:::

## Employer des horodatages lisibles

Les horodatages bruts du noyau sont généralement relatifs au démarrage. `dmesg --ctime` ou `--human` peut les afficher selon l'heure murale, mais les valeurs converties dépendent de l'historique de l'horloge et peuvent être inexactes si celle-ci a changé après le démarrage. Préservez le temps relatif au démarrage lorsqu'un séquençage précis est important.

:::single-choice{#kernel-log-timestamp-caution}
Pourquoi faut-il interpréter prudemment les horodatages d'heure murale convertis par `dmesg` ?

::option[Ils désignent toujours une autre machine.]{#kernel-log-other-machine explanation="Ils sont calculés localement, même si les changements d'horloge peuvent influencer la conversion."}
::option[Ils dépendent de l'association du temps relatif au démarrage à une horloge susceptible de changer.]{#kernel-log-clock-change .correct explanation="La synchronisation du temps ou une modification manuelle de l'horloge peut rendre l'heure affichée trompeuse."}
::option[Ils affichent l'espace libre du système de fichiers au lieu de l'heure.]{#kernel-log-free-space explanation="Les options d'horodatage affichent toujours des heures, pas la capacité du stockage."}
:::

## Interroger les enregistrements persistants du noyau

Sur un hôte systemd, interrogez les enregistrements du démarrage actuel avec :

```bash
$ journalctl -k -b
```

Si le stockage persistant du journal a conservé des démarrages antérieurs, affichez leur liste et sélectionnez-en un :

```bash
$ journalctl --list-boots
$ journalctl -k -b -1
```

Le routage syslog traditionnel peut créer `/var/log/kern.log` ou un autre fichier, mais cela dépend de la configuration. Un fichier `/var/log/dmesg` enregistré n'est pas non plus universel et peut ne représenter qu'un instantané du démarrage.

:::single-choice{#kernel-log-previous-boot}
Quelle commande demande les messages du noyau du démarrage précédent conservé ?

::option[`journalctl -u kernel -f`]{#kernel-log-unit-follow explanation="Les messages du noyau se sélectionnent avec `-k`, et le suivi ne choisit pas le démarrage précédent."}
::option[`dmesg --clear`]{#kernel-log-clear explanation="L'effacement change l'état du tampon et ne récupère pas un ancien démarrage."}
::option[`journalctl -k -b -1`]{#kernel-log-previous .correct explanation="Le filtre du noyau combiné au décalage de démarrage moins un sélectionne le précédent conservé."}
:::

## Enquêter sur un événement du noyau

Identifiez le démarrage, l'horodatage, le périphérique, le sous-système et l'action en cours à ce moment-là. Interrogez les enregistrements voisins du noyau et des services, puis comparez-les à l'inventaire et à l'état actuel du matériel :

```bash
$ journalctl -k -b --since '10 minutes ago'
$ lspci -k
$ lsblk
```

N'employez que les outils pertinents pour le sous-système. Avant de recharger un pilote, dissocier un périphérique ou redémarrer, évaluez l'impact sur le stockage, le réseau, la console et les services, puis préservez l'accès de récupération.

:::single-choice{#kernel-log-warning-response}
Quelle est la meilleure réaction à une seule ligne d'avertissement du noyau ?

::option[Décharger immédiatement tous les pilotes actifs.]{#kernel-log-unload-all explanation="Cela peut interrompre des périphériques essentiels et n'isole pas la cause de l'avertissement."}
::option[Supposer que toute la machine doit être remplacée.]{#kernel-log-replace-machine explanation="Un seul enregistrement ne suffit pas à établir cette conclusion."}
::option[La corréler aux événements voisins et à l'état actuel du sous-système.]{#kernel-log-correlate .correct explanation="Le contexte et un impact reproductible sont nécessaires avant de choisir une correction."}
:::

## Résumé

Vous savez maintenant distinguer les messages du tampon actif du noyau des journaux conservés.

1. Lire le tampon circulaire fini avec `dmesg`.
2. Interpréter prudemment les horodatages relatifs au démarrage et convertis.
3. Interroger le démarrage actuel ou précédent avec `journalctl -k`.
4. Corréler les messages du noyau avant toute modification perturbatrice.
