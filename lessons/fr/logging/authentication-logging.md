---
lesson_id: "authentication-logging"
course_id: "logging"
lang: "fr"
order_index: 5
title: "Journalisation de l'authentification"
description: "Découvrez comment trouver, interpréter et corréler sans risque les enregistrements d'authentification de Linux."
meta_title: "Journalisation de l'authentification - Journaux"
meta_description: "Explorez les journaux d'authentification Linux, auth.log et secure, pour comprendre les connexions, changements de privilèges et sessions."
meta_keywords: "authentification Linux, auth.log, /var/log/secure, connexion utilisateur, sécurité Linux, journaux authentification"
---

Les journaux d'authentification aident à comprendre les tentatives de connexion, les changements de privilèges et l'activité des sessions. Ils constituent des preuves sensibles pour la sécurité, mais une seule ligne établit rarement l'intention d'un utilisateur ou la compromission d'un compte.

## Trouver les enregistrements d'authentification

Les configurations syslog de la famille Debian routent souvent les événements vers `/var/log/auth.log`, tandis que celles de la famille Red Hat emploient couramment `/var/log/secure`. Le journal systemd peut conserver les mêmes événements avec les métadonnées d'unités et de processus, et une journalisation centralisée peut détenir la copie faisant autorité.

Découvrez la destination locale et interrogez le service pertinent, par exemple :

```bash
$ sudo journalctl -u ssh.service --since '1 hour ago'
$ sudo less /var/log/auth.log
```

L'unité SSH peut s'appeler `ssh.service` ou `sshd.service`. Les permissions limitent généralement l'accès à ces enregistrements, car ils exposent des détails sur les comptes et les accès.

:::single-choice{#auth-logs-file-location}
Où les événements d'authentification Linux doivent-ils toujours être stockés ?

::option[Dans la destination choisie par les règles locales de journalisation.]{#auth-logs-local-policy .correct explanation="Les fichiers, le journal et les collecteurs centralisés varient selon la distribution et la configuration."}
::option[Dans `/var/log/auth.log` sur chaque distribution.]{#auth-logs-auth-only explanation="Ce chemin est courant dans la famille Debian, mais n'est pas universel."}
::option[Dans le fichier d'historique du shell de chaque utilisateur.]{#auth-logs-shell-history explanation="L'historique du shell consigne les commandes de l'utilisateur, pas les événements d'authentification du système."}
:::

## Interpréter un événement

Un enregistrement traditionnel peut contenir :

```text
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

Il identifie l'heure, l'hôte, le programme émetteur, le module et le service PAM, l'utilisateur demandé pour la session et l'UID d'origine. À lui seul, il n'identifie pas la personne derrière l'UID 1000 et ne prouve pas une action malveillante. Résolvez l'UID au moyen des données de comptes valides au moment de l'incident et corrélez le terminal, l'adresse distante, la session et les événements voisins.

:::single-choice{#auth-logs-uid-inference}
Qu'établit `uid=1000` dans cet enregistrement ?

::option[Que le mot de passe root a été mal saisi mille fois.]{#auth-logs-thousand-passwords explanation="La valeur est un numéro d'identité, pas un nombre de tentatives."}
::option[L'identité numérique du compte associé au processus initiateur.]{#auth-logs-numeric-identity .correct explanation="D'autres preuves sur la session et le compte sont nécessaires pour attribuer l'action à une personne."}
::option[Que l'événement provient du port TCP 1000.]{#auth-logs-port explanation="Un UID n'est pas un champ de port réseau."}
:::

## Enquêter sur les réussites et les échecs

Recherchez les tentatives acceptées et rejetées dans un intervalle limité. Pour SSH, examinez également la source de la connexion, la méthode d'authentification, le compte cible, l'ouverture et la fermeture de la session ainsi que les redémarrages du service. Des échecs répétés peuvent provenir d'une erreur de l'utilisateur, d'une automatisation aux anciens identifiants, d'une analyse ou d'une attaque ; la fréquence seule ne permet pas de choisir l'explication.

`last` et `lastb` peuvent résumer les enregistrements de `wtmp` et `btmp` lorsqu'ils sont entretenus, mais ces bases binaires possèdent leurs propres limites de conservation et d'intégrité. Recoupez-les avec les enregistrements du journal ou de syslog et les sources centralisées.

:::single-choice{#auth-logs-failed-attempts}
Avec quoi faut-il corréler les échecs répétés de connexion ?

::option[Uniquement l'espace disque libre total.]{#auth-logs-disk-space explanation="La capacité n'identifie ni la source, ni le compte cible, ni la méthode d'une tentative d'authentification."}
::option[La source, le compte cible, la méthode, l'heure et les sessions réussies.]{#auth-logs-correlated-fields .correct explanation="Ces détails aident à distinguer une mauvaise configuration, une erreur utilisateur, une analyse et un accès non autorisé."}
::option[La conclusion que le compte est certainement compromis.]{#auth-logs-certain-compromise explanation="Les échecs peuvent avoir plusieurs causes bénignes ou hostiles."}
:::

## Préserver et intervenir

Si vous soupçonnez un incident, consignez l'heure et le fuseau de l'hôte, préservez les journaux originaux et leurs métadonnées, puis protégez toute copie exportée. Évitez de modifier les preuves sur place. Le verrouillage des comptes, les changements de pare-feu et la fin des sessions peuvent interrompre un accès légitime ou alerter un attaquant ; suivez donc la procédure de réponse aux incidents et conservez une voie de récupération.

:::single-choice{#auth-logs-preservation}
Comment faut-il traiter les preuves d'authentification pendant une enquête ?

::option[Modifier les lignes suspectes dans le fichier original pour les clarifier.]{#auth-logs-edit-original explanation="Modifier la source endommage l'intégrité des preuves."}
::option[Publier tout le journal afin que chacun puisse identifier les utilisateurs.]{#auth-logs-publish explanation="Les enregistrements d'authentification peuvent exposer des identités et des détails sensibles de l'infrastructure."}
::option[Préserver les originaux et protéger les copies exportées.]{#auth-logs-preserve .correct explanation="L'intégrité et la confidentialité sont toutes deux importantes pour les journaux de sécurité."}
:::

## Résumé

Vous savez maintenant examiner les événements d'authentification sans exagérer ce qu'un seul enregistrement prouve.

1. Découvrir la destination locale configurée des journaux d'authentification.
2. Interpréter l'identité, le service, la méthode et la session dans leur contexte.
3. Corréler les activités échouées et réussies entre les sources conservées.
4. Préserver les preuves et coordonner les mesures perturbatrices.
