---
lesson_id: "ssh-login-events"
course_id: "security-logs"
lang: "fr"
order_index: 2
title: "Connexions SSH"
description: "Apprenez à reconnaître les tentatives de connexion SSH acceptées ou refusées et à regrouper celles qui utilisent la même connexion réseau."
meta_title: "Connexions SSH - Journaux de sécurité"
meta_description: "Lisez le compte, l’adresse distante, la méthode d’authentification et le résultat dans un journal SSH, puis regroupez les tentatives par identifiant de connexion."
meta_keywords: "connexions SSH, journaux SSH, authentification, connexion acceptée, connexion refusée"
---

**SSH**, pour Secure Shell, permet de se connecter à une autre machine par le réseau. La machine qui reçoit la connexion peut consigner chaque tentative. Les entrées indiquent le compte présenté et précisent si le serveur a accepté la preuve d’authentification.

## Lire le résultat

Voici deux entrées SSH simulées. Le champ `login` indique le résultat. Un refus signifie que la vérification de l’authentification a échoué. Une tentative acceptée a passé cette vérification.

```text
t=09:13:48Z source=ssh host=web-01 account=alex login=rejected
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
```

La première entrée signale un refus pour `alex`. La seconde montre une tentative acceptée pour le même compte. Chaque résultat ne vaut que pour la tentative correspondante.

:::single-choice{#ssh-login-events-outcome-order} Quelle affirmation découle des deux entrées ?

::option[La tentative la plus récente a passé la vérification.]{#ssh-login-events-outcome-later .correct explanation="La seconde entrée affiche login=accepted à 09:14:02."}
::option[Les deux tentatives ont passé la vérification.]{#ssh-login-events-outcome-both explanation="La première ligne enregistre une tentative refusée."}
::option[La tentative la plus récente a échoué.]{#ssh-login-events-outcome-failed explanation="La première a été refusée. La seconde a été acceptée."}
:::

## Lire les adresses et les méthodes d’authentification

Une adresse distante indique d’où venait la connexion, du point de vue de la machine qui l’a reçue. Ici, elle figure dans `peer`. Une adresse peut être partagée. À elle seule, elle ne permet donc pas de savoir qui l’utilisait.

```text
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
peer=192.0.2.10 method=publickey connection=17
```

La deuxième ligne poursuit la même entrée. Le champ `method` indique la preuve que SSH a vérifiée. `password` signifie que SSH a vérifié un mot de passe. `publickey` signifie que l’appareil qui se connecte a prouvé qu’il pouvait utiliser une clé acceptée par le serveur pour ce compte.

:::single-choice{#ssh-login-events-method-evidence} Que peut-on affirmer au sujet de la tentative acceptée ?

::option[Le serveur a accepté une connexion par mot de passe.]{#ssh-login-events-method-password explanation="La méthode par mot de passe aurait son propre libellé. Cette entrée indique la méthode par clé publique."}
::option[Le serveur a identifié la personne qui utilisait cette adresse.]{#ssh-login-events-method-person explanation="L’adresse indique comment la connexion est arrivée sur l’hôte. Elle ne dit pas qui se trouvait devant le clavier."}
::option[Le serveur a accepté une connexion par clé.]{#ssh-login-events-method-key .correct explanation="L’entrée affiche à la fois login=accepted et method=publickey."}
:::

## Regrouper les tentatives par connexion

Une **connexion** est le lien réseau que SSH utilise pour échanger des messages. Dans ces exemples, l’hôte attribue un identifiant à chaque connexion. Une connexion peut servir à faire plusieurs tentatives. Une même adresse peut aussi ouvrir une autre connexion.

```text
t=09:13:48Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=rejected
t=09:13:55Z host=web-01 account=alex peer=192.0.2.10 connection=18 login=rejected
t=09:14:02Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=accepted
```

Sur `web-01`, le premier et le dernier enregistrement ont le même numéro de connexion, 17. Lisez cet identifiant avec le nom de l’hôte.

![Terminal LabEx montrant des tentatives SSH simulées depuis la même adresse avec les identifiants de connexion 17 et 18](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/ssh-login-events/ssh-connections.png)

Le terminal affiche les trois tentatives simulées ensemble pour que vous puissiez comparer leurs numéros de connexion.

:::single-choice{#ssh-login-events-group-connection} Quelles entrées se rapportent à la connexion 18 sur web-01 ?

::option[Les tentatives de 09:13:48 et de 09:14:02.]{#ssh-login-events-group-seventeen explanation="Les deux lignes portent le numéro de connexion 17."}
::option[Uniquement la tentative de 09:13:55.]{#ssh-login-events-group-eighteen .correct explanation="Cette ligne est la seule qui indique la connexion 18 sur web-01."}
::option[Les trois tentatives venant de 192.0.2.10.]{#ssh-login-events-group-address explanation="Les deux numéros de connexion apparaissent pour la même adresse."}
:::

## Rechercher ce qui suit une authentification réussie

Une authentification réussie indique que SSH a accepté la preuve présentée pour ce compte. Pour savoir ce qui s’est passé ensuite, recherchez une entrée annonçant l’ouverture d’une **session**. Une session retrace l’activité qui suit l’authentification. Une entrée d’authentification réussie décrit seulement le résultat de cette vérification.

:::single-choice{#ssh-login-events-after-accepted} Quelle entrée aiderait à savoir si une authentification réussie a entraîné l’ouverture d’une session ?

::option[Une autre entrée confirmant la même authentification réussie.]{#ssh-login-events-after-accepted-again explanation="Elle ne ferait que répéter le résultat de la vérification."}
::option[Une ancienne tentative refusée pour le compte sur un autre hôte.]{#ssh-login-events-after-other-host explanation="Cette entrée décrit une autre tentative sur une autre machine."}
::option[Une entrée indiquant qu’une session a été ouverte pour cette connexion.]{#ssh-login-events-after-session .correct explanation="Elle décrit l’étape suivante et peut la rattacher à la connexion acceptée."}
:::

## Résumé

Vous savez maintenant lire le résultat d’une tentative SSH et déterminer quelles entrées se rapportent à la même connexion.

1. Distinguer les tentatives acceptées des tentatives refusées.
2. Décrire une tentative à l’aide de l’adresse distante et de la méthode d’authentification.
3. Regrouper les entrées par hôte et par connexion lorsqu’un identifiant est disponible.
4. Chercher une entrée de session pour savoir ce qui a suivi une authentification réussie.
