---
index: 2
lang: "fr"
title: "Table de Routage"
meta_title: "Table de Routage - Routage"
meta_description: "Apprenez à comprendre la table de routage Linux et comment les paquets sont acheminés à l'aide de la commande route. Explorez les destinations, les passerelles et les interfaces pour les bases du réseau."
meta_keywords: "table de routage Linux, commande route, routage réseau, mise en réseau Linux, Linux pour débutants, tutoriel Linux, guide réseau"
---

## Lesson Content

Regardez la table de routage de votre machine :

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Destination

Dans le premier champ, nous avons une adresse IP de destination de 192.168.224.0. Cela signifie que tout paquet qui tente d'aller vers ce réseau sort par mon câble Ethernet (eth0). Si j'étais 192.168.224.5 et que je voulais atteindre 192.168.224.7, j'utiliserais simplement l'interface réseau eth0 directement.

Notez que nous avons des adresses de **0.0.0.0**. Cela signifie qu'aucune adresse n'est spécifiée ou qu'elle est inconnue. Ainsi, si par exemple, je voulais envoyer un paquet à l'adresse IP 151.123.43.6, notre table de routage ne sait pas où cela va, elle le désigne donc comme 0.0.0.0 et achemine par conséquent notre paquet vers la Gateway.

### Gateway

Si nous envoyons un paquet qui n'est pas sur le même réseau, il sera envoyé à cette adresse Gateway, qui est bien nommée comme étant une passerelle vers un autre réseau.

### Genmask

C'est le masque de sous-réseau, utilisé pour déterminer quelles adresses IP correspondent à quelle destination.

### Flags

- UG - Network is Up and is a Gateway
- U - Network is Up

### Iface

C'est l'interface par laquelle notre paquet sortira. eth0 désigne généralement le premier périphérique Ethernet de votre système.

## Exercise

Regardez votre table de routage et voyez où vos paquets peuvent aller.

## Quiz Question

Où les paquets sont-ils acheminés si notre table de routage ne sait pas ?

## Quiz Answer

Gateway
