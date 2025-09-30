---
index: 2
lang: "fr"
title: "route"
meta_title: "route - Configuration Réseau"
meta_description: "Apprenez à ajouter et supprimer des routes réseau à l'aide des commandes Linux route et ip. Comprenez la gestion de la table de routage pour les utilisateurs débutants et intermédiaires."
meta_keywords: "commande route, ip route, ajouter route, supprimer route, réseau Linux, table de routage, tutoriel Linux, guide débutant"
---

## Lesson Content

Nous avons déjà discuté de la visualisation de nos tables de routage avec la commande `route`. Si vous souhaitez ajouter ou supprimer des routes, vous pouvez le faire manuellement.

### Ajouter une nouvelle route

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### Supprimer une route

```bash
sudo route del -net 192.168.2.1/23
```

Vous pouvez également effectuer ces modifications avec la commande **ip** :

### Pour ajouter une route

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### Pour supprimer une route

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du routage réseau et de l'adressage IP :

1. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Entraînez-vous à configurer une IP statique, à définir une passerelle par défaut et à vérifier la configuration réseau à l'aide de la commande `ip`.
2. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment la passerelle par défaut gère le trafic distant et observez les interactions de la couche réseau.

Ces laboratoires vous aideront à appliquer les concepts d'adressage IP et de routage dans des scénarios réels et à renforcer votre confiance en matière de mise en réseau Linux.

## Quiz Question

Quel est le drapeau de commande pour supprimer une route ?

## Quiz Answer

del
