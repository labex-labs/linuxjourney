---
index: 2
lang: "fr"
title: "Table de Routage"
meta_title: "Table de Routage - Routage"
meta_description: "Un guide pour comprendre la table de routage Linux. Apprenez à interpréter la sortie de la commande route, y compris la destination, la passerelle, genmask et l'interface eth0. Maîtrisez les bases de votre table de routage Linux."
meta_keywords: "table de routage linux, table route linux, genmask, eth0, commande route, routage réseau, routage IP, destination, passerelle, masque de sous-réseau, réseau linux"
---

## Lesson Content

La **table de routage Linux** contient les règles qui déterminent où les paquets réseau sont envoyés. Chaque fois que votre système doit envoyer un paquet à une adresse IP, il consulte cette table pour trouver le chemin approprié. Pour afficher la **table de routage Linux** de votre machine, vous pouvez utiliser la commande `route`.

```plaintext
pete@icebox:~$ sudo route -n
Table de routage IP du noyau
Destination     Passerelle      Genmask         Drapeaux Métrique Ref    Utilisation Interface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Comprendre les Colonnes

Le résultat de la commande `route` est organisé en plusieurs colonnes, chacune fournissant des informations spécifiques sur une route réseau.

### Destination

La colonne Destination spécifie un réseau ou un hôte. L'entrée `192.168.224.0` dirige tous les paquets destinés à ce réseau spécifique. Si la destination d'un paquet se trouve dans ce réseau (par exemple, de 192.168.224.5 à 192.168.224.7), il est envoyé directement via l'interface spécifiée, telle que `eth0`.

La destination `0.0.0.0` est la route par défaut. Si la table de routage n'a pas d'entrée plus spécifique pour la destination d'un paquet, elle utilise cette route.

### Passerelle (Gateway)

La colonne Passerelle (Gateway) indique le routeur vers lequel les paquets sont envoyés. Si un paquet n'est pas sur le même réseau local, il est transféré à cette adresse de passerelle. Pour la route par défaut, il s'agit de l'adresse IP du routeur qui connecte votre réseau local à d'autres réseaux, comme Internet.

### Genmask

Le `genmask`, ou masque de génération, est le masque de sous-réseau pour le réseau de destination. Il est utilisé avec l'IP de destination pour déterminer si un paquet appartient à ce réseau. Par exemple, un `genmask` de `255.255.255.0` signifie que les trois premiers octets de l'adresse IP doivent correspondre aux trois premiers octets de la destination.

### Drapeaux (Flags)

Ces drapeaux fournissent des informations supplémentaires sur la route :

- **U** : Indique que la route est active et opérationnelle.
- **G** : Signifie que la route passe par une passerelle (routeur).
- **UG** : Signifie que la route est active et pointe vers une passerelle.

### Interface (Iface)

Cette colonne indique l'interface réseau, comme `eth0`, par laquelle les paquets pour cette route seront envoyés. `eth0` représente généralement la première carte Ethernet de votre système.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du routage réseau et de l'adressage IP :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IP et les interfaces réseau, qui sont des composants clés d'une table de routage.
2. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Apprenez à gérer l'adressage IP, à configurer des IP statiques, à définir des passerelles par défaut et à vérifier les configurations réseau, ce qui est directement lié aux entrées trouvées dans une table de routage.
3. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez l'adressage IP et la joignabilité réseau à l'aide de `ping` et `ip a`, ce qui vous aidera à comprendre comment les différents types d'IP interagissent et comment la joignabilité réseau est déterminée, ce qui se reflète dans les décisions de routage.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec la configuration et le dépannage réseau.

## Quiz Question

Si une destination n'est pas trouvée dans la table de routage, où les paquets sont-ils envoyés ? Veuillez répondre avec un seul mot anglais, en faisant attention à la casse.

## Quiz Answer

Gateway
