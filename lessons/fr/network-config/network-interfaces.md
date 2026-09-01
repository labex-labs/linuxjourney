---
lesson_id: "network-interfaces"
course_id: "network-config"
lang: "fr"
order_index: 1
title: "Interfaces réseau"
description: "Découvrez comment examiner l’état, les adresses et les statistiques des interfaces Linux ainsi que la gestion de leur configuration persistante."
meta_title: "Interfaces réseau - Configuration réseau"
meta_description: "Guide des interfaces réseau Linux : commandes ip et ifconfig, état administratif et opérationnel, configuration persistante et fichiers Debian."
meta_keywords: "interface Linux, interface réseau Linux, etc network interfaces, interfaces Debian, ifconfig, commande ip, configuration réseau, réseau Linux"
---

Une interface réseau Linux relie un espace de noms réseau à un périphérique physique, une boucle locale, un pont, un tunnel, un périphérique virtuel ou un autre type de liaison. L’état de l’interface, ses adresses, ses routes, le DNS et sa configuration persistante sont liés, mais distincts.

## Découvrir les interfaces

Utilisez les outils modernes d’iproute2 :

```bash
$ ip -brief link show
$ ip -brief address show
```

Les interfaces peuvent porter des noms prévisibles dérivés du matériel tels que `enp1s0`, des noms traditionnels tels que `eth0` ou des noms définis par l’administrateur. Ne supposez jamais que `eth0` existe ou désigne un adaptateur particulier.

:::single-choice{#interfaces-name-assumption} Pourquoi un script doit-il découvrir les interfaces plutôt que supposer l’existence de `eth0` ?

::option[Chaque interface doit obligatoirement s’appeler `lo`.]{#interfaces-all-loopback explanation="La boucle locale est une interface particulière, et non le nom de chaque liaison."}
::option[Les systèmes Linux peuvent employer plusieurs conventions de nommage des interfaces.]{#interfaces-naming-varies .correct explanation="Les noms dérivés du matériel, virtuels ou personnalisés rendent l’hypothèse d’un nom fixe `eth0` peu fiable."}
::option[Les noms d’interfaces sont toujours des mots de passe distants.]{#interfaces-name-password explanation="Ces noms identifient des périphériques du noyau et ne constituent pas des identifiants secrets."}
:::

## État administratif et opérationnel

`UP` signifie que l’interface est activée administrativement. `LOWER_UP` indique généralement que la couche inférieure se déclare opérationnelle, par exemple lorsque la porteuse Ethernet est présente. Aucun de ces indicateurs, pris isolément, ne prouve qu’une adresse IP, une route, le DNS, le pare-feu ou un chemin applicatif fonctionne.

```bash
$ ip -details link show dev enp1s0
$ ip -s link show dev enp1s0
```

Les statistiques peuvent révéler des erreurs, des abandons et des compteurs, mais ces derniers ne deviennent significatifs qu’avec un intervalle de temps et une valeur de référence.

:::single-choice{#interfaces-up-limit} Qu’est-ce que l’état administratif `UP` ne prouve pas ?

::option[Que la connectivité de bout en bout fonctionne.]{#interfaces-up-not-connectivity .correct explanation="Des pannes peuvent subsister au niveau de la couche inférieure, de l’adressage, du routage, du filtrage, du nommage ou du service."}
::option[Que l’administrateur a activé l’interface.]{#interfaces-up-does-prove explanation="C’est précisément la signification directe de cet état."}
::option[Que l’interface possède un objet dans le noyau.]{#interfaces-up-kernel-object explanation="L’état affiché appartient à une interface existante du noyau."}
:::

## Modifier l’état d’exécution

Voici quelques commandes qui modifient l’état d’exécution :

```bash
$ sudo ip link set dev enp1s0 up
$ sudo ip address add 192.0.2.10/24 dev enp1s0
```

Ces changements affectent l’état actuel du noyau et peuvent entrer en conflit avec un gestionnaire de réseau qui réappliquera ensuite son profil. La désactivation d’une interface utilisée pour l’administration distante peut interrompre immédiatement l’accès. Avant de la modifier, vérifiez le périphérique exact, conservez un accès à la console, relevez l’état actuel et préparez un retour en arrière temporisé ou testé.

:::single-choice{#interfaces-ip-address-add-persistence} La commande `ip address add` garantit-elle à elle seule la persistance après un redémarrage ?

::option[Non ; le système de configuration actif doit également enregistrer ce paramètre.]{#interfaces-manager-persistence .correct explanation="NetworkManager, systemd-networkd, ifupdown ou un autre gestionnaire applique la politique persistante."}
::option[Oui, car chaque modification du noyau met à jour tous les profils des gestionnaires.]{#interfaces-runtime-always-persistent explanation="Les changements apportés à l’état d’exécution du noyau ne mettent pas systématiquement à jour la configuration persistante."}
::option[Uniquement lorsque l’adresse est une adresse IPv4 privée.]{#interfaces-private-persistent explanation="La portée de l’adresse ne rend pas une commande d’exécution persistante."}
:::

## Identifier le gestionnaire de la configuration

Les emplacements de configuration persistante varient selon les distributions et les installations. Il peut s’agir de profils NetworkManager, d’unités systemd-networkd, de fichiers d’entrée netplan, de `/etc/network/interfaces`, de cloud-init ou d’un système d’orchestration. Déterminez quel service gère le périphérique avant de modifier des fichiers :

```bash
$ systemctl --type=service --state=running | grep -E 'NetworkManager|networkd|networking'
$ networkctl status
$ nmcli device status
```

N’utilisez que les commandes disponibles pour le gestionnaire identifié. Deux gestionnaires contrôlant la même liaison peuvent entrer en concurrence et écraser mutuellement leur état.

:::single-choice{#interfaces-config-owner} Que faut-il faire avant de modifier durablement une interface ?

::option[Modifier tous les fichiers de configuration réseau possibles.]{#interfaces-edit-all explanation="Des définitions concurrentes créent des conflits et des réapplications imprévisibles."}
::option[Identifier le gestionnaire de réseau qui contrôle l’interface.]{#interfaces-identify-owner .correct explanation="La source de configuration et la méthode d’application correctes dépendent de ce gestionnaire."}
::option[Supprimer toutes les routes actuelles avant de les examiner.]{#interfaces-delete-routes explanation="Cette opération destructive peut supprimer l’accès nécessaire à la récupération."}
:::

## Vérifier une modification

Vérifiez l’état de la liaison, les adresses attribuées et leur durée de vie, les routes sélectionnées, l’état du résolveur, l’accessibilité des voisins et l’application réelle. Pour une modification persistante, ne testez un redémarrage contrôlé du service ou de l’hôte que si vous disposez d’une voie de récupération.

:::single-choice{#interfaces-change-verification} Quel élément fournit une preuve plus solide que la simple présence de la nouvelle adresse dans `ip address` ?

::option[Le nom de l’interface contient un chiffre.]{#interfaces-digit explanation="Le nommage ne fournit aucune validation de bout en bout."}
::option[L’invite du shell conserve la même couleur.]{#interfaces-prompt-color explanation="L’apparence du terminal est sans rapport avec le fonctionnement du réseau."}
::option[Les routes, l’état du résolveur et l’application prévue fonctionnent également.]{#interfaces-end-to-end .correct explanation="Une configuration utilisable dépend du chemin complet et du comportement du service."}
:::

## Résumé

Vous savez maintenant examiner et modifier une interface sans confondre l’état d’exécution et la politique persistante.

1. Découvrir les noms et les adresses réels des interfaces.
2. Distinguer l’état administratif de la connectivité opérationnelle.
3. Considérer les modifications directes avec `ip` comme l’état actuel du noyau.
4. Identifier le gestionnaire de configuration actif avant toute modification persistante.
5. Vérifier ensuite le routage, la résolution des noms et le comportement de l’application.
