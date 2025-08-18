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

Il n'y a pas d'exercices pour cette leçon, mais vous pouvez lire plus d'informations sur les commandes discutées ici dans les pages de manuel.

```bash
man route
```

```bash
man ip-route
```

## Quiz Question

Quel est le drapeau de commande pour supprimer une route ?

## Quiz Answer

del
