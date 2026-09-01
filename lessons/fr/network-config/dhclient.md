---
lesson_id: "dhclient"
course_id: "network-config"
lang: "fr"
order_index: 3
title: "dhclient"
description: "Découvrez quand et comment utiliser dhclient sans entrer en conflit avec le gestionnaire de réseau du système."
meta_title: "dhclient - Configuration réseau"
meta_description: "Découvrez comment dhclient obtient des adresses IP par DHCP et gère les baux réseau, ainsi que le rôle de dhclient.conf et dhclient.leases sous Linux."
meta_keywords: "dhclient, DHCP, réseau Linux, adresse IP, configuration réseau, tutoriel Linux, guide débutant"
---

`dhclient` est un client DHCP d’ISC présent sur certains systèmes Linux. De nombreuses installations actuelles laissent plutôt NetworkManager, systemd-networkd ou un autre service exécuter son propre client DHCP. Le démarrage d’un second client sur une interface déjà gérée peut créer des conflits d’adresses, de routes, de paramètres DNS et d’état des baux.

## Identifier le client actif

Avant d’appeler `dhclient`, examinez le gestionnaire de configuration et les processus :

```bash
$ nmcli device status
$ networkctl status
$ ps -ef | grep '[d]hclient'
```

Utilisez les outils présents sur l’hôte. Si un gestionnaire contrôle l’interface, demandez-lui d’effectuer la configuration DHCP au lieu de lancer un client distinct.

:::single-choice{#dhclient-second-client-risk} Pourquoi éviter de démarrer `dhclient` sur une interface déjà gérée ?

::option[DHCP ne peut attribuer que des adresses de boucle locale.]{#dhclient-loopback-only explanation="DHCP attribue couramment une configuration réseau qui ne concerne pas la boucle locale."}
::option[Deux clients peuvent entrer en concurrence pour les adresses, les routes, le DNS et les baux.]{#dhclient-competing-state .correct explanation="Normalement, seul le gestionnaire de configuration identifié doit réconcilier l’état de l’interface."}
::option[Chaque requête DHCP reformate le disque local.]{#dhclient-reformats explanation="Le protocole modifie l’état du réseau, et non le format du disque."}
:::

## Demander explicitement un bail

Sur une interface de test non gérée dont `dhclient` doit être le gestionnaire, indiquez l’interface et activez la sortie détaillée :

```bash
$ sudo dhclient -v enp1s0
```

Une exécution sans interface peut agir sur plusieurs interfaces admissibles. Les chemins des fichiers de configuration et de baux varient selon le paquet et l’appel ; les noms `dhclient.conf` et `dhclient.leases` sont courants, mais ne supposez pas qu’ils se trouvent toujours au même emplacement.

:::single-choice{#dhclient-interface-operand} Pourquoi préciser `enp1s0` dans une demande manuelle ?

::option[Pour ne viser que l’interface réseau voulue.]{#dhclient-scope-interface .correct explanation="Un appel du client sans qualification peut prendre en compte davantage d’interfaces que prévu."}
::option[Pour sélectionner le port TCP 1 pour DHCP.]{#dhclient-tcp-port explanation="DHCP emploie UDP, et le nom de l’interface n’est pas un port."}
::option[Pour rendre le bail permanent.]{#dhclient-permanent explanation="La configuration DHCP reste un état de bail limité dans le temps."}
:::

## Libérer un bail

`dhclient -r INTERFACE` demande la libération du bail et peut retirer une configuration utilisable. Cette opération est perturbatrice et ne garantit pas que le serveur soit accessible pour recevoir la demande. Ne libérez pas un bail simplement pour l’examiner, surtout sur le chemin d’une administration distante.

:::single-choice{#dhclient-release-effect} Quel est le risque opérationnel de `dhclient -r enp1s0` ?

::option[Cette commande ne fait qu’afficher le bail actuel sans rien modifier.]{#dhclient-release-readonly explanation="La libération est une action qui modifie l’état."}
::option[Elle renouvelle tous les baux pour une durée illimitée.]{#dhclient-release-renews explanation="La libération et le renouvellement sont des opérations opposées."}
::option[Elle peut supprimer la connectivité DHCP actuelle.]{#dhclient-release-connectivity .correct explanation="La procédure de libération abandonne l’état du bail et peut interrompre l’accès distant."}
:::

## Vérifier le bail appliqué

Après une demande contrôlée, ne vérifiez pas uniquement l’adresse :

```bash
$ ip address show dev enp1s0
$ ip route show
$ resolvectl status
```

Examinez les journaux du gestionnaire ou du client ainsi que la durée du bail, puis testez la résolution de noms et l’application voulues. Un message DHCPACK peut contenir des options incorrectes, et l’attribution réussie d’une adresse ne prouve pas que la passerelle ou le DNS soit accessible.

:::single-choice{#dhclient-verify-state} Que faut-il vérifier après l’obtention d’un bail ?

::option[L’adresse, les routes, le DNS, le bail et le comportement de l’application.]{#dhclient-complete-verify .correct explanation="Le bail configure plusieurs composants liés qui doivent fonctionner ensemble."}
::option[Uniquement qu’une chaîne représentant une adresse s’affiche.]{#dhclient-address-only explanation="Les routes, le DNS, la durée de vie et le fonctionnement de bout en bout peuvent encore être incorrects."}
::option[Uniquement l’arrière-plan du bureau.]{#dhclient-wallpaper explanation="L’apparence du bureau est sans rapport avec l’état DHCP."}
:::

## Résumé

Vous savez maintenant n’utiliser `dhclient` que lorsqu’il est le gestionnaire prévu d’une interface.

1. Identifier le gestionnaire de réseau et le client DHCP actifs.
2. Éviter les clients concurrents sur une même interface.
3. Limiter une demande manuelle à une interface de test nommée.
4. Considérer la libération comme une opération perturbatrice et vérifier l’ensemble du résultat du bail.
