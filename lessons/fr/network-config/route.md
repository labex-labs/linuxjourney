---
index: 2
lang: "fr"
title: "route"
meta_title: "route - Configuration Réseau"
meta_description: "Apprenez à gérer votre table de routage Linux. Ce guide couvre l'ajout et la suppression de routes réseau en utilisant la commande moderne 'ip route' et la commande héritée 'route'."
meta_keywords: "commande ip route linux, commande ip route, ajouter route, supprimer route, table de routage, routage réseau, réseau linux, ip route"
---

## Lesson Content

Sous Linux, la table de routage dirige le trafic réseau vers sa destination correcte. Bien que nous ayons précédemment discuté de la visualisation de cette table, vous pouvez également ajouter ou supprimer manuellement des routes pour contrôler la manière dont les paquets de données sont transférés. Ceci est essentiel pour configurer des configurations réseau complexes ou pour dépanner des problèmes de connectivité.

### Utilisation de la commande legacy route

La commande `route` est un outil traditionnel pour gérer la table de routage. Bien qu'elle soit toujours fonctionnelle, elle est considérée comme obsolète et la commande `ip` est désormais préférée.

Pour ajouter une nouvelle route réseau, vous spécifiez l'adresse réseau, le masque de sous-réseau et la passerelle (`gw`) :

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

Pour supprimer une route, utilisez l'indicateur `del` avec l'adresse réseau :

```bash
sudo route del -net 192.168.2.1/23
```

### Gestion moderne des routes avec ip route

La commande `ip route` est l'outil moderne et plus puissant pour la configuration réseau sous Linux. Elle offre un ensemble d'options plus cohérent et plus étendu pour gérer les interfaces réseau et les routes. L'utilisation de la **commande ip route linux** est la pratique recommandée pour les systèmes actuels.

Pour ajouter une route avec la **commande ip route sous linux**, vous utilisez l'action `add`, en spécifiant le réseau de destination et le saut suivant via la passerelle :

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

Pour supprimer une route, vous pouvez utiliser l'action `delete`. Vous pouvez spécifier la route en entier ou seulement le réseau de destination si elle est unique :

```bash
# Supprimer en spécifiant la route complète
ip route delete 192.168.2.1/23 via 10.11.12.3

# Ou, supprimer en spécifiant seulement la destination
ip route delete 192.168.2.1/23
```

Maîtriser la commande `ip route` est une compétence clé pour tout administrateur Linux responsable de la gestion du réseau.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du routage réseau et de l'adressage IP :

1. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Entraînez-vous à configurer une IP statique, à définir une passerelle par défaut et à vérifier la configuration réseau à l'aide de la commande `ip`.
2. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment la passerelle par défaut gère le trafic distant et observez les interactions de la couche réseau.

Ces laboratoires vous aideront à appliquer les concepts d'adressage IP et de routage dans des scénarios réels et à gagner en confiance avec le réseau Linux.

## Quiz Question

When using the legacy `route` command, what is the flag used to delete a route? Please answer in English, paying attention to case.

## Quiz Answer

del
