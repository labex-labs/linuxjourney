---
lesson_id: "security-session-records"
course_id: "security-logs"
lang: "fr"
order_index: 4
title: "Journaux de sessions"
description: "Apprenez à associer les entrées d’ouverture et de fermeture et à déterminer de quelles sessions parle un extrait de journal."
meta_title: "Journaux de sessions - Journaux de sécurité"
meta_description: "Lisez les entrées de session Linux, associez une fermeture à son ouverture et choisissez quoi vérifier si la fermeture manque."
meta_keywords: "journaux de sessions Linux, ouverture de session, fermeture de session, identifiant de session, conservation des journaux"
---

Une vérification d’authentification réussie confirme que quelqu’un a pu se connecter avec un compte. Une **session** est la période d’activité qui suit la connexion et se termine lorsque l’utilisateur ferme la session ou se déconnecte. Les journaux indiquent le début et la fin de cette période si les deux événements ont été enregistrés.

## Lire une entrée d’ouverture

Le système peut attribuer un **identifiant de session** pour distinguer une session sur une machine. Ces lignes simulées montrent deux ouvertures par le même compte sur `web-01`. Toutes les heures de cette leçon sont dans le même fuseau horaire.

```text
t=09:14:05Z source=session host=web-01 account=alex session=42 state=opened
t=09:17:00Z source=session host=web-01 account=alex session=43 state=opened
```

La première ligne signale le début de la session 42. La seconde signale une autre session, la 43, sur le même hôte.

:::single-choice{#security-session-records-two-openings} Quelle affirmation les deux ouvertures étayent-elles ?

::option[La première session a pris fin au début de la deuxième.]{#security-session-records-open-ended explanation="La deuxième ouverture signale le début d’une autre session. Elle ne donne aucune heure de fin pour la première."}
::option[Deux comptes différents se sont connectés à l’hôte.]{#security-session-records-open-accounts explanation="Les deux lignes indiquent le même compte. Le champ de session permet de distinguer les deux périodes d’activité."}
::option[Le même compte a ouvert deux sessions distinctes.]{#security-session-records-open-two .correct explanation="Les deux lignes indiquent alex et chacune contient son propre identifiant de session sur web-01."}
:::

## Associer une ouverture à une fermeture

Lisez l’hôte et l’identifiant de session ensemble avant d’associer deux entrées. Comparez la ligne de fermeture ci-dessous aux entrées d’ouverture.

```text
t=09:20:05Z source=session host=web-01 account=alex session=42 state=closed
```

Sur `web-01`, les entrées d’ouverture et de fermeture de la session 42 sont espacées de six minutes. Elles donnent le début et la fin enregistrés. Elles n’énumèrent pas les actions effectuées entre les deux.

![Terminal LabEx affichant les ouvertures simulées des sessions 42 et 43 ainsi que la fermeture de la session 42](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-session-records/session-records.png)

Cette vue montre ensemble les entrées simulées d’ouverture et de fermeture.

:::single-choice{#security-session-records-pair-ids} Supposons que la ligne de fermeture indique plutôt `session=43`, avec le même hôte et la même heure. Quand cette session a-t-elle commencé ?

::option[À 09:14:05.]{#security-session-records-pair-forty-two explanation="Cette entrée d’ouverture indique le même compte, mais elle concerne la session 42."}
::option[À 09:17:00.]{#security-session-records-pair-forty-three .correct explanation="En associant web-01 à la session 43, on trouve la deuxième ouverture, à 09:17:00."}
::option[À 09:20:05.]{#security-session-records-pair-end-time explanation="C’est l’heure de fermeture enregistrée. Pour l’heure de début, lisez l’entrée d’ouverture correspondante."}
:::

## Vérifier une fermeture manquante

Revenez à l’entrée d’origine, qui clôt la session 42. L’extrait s’arrête à 09:21 et ne contient aucune fermeture pour la session 43. Celle-ci pouvait être encore active à la fin de l’extrait. Il se peut aussi que l’entrée de fermeture soit hors de la période disponible ou qu’elle manque à cette source. La **durée de conservation** indique combien de temps une entrée de journal reste stockée et consultable.

:::single-choice{#security-session-records-missing-close} Que pouvez-vous dire de la session 43 d’après le seul extrait ?

::option[Elle était encore active à la fin de l’extrait.]{#security-session-records-missing-active explanation="C’est possible, mais l’absence de fermeture ne suffit pas pour connaître son état."}
::option[L’extrait ne contient pas d’heure de fermeture pour cette session.]{#security-session-records-missing-unknown .correct explanation="Cela décrit le contenu disponible. Une source ultérieure ou différente peut donner l’heure manquante."}
::option[Elle a été fermée en même temps que la session 42.]{#security-session-records-missing-together explanation="L’entrée de fermeture concerne la session 42. Aucune fermeture n’est associée à la 43 dans cet extrait."}
:::

## Choisir la source en fonction de la question

Pour retrouver une ancienne heure de fermeture, cherchez l’entrée correspondante dans un extrait plus récent du même hôte. Pour savoir si la session est encore active, consultez la liste actuelle des sessions de cet hôte. Un journal enregistré et une liste actuelle répondent à des questions sur des moments différents.

:::single-choice{#security-session-records-current-status} Vous devez savoir si la session 43 est encore active. Quelle source est la plus utile ?

::option[Une liste actuelle des sessions sur web-01.]{#security-session-records-current-list .correct explanation="La liste indique les sessions que l’hôte signale comme actives à cet instant."}
::option[Une copie ancienne de l’entrée d’ouverture.]{#security-session-records-current-opening explanation="Elle indique que la session a commencé. Elle ne dit pas si elle est toujours active."}
::option[Une entrée de fermeture de la session 42 sur web-01.]{#security-session-records-current-other explanation="La fermeture d’une autre session ne répond pas à la question sur la session 43."}
:::

## Résumé

Vous savez maintenant utiliser les journaux pour décrire le début et la fin enregistrés d’une session.

1. Repérer une ouverture avec son hôte et son identifiant de session.
2. Associer une fermeture à la bonne ouverture.
3. Nommer ce que laisse en suspens une fermeture manquante.
4. Choisir entre des entrées historiques et une liste actuelle de sessions.
