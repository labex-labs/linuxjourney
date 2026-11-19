---
lesson_id: "security-events"
course_id: "security-logs"
lang: "fr"
order_index: 1
title: "Événements de sécurité"
description: "Apprenez à distinguer un événement de sécurité, le journal qui en garde la trace et l’alerte qui invite à l’examiner."
meta_title: "Événements de sécurité - Journaux de sécurité"
meta_description: "Lisez une entrée de sécurité Linux, comparez-la à une alerte et choisissez quoi vérifier lorsque les journaux disponibles ne suffisent pas."
meta_keywords: "événements de sécurité, journaux de sécurité, entrées de journal, alertes, journaux Linux"
---

Un serveur signale un échec de connexion. Que s’est-il passé ? Que pouvez-vous en déduire ? Commencez par faire la différence entre ce que la machine a enregistré et les conclusions que vous pourriez en tirer.

## Événements et entrées de journal

Un **événement** est un fait qui s’est produit, par exemple le rejet d’une tentative de connexion. Une **entrée de journal** en conserve une description. Un **journal** regroupe ces entrées. Pour faciliter la lecture, ce cours utilise des exemples simulés dont les noms de champs sont uniformes. Les outils réels nomment et conservent leurs entrées de différentes façons.

```text
t=08:55:00Z source=ssh host=web-01 account=alex login=rejected
```

Cette entrée indique qu’une tentative de connexion à distance pour le compte `alex` a été refusée. Vous pouvez lire l’entrée après la tentative. D’autres leçons montreront comment comparer les horodatages de plusieurs sources.

![Terminal LabEx affichant une entrée simulée de connexion SSH refusée pour alex sur web-01](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-events/event-fields.png)

Le terminal LabEx affiche la même entrée simulée à partir d’un fichier texte.

:::single-choice{#security-events-event-versus-record} Dans cet exemple, qu’est-ce qui constitue l’événement lui-même ?

::option[La ligne enregistrée qui décrit le refus.]{#security-events-event-line explanation="La ligne est l’entrée que vous pouvez lire après l’événement."}
::option[La consultation ultérieure de la ligne enregistrée.]{#security-events-event-review explanation="La lecture intervient plus tard. L’événement décrit est le refus de connexion."}
::option[La tentative de connexion a été refusée.]{#security-events-event-attempt .correct explanation="Le refus a eu lieu sur le serveur. Le journal conserve la trace de ce qui s’est passé."}
:::

## Lire les champs

Un **champ** contient une information de l’entrée. Dans ces exemples, `t` donne l’heure enregistrée, `host` désigne la machine où l’événement est survenu et `source` indique l’outil qui l’a signalé. Le champ `account` indique le compte et `login` donne le résultat de la tentative.

:::single-choice{#security-events-field-host} Vous voulez savoir quelle machine a enregistré le refus de connexion. Quelle valeur l’identifie ?

::option[`alex`, dans le champ account.]{#security-events-field-host-account explanation="Account désigne le compte concerné par la tentative."}
::option[`web-01`, dans le champ host.]{#security-events-field-host-web .correct explanation="Host désigne la machine sur laquelle l’événement s’est produit."}
::option[`ssh`, dans le champ source.]{#security-events-field-host-tool explanation="Source identifie l’outil qui a signalé l’événement."}
:::

## Alertes et règles

Une **alerte** attire l’attention sur une situation qui peut mériter un examen. Une règle de supervision peut déclencher une alerte après trois tentatives refusées pour le même compte sur le même hôte en cinq minutes. Elle regroupe les entrées par compte, hôte et période. L’alerte indique que les conditions sont remplies. Il peut s’agir d’une personne qui a saisi plusieurs fois un mauvais mot de passe.

:::single-choice{#security-events-alert-interpretation} La règle signale trois échecs pour alex sur web-01. Que permet d’affirmer l’alerte ?

::option[Les échecs enregistrés remplissent les conditions prévues par la règle.]{#security-events-alert-condition .correct explanation="L’alerte signale une série d’événements à examiner. La règle n’identifie pas la personne à l’origine des tentatives."}
::option[Trois personnes différentes ont essayé de se connecter.]{#security-events-alert-people explanation="Les trois tentatives peuvent provenir d’une ou de plusieurs personnes. La règle compte des entrées."}
::option[Quelqu’un a réussi à se connecter après trois tentatives.]{#security-events-alert-success explanation="La règle compte les connexions refusées. Elle ne fournit aucun résultat sur une éventuelle connexion ultérieure."}
:::

## Choisir quoi vérifier ensuite

Pour savoir si `alex` s’est connecté plus tard, cherchez sur `web-01` un résultat de connexion postérieur aux échecs. Vérifiez d’abord la période couverte. Un export de journal ne contient qu’une sélection d’entrées et peut s’arrêter avant la période recherchée.

:::single-choice{#security-events-next-record} Votre export s’arrête à 09:00. Vous devez vérifier s’il y a eu une connexion réussie à 09:05. Que devriez-vous chercher ?

::option[Le même export trié du plus récent au plus ancien.]{#security-events-next-sort explanation="Le tri change l’ordre. Il ne peut pas ajouter d’entrées après 09:00."}
::option[Les entrées de connexion de web-01 pour une période qui inclut 09:05.]{#security-events-next-window .correct explanation="Vous avez besoin de la bonne source et d’une période contenant l’événement à vérifier."}
::option[Un nouveau décompte des échecs avant 09:00.]{#security-events-next-count explanation="Ce décompte concerne un autre résultat et une période antérieure."}
:::

## Résumé

Vous savez maintenant lire une entrée de sécurité et choisir la prochaine vérification après une alerte.

1. Distinguer un événement de la ligne qui le consigne.
2. Repérer le compte, l’hôte et le résultat dans un exemple.
3. Utiliser la règle d’alerte pour savoir ce qui a été observé.
4. Vérifier que la source et la période permettent de répondre à la question.
