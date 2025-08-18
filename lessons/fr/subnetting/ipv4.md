---
lang: "fr"
title: "IPv4"
meta_title: "IPv4 - Subnetting"
meta_description: "Apprenez les adresses IPv4, leur structure et comment trouver votre IP en utilisant ifconfig. Comprenez les bases du réseau pour les débutants Linux."
meta_keywords: "IPv4, adresse IP, ifconfig, bases du réseau, réseau Linux, débutant, tutoriel, guide"
---

## Lesson Content

Nous savons donc que les hôtes réseau ont une adresse unique à laquelle ils peuvent être trouvés. Ces adresses sont appelées adresses IP. Une adresse IPv4 ressemble à ceci :

```
204.23.124.23
```

Cette adresse contient en fait deux parties : la partie réseau qui nous indique sur quel réseau elle se trouve, et la partie hôte qui nous indique quel hôte sur ce réseau elle est. Pour ce cours, nous discuterons principalement des adresses IPv4, qui sont ce que vous verrez couramment lorsque vous ferez référence aux adresses IP.

Une adresse IP est séparée en octets par des points. Il y a donc 4 octets dans une adresse IPv4. Si vous connaissez un peu l'informatique, un octet est de 8 bits, et 8 bits équivalent en fait à 1 octet, nous disons donc aussi qu'une adresse IPv4 a 4 octets. Nous utilisons fréquemment les bits lorsque nous traitons des sous-réseaux et des adresses IP.

Vous pouvez afficher votre adresse IP avec la commande `ifconfig -a` :

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Comme vous pouvez le voir, mon adresse IPv4 est : 192.168.1.129

## Exercise

Trouvez votre adresse IP avec `ifconfig`.

## Quiz Question

Combien d'octets y a-t-il dans une adresse IPv4 ?

## Quiz Answer

4
