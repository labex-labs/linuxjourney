---
lesson_id: "nat-network-address-translation"
course_id: "subnetting"
lang: "fr"
order_index: 6
title: "NAT"
description: "Découvrez comment la traduction de la source, de la destination et des ports modifie les flux IPv4 et l’état des connexions."
meta_title: "NAT - Sous-réseaux"
meta_description: "Découvrez le NAT sous Linux, son fonctionnement, les adresses IP privées et publiques et sa distinction avec la politique de sécurité."
meta_keywords: "NAT, traduction adresses réseau, réseau Linux, IP privée, IP publique, tutoriel Linux, guide débutant"
---

La traduction d’adresses réseau réécrit les champs d’adresses, et souvent les ports de transport, lorsque les paquets traversent un dispositif de traduction. Elle sert largement à relier des réseaux IPv4 adressés de manière privée au moyen d’un ensemble plus restreint d’adresses routables à l’extérieur.

## Traduction de la source

Le NAT source remplace l’adresse source d’un paquet lorsqu’il quitte un réseau. Les déploiements plusieurs-vers-un traduisent également les ports source afin que plusieurs flux internes puissent partager une adresse externe. Cette forme qui tient compte des ports est souvent appelée NAPT, PAT ou masquage lorsque l’adresse externe peut changer.

Le traducteur suit les associations afin de pouvoir réécrire les paquets de réponse vers le terminal interne d’origine. Il achemine normalement le même flux de transport ; il n’a pas besoin d’ouvrir une connexion proxy distincte comme le ferait un proxy applicatif.

:::single-choice{#nat-source-translation} Que modifie le NAT source sur un paquet sortant ?

::option[Uniquement les permissions de fichiers de l’application de destination.]{#nat-file-permissions explanation="Le NAT agit sur les en-têtes réseau et de transport, et non sur les systèmes de fichiers distants."}
::option[L’adresse source et, dans un usage plusieurs-vers-un, souvent le port source.]{#nat-source-fields .correct explanation="L’association permet de relier le trafic de retour au flux interne d’origine."}
::option[Le nom DNS enregistré définitivement par le client.]{#nat-dns-name explanation="La traduction ne réécrit pas la base des services de noms du client."}
:::

## Traduction de la destination

Le NAT de destination réécrit l’adresse ou le port de destination, généralement pour publier un service interne par un terminal externe. Une règle de redirection de port peut associer un port TCP externe à une autre adresse et un autre port internes. Le trafic de retour exige une traduction inverse cohérente.

:::single-choice{#nat-port-forward} Quelle forme de NAT met couramment en œuvre une redirection de port entrante ?

::option[Uniquement le NAT source avant la recherche de route.]{#nat-snat-port-forward explanation="La publication d’une destination interne exige une traduction des champs de destination."}
::option[Aucune traduction d’adresse ni de port.]{#nat-no-translation explanation="Une règle de redirection de port constitue par définition une politique de traduction."}
::option[Le NAT de destination.]{#nat-dnat .correct explanation="Le DNAT associe la destination externe au terminal de service interne sélectionné."}
:::

## NAT et politique du pare-feu

Le NAT n’est pas un pare-feu. Un traducteur avec état peut ne posséder aucune association pour un trafic entrant non sollicité, mais l’acheminement explicite, la traduction de destination, le filtrage et l’exposition de l’application déterminent ce qui est accessible. La politique de sécurité doit être exprimée et auditée par des règles de pare-feu, des services au moindre privilège et des contrôles de bout en bout plutôt que déduite de la réécriture des adresses.

:::single-choice{#nat-not-firewall} Pourquoi le NAT ne doit-il pas être considéré comme une politique de sécurité à lui seul ?

::option[Le NAT chiffre automatiquement chaque charge utile.]{#nat-encrypts explanation="La traduction d’adresses n’assure aucune confidentialité de la charge utile."}
::option[Les règles de traduction et les règles de filtrage du trafic ont des rôles différents.]{#nat-filter-separate .correct explanation="L’accessibilité et l’autorisation exigent un filtrage et une politique de service explicites même en présence de traduction."}
::option[Le NAT empêche les administrateurs de définir des règles de pare-feu.]{#nat-prevents-firewall explanation="La traduction et la politique de pare-feu coexistent couramment."}
:::

## Conséquences opérationnelles

Le NAT peut épuiser les associations d’adresses et de ports, compliquer les protocoles pair à pair, masquer les sources d’origine aux applications et nécessiter un traitement spécial des protocoles qui intègrent des adresses. Les journaux doivent conserver les horodatages et les détails des associations de traduction si les flux doivent être retracés.

Sous Linux, les politiques modernes se configurent couramment avec nftables et le suivi des connexions. Examinez le jeu de règles réel avant de le modifier :

```bash
$ sudo nft list ruleset
$ sudo conntrack -L
```

La deuxième commande exige les outils conntrack et des privilèges. Les modifications du jeu de règles peuvent interrompre l’accès distant ; employez donc un accès de récupération par la console, une configuration atomique, une validation et un retour en arrière.

:::single-choice{#nat-trace-flow} Quel indice est nécessaire pour retrouver le client interne à l’origine d’un flux qui partage une adresse ?

::option[Uniquement l’adresse externe, sans heure ni port.]{#nat-address-only explanation="De nombreux clients et flux peuvent partager cette adresse."}
::option[Uniquement le nom d’hôte affiché du client.]{#nat-hostname-only explanation="Le traducteur associe des tuples de paquets, et pas nécessairement des noms d’hôtes."}
::option[Une association de traduction corrélée dans le temps qui comprend le protocole et les ports.]{#nat-correlated-mapping .correct explanation="Le tuple complet et l’horodatage distinguent les flux traduits simultanés."}
:::

## Résumé

Vous savez maintenant distinguer la traduction d’adresses du routage, des proxys et de la politique du pare-feu.

1. Identifier la traduction de la source sur les flux sortants.
2. Identifier la traduction de la destination dans les services publiés.
3. Comprendre comment les associations de ports permettent le partage des adresses.
4. Appliquer un filtrage explicite au lieu de considérer le NAT comme une sécurité.
5. Préserver les indices d’association et l’accès de récupération pendant les changements.
