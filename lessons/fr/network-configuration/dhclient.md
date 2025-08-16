---
lang: "fr"
title: "dhclient"
description: "Découvrez dhclient, comment il obtient des adresses IP en utilisant DHCP et gère les baux réseau. Comprenez les fichiers dhclient.conf et dhclient.leases. Guide pour débutants Linux."
keywords: "dhclient, DHCP, réseau Linux, adresse IP, configuration réseau, tutoriel Linux, guide du débutant"
---

## Lesson Content

Nous avons déjà parlé de DHCP, et le plus souvent, vous n'aurez jamais besoin de définir statiquement vos adresses IP, masques de sous-réseau, etc. Au lieu de cela, vous utiliserez DHCP ! Le `dhclient` démarre au démarrage et obtient une liste des interfaces réseau à partir du fichier `dhclient.conf`. Pour chaque interface listée, il essaie de configurer l'interface en utilisant le protocole DHCP.

Dans le fichier `dhclient.leases`, `dhclient` garde une trace d'une liste de baux à travers les redémarrages du système. Après avoir lu `dhclient.conf`, le fichier `dhclient.leases` est lu pour lui faire savoir quels baux il a déjà attribués.

### Pour obtenir une nouvelle IP

```bash
sudo dhclient
```

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Qu'est-ce qui essaie d'attribuer des adresses IP avec le protocole DHCP ?

## Quiz Answer

dhclient
