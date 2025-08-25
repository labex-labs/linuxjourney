---
index: 3
lang: "fr"
title: "dhclient"
meta_title: "dhclient - Configuration réseau"
meta_description: "Découvrez dhclient, comment il obtient des adresses IP en utilisant DHCP et gère les baux réseau. Comprenez les fichiers dhclient.conf et dhclient.leases. Guide pour débutants Linux."
meta_keywords: "dhclient, DHCP, réseau Linux, adresse IP, configuration réseau, tutoriel Linux, guide du débutant"
---

## Lesson Content

Nous avons déjà discuté du DHCP, et le plus souvent, vous n'aurez jamais besoin de définir statiquement vos adresses IP, masques de sous-réseau, etc. Au lieu de cela, vous utiliserez le DHCP ! Le `dhclient` démarre au démarrage et obtient une liste d'interfaces réseau à partir du fichier `dhclient.conf`. Pour chaque interface listée, il essaie de configurer l'interface en utilisant le protocole DHCP.

Dans le fichier `dhclient.leases`, `dhclient` garde une trace d'une liste de baux à travers les redémarrages du système. Après avoir lu `dhclient.conf`, le fichier `dhclient.leases` est lu pour lui faire savoir quels baux il a déjà attribués.

### Pour obtenir une nouvelle IP

```bash
sudo dhclient
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage IP dynamique et de la configuration réseau :

1. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/linux-manage-ip-addressing-in-linux-592736)** - Entraînez-vous à utiliser `dhclient` pour obtenir une adresse IP dynamique et vérifier la configuration réseau dans un environnement Linux réel.
2. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Apprenez à inspecter les interfaces réseau et à identifier les adresses MAC et IP, qui sont fondamentales pour comprendre comment le DHCP attribue les adresses.
3. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Testez la joignabilité du réseau et explorez différents types d'adresses IP, en approfondissant votre compréhension du fonctionnement des adresses IP dans un réseau.

Ces laboratoires vous aideront à appliquer les concepts de DHCP et d'adressage IP dans des scénarios réels et à renforcer votre confiance dans la configuration réseau sous Linux.

## Quiz Question

Qu'est-ce qui essaie d'attribuer des adresses IP avec le protocole DHCP ?

## Quiz Answer

dhclient
