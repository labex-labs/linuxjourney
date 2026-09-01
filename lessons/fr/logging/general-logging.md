---
lesson_id: "general-logging"
course_id: "logging"
lang: "fr"
order_index: 3
title: "Journalisation générale"
description: "Découvrez comment trouver, filtrer, suivre et corréler les journaux généraux d'un système Linux."
meta_title: "Journalisation générale - Journaux"
meta_description: "Guide des journaux Linux généraux : /var/log/messages, syslog, journalctl, suivi, filtrage et analyse lors du dépannage."
meta_keywords: "journaux Linux, syslog, /var/log/messages, dépannage Linux, analyse journaux, surveillance système, /var/log"
---

Les journaux généraux du système réunissent les avis ordinaires, avertissements et erreurs de plusieurs sources. Ils constituent des points de départ utiles, mais leurs noms de fichiers et leur contenu dépendent des règles de routage et ne sont pas des garanties universelles de Linux.

## Trouver la source pertinente

Selon la distribution et la configuration, les messages généraux peuvent apparaître dans `/var/log/syslog`, `/var/log/messages`, le journal systemd ou plusieurs destinations. Commencez par identifier l'hôte et l'intervalle de l'incident, puis examinez les sources disponibles :

```bash
$ ls -lh /var/log
$ journalctl --since '2026-08-31 09:00' --until '2026-08-31 09:15'
```

Les journaux des applications peuvent se trouver dans leurs propres sous-répertoires ou dans un service externe. Les enregistrements d'authentification, d'audit, de paquets, de bases de données et de serveurs web peuvent être délibérément séparés du flux général.

:::single-choice{#general-logs-universal-file} Pourquoi ne faut-il pas supposer que `/var/log/messages` existe sur chaque hôte Linux ?

::option[Les destinations générales dépendent des collecteurs locaux et des règles de routage.]{#general-logs-local-routing .correct explanation="Un système qui emploie seulement le journal ou une autre configuration syslog peut choisir d'autres destinations."}
::option[Linux n'autorise qu'un seul fichier de journal par disque.]{#general-logs-one-file explanation="Les systèmes entretiennent couramment de nombreux fichiers de journaux et stockages de journal."}
::option[Le chemin est exclusivement réservé aux documents des utilisateurs.]{#general-logs-user-documents explanation="La hiérarchie `/var/log` sert conventionnellement aux journaux."}
:::

## Examiner les journaux texte

Employez `less` pour une navigation contrôlée et `tail` pour les enregistrements les plus récents :

```bash
$ sudo less /var/log/syslog
$ sudo tail -n 100 /var/log/messages
```

Suivez les nouvelles lignes pendant une reproduction limitée avec `tail -F FICHIER`. `-F` réessaie lorsqu'un fichier est remplacé pendant la rotation, contrairement à un simple instantané. Arrêtez le suivi avec `Ctrl-C` et ne laissez pas ouvertes de vastes sessions privilégiées.

:::single-choice{#general-logs-tail-f-capability} À quoi `tail -F` sert-il pendant une reproduction contrôlée ?

::option[À suivre un fichier nommé malgré son remplacement courant pendant la rotation.]{#general-logs-tail-follow .correct explanation="Le comportement de nouvelle tentative par nom aide à continuer après le renommage et la recréation du fichier actif."}
::option[À passer tous les niveaux de gravité des journaux à debug.]{#general-logs-tail-debug explanation="Tail lit le contenu des fichiers et ne reconfigure pas les émetteurs."}
::option[À déchiffrer les archives compressées sans autre programme.]{#general-logs-tail-decrypt explanation="La commande ne fournit pas de décompression ou de déchiffrement général des archives."}
:::

## Filtrer sans perdre le contexte

Recherchez dans un fichier ou un intervalle du journal limité plutôt que de canaliser immédiatement un flux actif sans borne :

```bash
$ grep -n -C 3 'connection refused' /var/log/example.log
$ journalctl -u example.service --since '10 minutes ago' --grep='connection refused'
```

La casse, la formulation, les limites de débit et la localisation peuvent rendre une recherche littérale incomplète. Consignez les événements réussis comme ceux qui échouent et conservez les lignes voisines, car la cause peut précéder l'erreur visible.

:::single-choice{#general-logs-context-lines} Pourquoi inclure les lignes qui entourent une erreur correspondante ?

::option[L'événement précédent peut expliquer la défaillance ultérieure.]{#general-logs-preceding-context .correct explanation="Le contexte temporel aide à reconstruire une séquence au lieu de considérer une seule chaîne comme tout l'incident."}
::option[Le contexte garantit que la première correspondance est la cause racine.]{#general-logs-guaranteed-cause explanation="D'autres preuves doivent encore être corrélées ; le contexte ne démontre pas la causalité."}
::option[Il modifie automatiquement la configuration du service.]{#general-logs-context-config explanation="La sortie d'une recherche est en lecture seule et ne met pas à jour les réglages du service."}
:::

## Inclure les journaux tournés et archivés

Un incident peut franchir une limite de rotation. Le fichier actif, les archives numérotées et les fichiers compressés peuvent contenir différentes parties de la même séquence. Des outils comme `zgrep` et `zless` lisent les archives compressées avec gzip :

```bash
$ sudo zgrep -n 'connection refused' /var/log/example.log*.gz
```

Ordonnez les résultats selon les véritables horodatages, pas seulement selon le suffixe. Avant de copier des preuves, préservez les métadonnées et limitez l'accès, car les journaux peuvent contenir des données personnelles ou des identifiants.

:::single-choice{#general-logs-rotation-boundary} Que faut-il examiner lorsqu'un incident franchit une rotation des journaux ?

::option[Uniquement le nouveau fichier actif vide.]{#general-logs-active-only explanation="Les enregistrements antérieurs peuvent avoir été déplacés dans les archives tournées."}
::option[Les journaux actifs et archivés, ordonnés selon l'heure des événements.]{#general-logs-all-intervals .correct explanation="La séquence pertinente peut être divisée entre les fichiers actuels et tournés."}
::option[Seulement les noms de fichiers, sans tenir compte des horodatages.]{#general-logs-filenames-only explanation="L'ordre des suffixes et celui des événements ne sont pas toujours équivalents."}
:::

## Résumé

Vous savez maintenant enquêter dans les journaux généraux à travers fichiers, journal et limites de rotation.

1. Découvrir les destinations au lieu de supposer un nom de fichier universel.
2. Lire un intervalle limité et ne suivre que pendant la reproduction.
3. Conserver le contexte temporel autour des enregistrements correspondants.
4. Inclure les archives tournées et protéger les preuves sensibles.
