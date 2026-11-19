---
lesson_id: "linux-audit-logs"
course_id: "system-auditing"
lang: "fr"
order_index: 2
title: "Journaux d’audit Linux"
description: "Apprenez à regrouper les entrées d’audit Linux qui décrivent une même opération enregistrée."
meta_title: "Journaux d’audit Linux - Audit système"
meta_description: "Apprenez à regrouper les entrées d’audit Linux qui décrivent une même opération enregistrée."
meta_keywords: "journaux d’audit Linux, audit système, cybersécurité, Linux Journey"
---

Linux Audit peut écrire plusieurs entrées sur un même événement. Une ligne peut décrire l’opération, tandis qu’une autre fournit un chemin. Regroupez les lignes liées avant d’interpréter ce qu’elles indiquent.

## Repérer l’événement commun

Les valeurs ci-dessous sont des entrées d’exercice abrégées du même hôte et de la même date. Le nombre qui suit les deux-points dans la référence d’audit aide à regrouper les entrées portant le même horodatage et le même identifiant d’événement. Ces lignes appartiennent au même événement.

```text
type=SYSCALL msg=audit(1763456400.120:42) success=yes auid=1001 euid=0
type=PATH    msg=audit(1763456400.120:42) name="/etc/journey/site.conf"
```

La première ligne indique le résultat et les champs relatifs au compte. La ligne du chemin nomme un fichier associé à l’événement.

:::single-choice{#linux-audit-logs-group-rows} Quelles données permettent de relier l’opération au chemin dans cet exemple ?

::option[Les deux types d’entrées SYSCALL et PATH, à eux seuls.]{#linux-audit-logs-group-rows-a explanation="Ces types décrivent le rôle de chaque ligne. De nombreux événements peuvent contenir les mêmes types."}
::option[Le fait que les deux lignes commencent par type.]{#linux-audit-logs-group-rows-c explanation="Chaque ligne peut avoir un type tout en décrivant un événement différent."}
::option[La même référence d’audit sur le même hôte.]{#linux-audit-logs-group-rows-b .correct explanation="Cette référence regroupe les lignes qui décrivent l’événement 42."}
:::

![Lignes simulées SYSCALL et PATH de Linux Audit portant la même référence d’événement](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/linux-audit-logs/grouped-event.png)

## Lire les deux identités

Dans cet exemple, `auid` est l’identifiant d’audit de l’utilisateur à l’origine de la session et `euid` est l’identifiant utilisateur effectif pour l’action. Un programme peut utiliser une identité effective différente de celle de connexion. Un identifiant numérique désigne un compte sur l’hôte. D’autres entrées peuvent être nécessaires pour savoir qui utilisait ce compte.

:::single-choice{#linux-audit-logs-identify-login} Quel champ indique l’identité de connexion enregistrée par l’audit dans cet exemple ?

::option[Euid 0.]{#linux-audit-logs-identify-login-b explanation="Il donne l’identité effective du programme pour cet événement."}
::option[Auid 1001.]{#linux-audit-logs-identify-login-a .correct explanation="Auid désigne l’identité de connexion dans l’audit et euid désigne l’identité effective."}
::option[Le numéro d’événement 42.]{#linux-audit-logs-identify-login-c explanation="Ce numéro regroupe les entrées et ne désigne aucun compte."}
:::

## Limiter le constat aux faits observés

Le champ du résultat indique que l’opération enregistrée a réussi. Consultez l’événement entier pour identifier l’opération. Pour savoir si le contenu a changé, comparez le fichier à une référence connue.

:::single-choice{#linux-audit-logs-useful-follow-up} Qu’est-ce qui permettrait de savoir si le contenu diffère de celui du fichier approuvé ?

::option[Une comparaison avec une copie de référence approuvée ou une référence d’intégrité.]{#linux-audit-logs-useful-follow-up-c .correct explanation="Ces éléments peuvent montrer ce qui a changé dans le fichier."}
::option[Une deuxième entrée d’audit qui signale une autre opération réussie.]{#linux-audit-logs-useful-follow-up-a explanation="Elle peut établir une autre action enregistrée. Les octets actuels du fichier restent à comparer à la copie approuvée."}
::option[L’identifiant du compte de connexion dans le même événement.]{#linux-audit-logs-useful-follow-up-b explanation="Il précise le compte concerné. Il ne décrit aucun changement des octets du fichier."}
:::

## Résumé

Vous savez maintenant regrouper les entrées pour lire un événement d’audit.

1. Associez les entrées à l’aide de l’hôte et de la référence d’événement d’audit.
2. Lisez séparément l’identité de connexion et l’identité effective.
3. Choisissez une vérification si le résultat enregistré laisse une question ouverte.
