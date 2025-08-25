---
index: 1
lang: "fr"
title: "IPv4"
meta_title: "IPv4 - Sous-réseautage"
meta_description: "Découvrez les adresses IPv4, leur structure et comment trouver votre IP à l'aide d'ifconfig. Comprenez les bases du réseau pour les débutants Linux."
meta_keywords: "IPv4, adresse IP, ifconfig, bases du réseau, réseau Linux, débutant, tutoriel, guide"
---

## Lesson Content

Nous savons donc que les hôtes réseau ont une adresse unique à laquelle ils peuvent être trouvés. Ces adresses sont appelées adresses IP. Une adresse IPv4 ressemble à ceci :

```
204.23.124.23
```

Cette adresse contient en fait deux parties : la partie réseau qui nous indique sur quel réseau elle se trouve, et la partie hôte qui nous indique quel hôte sur ce réseau elle est. Pour ce cours, nous discuterons principalement des adresses IPv4, qui sont ce que vous verrez couramment lorsque vous ferez référence aux adresses IP.

Une adresse IP est séparée en octets par des points. Il y a donc 4 octets dans une adresse IPv4. Si vous avez quelques notions d'informatique, un octet est de 8 bits, et 8 bits équivalent en fait à 1 octet, nous disons donc aussi qu'une adresse IPv4 a 4 octets. Nous utilisons fréquemment les bits lorsque nous traitons des sous-réseaux et des adresses IP.

Vous pouvez afficher votre adresse IP avec la commande `ifconfig -a` :

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Comme vous pouvez le voir, mon adresse IPv4 est : 192.168.1.129

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage IP et de l'identification réseau sous Linux :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IPv4 et IPv6, sur un système Linux.
2. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez différents types d'adresses IP et testez la joignabilité du réseau à l'aide de commandes comme `ping` et `ip a`.
3. **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, essentiels pour une compréhension plus approfondie de la structure des adresses IP et des réseaux au niveau du bit.

Ces laboratoires vous aideront à appliquer les concepts d'adressage IP dans des scénarios réels et à renforcer votre confiance dans la configuration et le dépannage réseau sous Linux.

## Quiz Question

Combien d'octets y a-t-il dans une adresse IPv4 ?

## Quiz Answer

4
