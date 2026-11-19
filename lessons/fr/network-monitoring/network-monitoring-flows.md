---
lesson_id: "network-monitoring-flows"
course_id: "network-monitoring"
lang: "fr"
order_index: 2
title: "Flux réseau"
description: "Apprenez à lire les adresses, les ports, les horaires et les volumes d’octets dans un résumé de flux."
meta_title: "Flux réseau - Supervision réseau"
meta_description: "Apprenez à lire les adresses, les ports, les horaires et les volumes d’octets dans un résumé de flux."
meta_keywords: "flux réseau, supervision réseau, cybersécurité, Linux Journey"
---

Un **flux** regroupe du trafic qui partage des propriétés telles que les adresses réseau, les ports et le protocole. Les outils de supervision peuvent compter les octets ou les paquets d’un flux sans en conserver le contenu complet.

## Lire les deux extrémités

Dans ce résumé simulé, le collecteur consigne un sens de circulation de la source vers la destination. Les protocoles de transport tels que TCP utilisent des numéros de port qui peuvent aider à identifier un service à l’écoute du côté destinataire.

```text
start=09:21:00Z protocol=TCP src=192.0.2.10:51600 dst=192.0.2.20:443 bytes=1800
start=09:21:00Z protocol=TCP src=192.0.2.20:443 dst=192.0.2.10:51600 bytes=8200
```

La première ligne correspond au trafic vers le port 443. La seconde indique le sens inverse. Certains collecteurs regroupent les deux sens, alors vérifiez le format que vous lisez.

:::single-choice{#network-monitoring-flows-endpoint-direction} Dans la première ligne, quels sont l’adresse et le port qui reçoivent le trafic enregistré ?

::option[192.0.2.10:51600.]{#network-monitoring-flows-endpoint-direction-a explanation="C’est l’extrémité émettrice dans le premier sens."}
::option[Les deux extrémités indiquées comme destinations.]{#network-monitoring-flows-endpoint-direction-c explanation="Chaque ligne de cet exemple consigne un seul sens."}
::option[192.0.2.20:443.]{#network-monitoring-flows-endpoint-direction-b .correct explanation="Le champ de destination indique où le trafic a été envoyé."}
:::

## Comparer les volumes

L’exemple montre davantage d’octets dans le sens qui part du port 443. Une réponse plus volumineuse peut être normale pour une page web. Le volume seul ne révèle ni le contenu de la page, ni le compte, ni la raison de ce volume.

:::single-choice{#network-monitoring-flows-byte-count} Que décrivent les 8 200 octets de la seconde ligne ?

::option[Le texte exact du message de réponse.]{#network-monitoring-flows-byte-count-b explanation="Le résumé du flux donne un volume et omet le message."}
::option[Le volume enregistré dans ce sens.]{#network-monitoring-flows-byte-count-a .correct explanation="Le nombre d’octets résume le trafic. La source et la destination indiquent son sens."}
::option[La certitude que la page s’est chargée correctement.]{#network-monitoring-flows-byte-count-c explanation="Le volume n’indique pas le résultat HTTP."}
:::

## Ajouter du contexte

Appuyez-vous sur l’heure et les informations dont vous disposez sur le service pour déterminer quels flux sont pertinents. Pour savoir ce que le serveur web a renvoyé, consultez ses journaux d’accès à la même heure et, si possible, pour la même connexion.

:::single-choice{#network-monitoring-flows-next-source} Vous cherchez le statut HTTP de la requête web. Quelle autre source serait utile ?

::option[Une entrée correspondante du journal d’accès web.]{#network-monitoring-flows-next-source-c .correct explanation="Une entrée du journal d’accès du serveur peut donner le résultat HTTP."}
::option[Le nombre d’octets du flux arrondi à la centaine la plus proche.]{#network-monitoring-flows-next-source-a explanation="L’arrondi modifie la précision sans fournir le statut de la réponse."}
::option[Un autre résumé de flux pour les mêmes extrémités.]{#network-monitoring-flows-next-source-b explanation="Un autre résumé peut confirmer d’autres observations de trafic. En général, il ne donne pas le statut de la réponse HTTP."}
:::

## Résumé

Vous savez maintenant lire les principaux champs d’un résumé de flux.

1. Repérez les adresses et les ports aux deux extrémités.
2. Interprétez le volume d’octets dans le sens indiqué.
3. Consultez une autre source si vous avez besoin du résultat au niveau de l’application.
