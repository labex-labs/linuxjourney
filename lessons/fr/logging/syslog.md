---
lesson_id: "syslog"
course_id: "logging"
lang: "fr"
order_index: 2
title: "syslog"
description: "Découvrez le fonctionnement des facilities, niveaux de gravité, règles de routage de syslog et de la commande logger."
meta_title: "syslog - Journaux"
meta_description: "Découvrez syslog et rsyslog sous Linux, les niveaux et facilities, les règles de routage et la commande logger."
meta_keywords: "syslog, rsyslog, journaux Linux, commande logger, /var/log/syslog, facilities syslog, niveaux gravité"
---

Syslog définit un modèle de messages et des conventions de transport employés par de nombreux systèmes de type Unix. Rsyslog est une implémentation capable de recevoir, filtrer, transformer, stocker et transférer les messages. Il peut coexister avec `systemd-journald` ; aucun de ces noms ne signifie que chaque application emprunte cette voie.

## Facilities et niveaux de gravité

Un message syslog possède une facility qui décrit sa grande catégorie de source et un niveau de gravité allant de l'urgence au débogage. Parmi les facilities courantes figurent `auth`, `cron`, `daemon`, `kern`, `mail`, `user` et `local0` à `local7`.

Les niveaux de gravité sont ordonnés. Dans la syntaxe classique des sélecteurs, `daemon.warning` correspond normalement aux messages de daemon au niveau warning et à tous les niveaux plus graves, pas uniquement à warning. Une correspondance exacte emploie un modificateur égal dans les implémentations qui prennent en charge cette syntaxe, par exemple `daemon.=warning`.

:::single-choice{#syslog-warning-selector}
À quoi un sélecteur classique comme `daemon.warning` correspond-il normalement ?

::option[Uniquement aux messages dont le texte contient le mot daemon.]{#syslog-text-daemon explanation="Ce sélecteur repose sur les métadonnées de facility, pas sur une recherche dans le texte."}
::option[À chaque message de débogage de toutes les facilities.]{#syslog-all-debug explanation="Le sélecteur se limite à la facility daemon et à un seuil de gravité."}
::option[Aux avertissements et aux messages plus graves de daemon.]{#syslog-warning-or-higher .correct explanation="Le sélecteur de priorité comprend le niveau nommé et les niveaux d'urgence supérieure."}
:::

## Lire les règles rsyslog

Rsyslog charge généralement un fichier principal et des fragments sous `/etc/rsyslog.d/`. Une règle traditionnelle comprend un sélecteur suivi d'une action :

```text
auth,authpriv.*          /var/log/auth.log
*.*;auth,authpriv.none  -/var/log/syslog
kern.*                  /var/log/kern.log
```

La première ligne route toutes les priorités de deux facilities d'authentification. La deuxième sélectionne largement les messages tout en excluant ces facilities. La troisième route les messages de la facility du noyau. Un `-` au début d'une action vers un fichier demande généralement des écritures asynchrones ; il ne signifie pas une exclusion.

Examinez tous les fichiers inclus et validez la syntaxe exacte de la version installée avant de modifier le routage en production.

:::single-choice{#syslog-selector-action}
Dans une règle rsyslog traditionnelle, qu'est-ce que l'action ?

::option[L'expression de facility et de gravité située à gauche.]{#syslog-left-selector explanation="Cette partie sélectionne les messages."}
::option[La destination ou l'opération située à droite.]{#syslog-right-action .correct explanation="L'action détermine si les enregistrements sélectionnés vont vers un fichier, une cible distante ou une autre sortie."}
::option[Le commentaire qui décrit la version du paquet.]{#syslog-comment-version explanation="Les commentaires n'effectuent aucun routage de messages."}
:::

## Envoyer un message de test

Employez `logger` pour soumettre un test contrôlé, avec une étiquette et une priorité reconnaissables :

```bash
$ logger -p user.notice -t lesson-test 'routing check 2026-08-31T10:00'
```

Interrogez ensuite la destination attendue, par exemple :

```bash
$ journalctl -t lesson-test --since '5 minutes ago'
```

Le même événement peut apparaître dans le journal et dans un fichier texte selon le transfert et le routage. `logger -s` copie aussi le message sur la sortie d'erreur standard ; cela ne prouve pas son stockage durable.

:::single-choice{#syslog-logger-tag}
Qu'ajoute `logger -t lesson-test` au message soumis ?

::option[Une demande de suppression des anciens enregistrements de test.]{#syslog-tag-delete explanation="L'option définit une étiquette d'identification et ne gère pas la conservation."}
::option[L'identifiant `lesson-test` comme étiquette du message.]{#syslog-tag-identifier .correct explanation="Une étiquette unique facilite la recherche de l'événement contrôlé dans les destinations configurées."}
::option[Un délai de livraison de cinq minutes.]{#syslog-tag-delay explanation="L'option d'étiquette n'encode aucun délai de livraison."}
:::

## Modifier et vérifier le routage

Avant tout changement, sauvegardez la configuration actuelle et identifiez les consommateurs en aval. Validez la syntaxe avec le mode de vérification de l'implémentation, couramment :

```bash
$ sudo rsyslogd -N1
```

Ne rechargez le service au moyen de son gestionnaire qu'après cette validation. Envoyez un nouveau message étiqueté, vérifiez chaque destination nécessaire et contrôlez l'état du service ainsi que ses journaux d'erreurs internes. Une règle syntaxiquement valide peut encore router trop largement, dupliquer les enregistrements ou exposer des données sensibles.

Le transfert distant doit employer un transport authentifié et chiffré lorsque les journaux traversent des réseaux non fiables. UDP n'offre aucun accusé de réception de bout en bout ; les besoins d'audit essentiels exigent une conception tenant compte des files, pertes, de l'intégrité, du contrôle d'accès et des pannes du récepteur.

:::single-choice{#syslog-change-verification}
Quelle preuve suffit à montrer qu'une nouvelle règle de routage fonctionne ?

::option[Le fichier de configuration possède une date de modification récente.]{#syslog-mtime explanation="Un horodatage ne prouve ni la validité de la syntaxe, ni la livraison."}
::option[L'émetteur peut joindre le récepteur avec un ping.]{#syslog-ping explanation="L'accessibilité réseau seule ne vérifie ni le protocole de journalisation, ni le chemin de stockage."}
::option[La validation réussit et un test étiqueté atteint chaque destination prévue.]{#syslog-validate-and-test .correct explanation="La validation statique et l'observation de bout en bout d'un événement sont toutes deux nécessaires."}
:::

## Résumé

Vous savez maintenant tester le routage syslog depuis les métadonnées d'un message jusqu'à sa destination configurée.

1. Distinguer les facilities des niveaux de gravité ordonnés.
2. Lire les sélecteurs séparément de leurs actions.
3. Envoyer un événement étiqueté et priorisé avec `logger`.
4. Valider la configuration et vérifier la livraison de bout en bout.
