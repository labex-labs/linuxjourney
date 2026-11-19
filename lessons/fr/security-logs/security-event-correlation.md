---
lesson_id: "security-event-correlation"
course_id: "security-logs"
lang: "fr"
order_index: 5
title: "Corrélation d’événements"
description: "Apprenez à rapprocher des entrées de sécurité grâce à l’heure, à l’hôte, au compte et à la session."
meta_title: "Corrélation d’événements - Journaux de sécurité"
meta_description: "Comparez des entrées SSH et sudo, alignez les horodatages et déterminez quels éléments appuient un lien entre les événements."
meta_keywords: "corrélation d’événements, journaux de sécurité, connexions SSH, événements sudo, horodatage, identifiants de session"
---

Une entrée indique que quelqu’un s’est connecté à une machine. Une autre montre qu’une commande a été autorisée. Peut-on faire le lien ? La **corrélation d’événements** consiste à comparer plusieurs entrées pour savoir si elles décrivent des activités liées.

## Lire deux entrées

SSH permet de se connecter à une autre machine. Une fois connecté, on peut utiliser `sudo` pour demander l’exécution d’une commande sous un autre compte. Voici deux entrées simulées du même jour. Elles utilisent les mêmes noms de champs pour faciliter l’exercice. Les vrais journaux peuvent utiliser d’autres noms ou omettre certains champs.

```text
t=09:14:02Z      source=ssh   host=web-01 account=alex session=42 login=accepted
t=11:15:10+02:00 source=sudo  host=web-01 account=alex session=42 decision=allowed
```

Le champ `source` indique l’outil qui signale l’événement et `host` désigne la machine où il a eu lieu. Les deux entrées mentionnent une activité sous le compte `alex`. Il faudrait d’autres éléments pour savoir qui a utilisé ce compte.

:::single-choice{#security-event-correlation-account-evidence} Un membre de l’équipe affirme qu’Alex a fait lui-même la demande sudo. Qu’établissent les entrées à ce stade ?

::option[Alex a lui-même fait la demande sudo.]{#security-event-correlation-account-person explanation="Le nom d’un compte ne suffit pas à identifier la personne qui l’utilisait."}
::option[Les entrées signalent des activités sous deux comptes différents.]{#security-event-correlation-account-different explanation="Les deux champs account indiquent alex. Les champs source diffèrent parce qu’ils indiquent les outils qui signalent l’activité."}
::option[Les deux événements mentionnent le même compte.]{#security-event-correlation-account-shared .correct explanation="Les deux entrées indiquent alex. Il faudrait d’autres éléments pour identifier la personne qui utilisait le compte."}
:::

## Comparer les heures des événements

Le champ `t` contient l’heure enregistrée. Dans la première entrée, `Z` indique l’heure UTC, une référence commune pour la comparaison. Dans la seconde, `+02:00` signifie que l’heure affichée est deux heures en avance sur UTC. Retirez donc deux heures à `11:15:10` pour obtenir `09:15:10` UTC.

Comparez maintenant `09:14:02` et `09:15:10`. La connexion a été enregistrée en premier. Deux événements très proches dans le temps peuvent néanmoins venir de connexions distinctes.

:::single-choice{#security-event-correlation-time-order} Un autre jour, une connexion est enregistrée à `09:14Z` et une demande à `11:13+02:00`. Dans quel ordre surviennent-elles ?

::option[La demande précède la connexion d’une minute.]{#security-event-correlation-time-request-first .correct explanation="En retirant deux heures, la demande est à 09:13 UTC. La connexion est à 09:14 UTC."}
::option[La connexion précède la demande d’une minute.]{#security-event-correlation-time-login-first explanation="La demande correspond à 09:13 UTC, soit une minute avant la connexion à 09:14 UTC."}
::option[La connexion précède la demande de près de deux heures.]{#security-event-correlation-time-unadjusted explanation="Ce raisonnement compare les heures affichées telles quelles. Convertissez les deux en UTC avant de les ordonner."}
:::

## Vérifier l’hôte et la session

Une **session** couvre la période entre la connexion et la fermeture de session ou la déconnexion. Dans ces exemples, l’entrée SSH contient l’identifiant rattaché à la connexion acceptée. Les deux sources utilisent le même identifiant pour cette connexion sur le même hôte. Les deux premières entrées indiquent `host=web-01` et `session=42`, ce qui rattache la connexion et la demande à une seule session.

Dans ces exemples, un numéro de session est propre à son hôte. L’entrée suivante indique le même compte et le même numéro de session, quelques secondes plus tard.

```text
t=09:15:18Z source=sudo host=web-02 account=alex session=42 decision=allowed
```

![Terminal LabEx affichant des entrées simulées de web-01 et web-02 ainsi qu’une conversion à 09:15:10 UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-event-correlation/utc-correlation.png)

Le terminal affiche les trois entrées simulées et confirme la conversion en UTC avec la commande `date` d’Ubuntu.

:::single-choice{#security-event-correlation-host-scope} Quel est le rapport entre la troisième entrée et la session SSH initiale ?

::option[Elle appartient à la même session car le compte et l’heure concordent.]{#security-event-correlation-host-scope-account explanation="Deux hôtes peuvent enregistrer une activité sous le même nom de compte à quelques secondes d’intervalle."}
::option[Elle appartient à une autre session car l’hôte diffère.]{#security-event-correlation-host-scope-machine .correct explanation="La session 42 sur web-02 est propre à cet hôte. La connexion initiale a eu lieu sur web-01."}
::option[Elle appartient à cette session car le numéro de session est identique.]{#security-event-correlation-host-scope-session explanation="Dans cet exemple, le numéro n’a de sens que sur l’hôte correspondant. Les noms d’hôtes diffèrent."}
:::

## Dire ce que les entrées permettent d’affirmer

Sur `web-01`, la connexion a été acceptée et `sudo` a autorisé une commande pendant cette session. Voilà ce qu’établissent les entrées disponibles. Pour savoir si la commande a abouti, cherchez une entrée qui en donne le résultat. Une session peut contenir plusieurs commandes. Associez donc le résultat à la demande précise. En l’absence d’une entrée correspondante, le résultat reste inconnu.

:::single-choice{#security-event-correlation-completion-evidence} Quelle nouvelle entrée permettrait de savoir si la commande a réussi ?

::option[Le résultat d’une autre commande de la même session.]{#security-event-correlation-completion-other-command explanation="Une session peut contenir plusieurs commandes. Le résultat doit correspondre à la demande vérifiée."}
::option[Une seconde entrée indiquant que la demande a été autorisée.]{#security-event-correlation-completion-permission explanation="Cela confirme l’autorisation. Le résultat nécessite encore une entrée distincte."}
::option[Un résultat pour la commande visée par cette demande précise.]{#security-event-correlation-completion-result .correct explanation="Une entrée correspondante peut indiquer comment la commande s’est terminée."}
:::

Pour vous exercer à filtrer et à comparer d’autres traces d’authentification et de sudo, essayez l’[analyse des journaux système](https://labex.io/tutorials/linux-system-log-analysis-656124).

## Résumé

Vous savez maintenant utiliser plusieurs entrées pour formuler une conclusion et déterminer quoi vérifier ensuite.

1. Identifier le compte nommé dans un événement.
2. Convertir les horodatages dans un même fuseau avant de les comparer.
3. Utiliser ensemble l’hôte et la session pour rapprocher des activités.
4. Indiquer ce que les entrées établissent et rechercher la preuve qui manque.
