---
lesson_id: "system-logging"
course_id: "logging"
lang: "fr"
order_index: 1
title: "Journalisation du système"
description: "Découvrez comment les sources, collecteurs, stockages et outils de consultation des journaux Linux s'articulent."
meta_title: "Journalisation du système - Journaux"
meta_description: "Découvrez la journalisation système Linux, syslog, rsyslogd, le journal systemd et la manière de trouver et lire les journaux dans /var/log."
meta_keywords: "journalisation système Linux, syslog, rsyslogd, /var/log, journaux système, journalctl"
---

Les journaux consignent les événements émis par le noyau, les services, les applications et les composants de sécurité. Ils facilitent le dépannage et l'audit, mais seulement si la collecte fonctionne, si les horodatages sont compris et si la source concernée est incluse.

## Suivre un message de journal

Le parcours de journalisation comprend plusieurs parties distinctes :

1. Une source émet un événement.
2. Un collecteur l'accepte et l'enrichit.
3. Les règles de routage et de conservation choisissent les destinations de stockage ou de transfert.
4. Un outil de consultation interroge les enregistrements conservés.

Sur un hôte systemd, `systemd-journald` collecte couramment la sortie standard des services, les messages du noyau et les messages natifs du journal ou de syslog. Un démon syslog comme rsyslog peut également recevoir les messages, les écrire dans des fichiers texte traditionnels ou les transférer. Les applications peuvent plutôt entretenir leurs propres fichiers ou une télémétrie externe.

:::single-choice{#system-logging-distinct-roles}
Quel composant décide où les messages acceptés sont stockés ou transférés ?

::option[Le répertoire de travail actuel du terminal.]{#system-logging-cwd explanation="Un répertoire du shell ne définit pas les routes de journalisation à l'échelle du système."}
::option[Le nom de fichier de l'image du noyau actif.]{#system-logging-kernel-file explanation="Le noyau peut émettre des messages, mais le nom de son image ne définit pas la politique de routage."}
::option[La configuration du routage et de la conservation.]{#system-logging-routing .correct explanation="Les règles situées entre la collecte et le stockage déterminent les destinations et le comportement de conservation."}
:::

## Découvrir les journaux disponibles

Ne supposez pas que chaque hôte possède les mêmes fichiers. Examinez les services de journalisation actifs et la configuration locale :

```bash
$ systemctl --type=service --state=running | grep -E 'journal|syslog'
$ ls -la /var/log
$ journalctl --disk-usage
```

`/var/log/syslog` est courant dans la famille Debian avec un routage compatible, tandis que `/var/log/messages` l'est ailleurs. Les deux peuvent être absents sur un hôte qui emploie uniquement le journal. La documentation des applications et la configuration des unités peuvent révéler d'autres destinations.

:::single-choice{#system-logging-file-absence}
Que signifie nécessairement l'absence du fichier `/var/log/syslog` ?

::option[L'hôte peut employer une autre destination de journalisation configurée.]{#system-logging-other-destination .correct explanation="Les systèmes fondés uniquement sur le journal et les différentes politiques syslog ne créent pas nécessairement ce fichier."}
::option[Le noyau n'a jamais produit le moindre message.]{#system-logging-no-kernel explanation="Des enregistrements du noyau peuvent se trouver dans le journal ou dans une autre destination."}
::option[Toutes les applications ont cessé de fonctionner.]{#system-logging-apps-stopped explanation="L'état des applications ne peut pas se déduire d'un seul chemin absent."}
:::

## Interroger le journal

Commencez par une requête limitée plutôt que d'afficher tout le journal :

```bash
$ journalctl -b -p warning
$ journalctl -u ssh.service --since '1 hour ago'
```

`-b` sélectionne le démarrage actuel, `-p` filtre selon la priorité et `-u` selon une unité. Les noms d'unités et les démarrages conservés diffèrent selon l'hôte. Employez `journalctl --list-boots` pour afficher les démarrages disponibles et `journalctl -f` pour suivre les nouveaux enregistrements pendant la reproduction d'un problème.

:::single-choice{#system-logging-current-boot}
Quelle option limite une requête `journalctl` au démarrage actuel ?

::option[`-b`]{#system-logging-boot-option .correct explanation="Sans argument, le sélecteur de démarrage choisit celui en cours."}
::option[`-u`]{#system-logging-unit-option explanation="Cette option filtre selon une unité systemd."}
::option[`-f`]{#system-logging-follow-option explanation="Cette option suit les nouveaux enregistrements ajoutés."}
:::

## Lire les enregistrements dans leur contexte

Une ligne traditionnelle de style syslog peut ressembler à ceci :

```text
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Elle contient un horodatage, un hôte, un programme et un PID, puis un message. Considérez le texte du message comme la sortie d'une application, pas comme un fait structuré garanti. Vérifiez le fuseau horaire, la synchronisation de l'horloge, l'identifiant de démarrage, la réutilisation des PID et les enregistrements qui précèdent et suivent immédiatement l'événement. Les champs du journal peuvent offrir des identifiants plus solides que le seul texte affiché.

Les journaux peuvent contenir des noms d'utilisateurs, adresses, chemins, jetons ou d'autres données sensibles. Appliquez le moindre privilège, expurgez les exportations et préservez les originaux et horodatages pendant une enquête.

:::single-choice{#system-logging-export-safety}
Que faut-il faire avant de partager un extrait de journal à l'extérieur ?

::option[Remplacer chaque horodatage par une valeur aléatoire.]{#system-logging-random-time explanation="Détruire les informations temporelles peut empêcher la corrélation et ne constitue pas une bonne méthode d'expurgation."}
::option[Rechercher les secrets et identifiants sensibles qu'il contient.]{#system-logging-review-sensitive .correct explanation="Les journaux contiennent souvent des données opérationnelles ou personnelles qui exigent une expurgation contrôlée."}
::option[Rendre le journal original accessible en écriture à tous.]{#system-logging-world-writable explanation="Affaiblir les contrôles d'accès peut nuire à l'intégrité et exposer d'autres données."}
:::

## Résumé

Vous savez maintenant trouver et interroger les journaux Linux sans supposer un chemin de stockage universel.

1. Distinguer sources d'événements, collecteurs, routage, stockage et outils de consultation.
2. Découvrir la configuration de journalisation active de l'hôte.
3. Employer des requêtes limitées selon l'unité, le démarrage, l'heure ou la priorité.
4. Corréler les enregistrements dans leur contexte et protéger les données sensibles.
