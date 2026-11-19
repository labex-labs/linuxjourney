---
lesson_id: "linux-host-firewalls"
course_id: "linux-hardening"
lang: "fr"
order_index: 5
title: "Pare-feu d’hôte"
description: "Apprenez à lire une politique simple de pare-feu d’hôte et à prévoir des contrôles depuis les emplacements pertinents."
meta_title: "Pare-feu d’hôte - Durcissement de Linux"
meta_description: "Apprenez à lire une politique simple de pare-feu d’hôte et à prévoir des contrôles depuis les emplacements pertinents."
meta_keywords: "pare-feu d’hôte, durcissement de Linux, cybersécurité, Linux Journey"
---

Un **pare-feu d’hôte** peut autoriser ou bloquer le trafic réseau entrant selon des critères tels que l’adresse source, le protocole et le port de destination. Déterminez d’abord le trafic dont le service a besoin.

## Lire un exemple de politique

La politique simplifiée suivante s’applique à un seul hôte. La barre oblique dans `192.0.2.0/24` indique une plage d’adresses IPv4. Dans cet exemple, `192.0.2.44` appartient à cette plage, tandis que `198.51.100.8` se situe en dehors.

```text
Allow TCP port 443 from any source.
Allow TCP port 22 from 192.0.2.0/24.
Deny other new inbound connections.
```

Le port 443 dessert le site public. Le port 22 est réservé au réseau de maintenance. La règle par défaut s’applique aux connexions qui ne correspondent à aucune des deux autorisations.

:::single-choice{#linux-host-firewalls-match-trusted-network} Quelle nouvelle connexion correspond à la règle de maintenance ?

::option[Port TCP 22 depuis 198.51.100.8.]{#linux-host-firewalls-match-trusted-network-b explanation="Le port correspond, mais la source se trouve en dehors du réseau de maintenance."}
::option[Port TCP 443 depuis 192.0.2.44.]{#linux-host-firewalls-match-trusted-network-c explanation="Cette connexion correspond à la règle du site public."}
::option[Port TCP 22 depuis 192.0.2.44.]{#linux-host-firewalls-match-trusted-network-a .correct explanation="Le port de destination et la plage source correspondent tous deux."}
:::

![Politique simulée de pare-feu d’hôte avec accès HTTPS public et accès de maintenance restreint](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-host-firewalls/sample-policy.png)

## Vérifier les règles et l’écoute

Une connexion autorisée peut échouer si aucun programme n’est à l’écoute. De même, un programme qui écoute correctement peut être inaccessible par un chemin bloqué par le pare-feu. Lisez les règles et vérifiez séparément que le programme écoute.

:::single-choice{#linux-host-firewalls-allowed-but-failed} La règle autorise le port 443, mais aucun programme n’y écoute sur l’hôte. Que devez-vous vérifier ?

::option[Si le client doit utiliser l’accès SSH de maintenance.]{#linux-host-firewalls-allowed-but-failed-a explanation="Il s’agit d’un autre service."}
::option[Si le service web public écoute sur le port attendu.]{#linux-host-firewalls-allowed-but-failed-b .correct explanation="Une autorisation du pare-feu ne met aucun programme à l’écoute."}
::option[Si la requête provient du réseau de maintenance.]{#linux-host-firewalls-allowed-but-failed-c explanation="La règle publique accepte toutes les sources dans cet exemple."}
:::

## Prévoir une vérification sûre

Lorsque vous vérifiez une modification contrôlée, gardez un accès de maintenance légitime à disposition. Testez l’accès autorisé depuis le réseau de maintenance. Vérifiez qu’une tentative depuis un emplacement approuvé en dehors de ce réseau est bloquée. Notez la source, la cible et le résultat attendu pour chaque test.

:::single-choice{#linux-host-firewalls-verification-pair} Quelle paire de contrôles vérifie la restriction SSH prévue ?

::option[Un contrôle autorisé du port 22 depuis l’intérieur et depuis l’extérieur du réseau de maintenance.]{#linux-host-firewalls-verification-pair-c .correct explanation="Ces tentatives vérifient les deux cas prévus par la politique."}
::option[Deux connexions SSH depuis la même machine autorisée.]{#linux-host-firewalls-verification-pair-a explanation="Vous vérifieriez deux fois le cas autorisé."}
::option[Deux requêtes du navigateur vers la page d’accueil publique.]{#linux-host-firewalls-verification-pair-b explanation="Elles testent le port public et laissent l’accès de maintenance sans contrôle."}
:::

## Résumé

Vous savez maintenant examiner les règles du pare-feu d’hôte en tenant compte de l’état du service.

1. Identifiez la règle qui correspond au protocole, à la destination et à la source.
2. Vérifiez que le service autorisé est à l’écoute.
3. Vérifiez à la fois l’accès prévu et la restriction prévue.
