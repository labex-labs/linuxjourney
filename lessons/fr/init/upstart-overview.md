---
lesson_id: "upstart-overview"
course_id: "init"
lang: "fr"
order_index: 3
title: "Présentation d'Upstart"
description: "Découvrez comment l'ancien système d'initialisation Upstart relie les expressions d'événements aux objectifs du cycle de vie des jobs."
meta_title: "Présentation d'Upstart - Init"
meta_description: "Découvrez Upstart, son modèle piloté par les événements, la gestion des services et les configurations de jobs Linux."
meta_keywords: "Upstart, système init, services Linux, Ubuntu, SysV, événements Upstart, jobs Upstart"
---

Upstart est un ancien système d'initialisation et de gestion des services fondé sur les événements, développé par Canonical. Les anciennes versions d'Ubuntu et plusieurs autres distributions l'ont employé, mais les versions actuelles d'Ubuntu utilisent systemd. Étudiez Upstart pour entretenir une machine ancienne dont l'usage est confirmé, pas comme hypothèse par défaut d'une installation moderne.

## Confirmer la présence d'un ancien système Upstart

Examinez le PID 1 et l'interface de contrôle active :

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
$ initctl version
```

La dernière commande ne réussit de façon significative que si le service de contrôle Upstart et son client sont présents. Un répertoire comme `/usr/share/upstart` ou des fichiers restants sous `/etc/init` constituent de faibles indices, car des paquets et vestiges de migration peuvent subsister après la prise de contrôle par un autre système.

:::single-choice{#upstart-overview-active-evidence} Quelle est la meilleure preuve qu'un hôte emploie réellement Upstart ?

::option[Le nom d'un répertoire contient le mot `upstart`.]{#upstart-overview-directory-only explanation="De la documentation installée ou des vestiges peuvent subsister sur un système qui emploie une autre initialisation."}
::option[Le système possède au moins un script shell.]{#upstart-overview-shell-script explanation="Les scripts shell sont courants dans tous les environnements d'initialisation."}
::option[Le PID 1 et l'interface `initctl` réelle identifient Upstart.]{#upstart-overview-live-interface .correct explanation="Les preuves fournies par le processus et le contrôle à l'exécution sont plus fortes que la présence d'anciens fichiers."}
:::

## Jobs et événements

Un **job** Upstart décrit un service ou une tâche, notamment ses commandes de processus et les conditions de son cycle de vie. Un **événement** est une notification nommée accompagnée d'éventuelles variables d'environnement. La configuration du job peut exprimer le moment où son objectif doit passer au démarrage ou à l'arrêt.

Les fichiers des jobs système se trouvent souvent sous `/etc/init/` avec le suffixe `.conf`. Par exemple :

```text
description "Example worker"
start on runlevel [2345]
stop on runlevel [016]
exec /usr/local/sbin/example-worker
```

Cet exemple emploie les événements de niveaux comme entrées de compatibilité. Upstart peut aussi réagir à des événements de systèmes de fichiers, périphériques, réseaux ou applications selon ceux qu'émet le système.

:::single-choice{#upstart-overview-start-on} Que définit une section `start on` d'Upstart ?

::option[La version du noyau qui doit ensuite être compilée.]{#upstart-overview-kernel-version explanation="Les conditions d'événements d'un job ne choisissent pas une construction du noyau."}
::option[L'expression d'événements qui fait évoluer l'objectif du job vers le démarrage.]{#upstart-overview-start-condition .correct explanation="Lorsque l'expression est satisfaite, Upstart tente la transition de démarrage configurée du job."}
::option[La partition du disque où tous les jobs stockent leurs données.]{#upstart-overview-partition explanation="L'emplacement du stockage est sans rapport avec la syntaxe des événements Upstart."}
:::

## Démarrage piloté par les événements

Pendant le démarrage, Upstart charge les définitions de jobs et reçoit des événements. Les expressions `start on` ou `stop on` correspondantes mettent à jour les objectifs ; les transitions des jobs peuvent émettre d'autres événements qui débloquent le travail suivant. Les jobs indépendants peuvent progresser simultanément.

Ce modèle évite une séquence globale de scripts codée en dur, mais devient difficile à diagnostiquer lorsque les noms, l'ordre et les conditions des événements sont implicites. Les événements ne forment pas par défaut une file de messages durable : un job ajouté ou une condition modifiée plus tard ne doit pas supposer le rejeu de tous les événements passés.

:::single-choice{#upstart-overview-event-chain} Comment un job Upstart peut-il conduire au démarrage d'un autre ?

::option[Il réécrit en mémoire le binaire exécutable de l'autre job.]{#upstart-overview-rewrite-binary explanation="La coordination passe par les événements, pas par la modification du code."}
::option[Chaque job démarre toujours strictement selon l'ordre de son nom de fichier.]{#upstart-overview-filename-order explanation="Upstart emploie des expressions d'événements plutôt qu'une seule liste de démarrage ordonnée par fichiers."}
::option[Sa transition peut émettre un événement auquel correspond un autre job.]{#upstart-overview-emitted-event .correct explanation="Les expressions d'événements relient les transitions du cycle de vie de jobs autrement indépendants."}
:::

## Migration et compatibilité

Systemd peut fournir une compatibilité limitée pour certains anciens scripts de services, mais n'exécute pas la syntaxe des jobs Upstart comme des unités systemd natives. Lors d'une migration, traduisez les conditions de cycle de vie, l'environnement, les règles de relance, la journalisation, les dépendances et la sémantique de disponibilité au lieu de renommer mécaniquement les fichiers.

:::single-choice{#upstart-overview-current-ubuntu} Quel système d'initialisation les versions standard actuelles d'Ubuntu emploient-elles ?

::option[Exclusivement Upstart sur chaque installation.]{#upstart-overview-current-upstart explanation="Cela n'était vrai que pendant certaines périodes historiques et pour certaines configurations."}
::option[systemd.]{#upstart-overview-current-systemd .correct explanation="Upstart appartient aux anciennes générations d'Ubuntu ; les versions actuelles emploient systemd comme PID 1."}
::option[Aucun processus d'initialisation.]{#upstart-overview-no-init explanation="Un système Ubuntu complet a toujours besoin d'un gestionnaire de services comme PID 1."}
:::

## Résumé

Vous savez maintenant lire Upstart comme un ancien modèle de jobs et d'événements.

1. Confirmer le PID 1 réel et l'interface de contrôle.
2. Distinguer les définitions de jobs des notifications d'événements.
3. Interpréter `start on` et `stop on` comme des expressions de cycle de vie.
4. Migrer explicitement la sémantique au lieu de renommer les fichiers de configuration.
