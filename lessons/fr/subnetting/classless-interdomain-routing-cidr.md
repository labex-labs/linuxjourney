---
index: 5
lang: "fr"
title: "CIDR"
meta_title: "CIDR - Sous-réseautage"
meta_description: "Un guide de la notation CIDR. Apprenez le format CIDR, le sous-réseautage CIDR et comment calculer les hôtes pour votre réseau, y compris sur un serveur Ubuntu. Maîtrisez l'adressage IP avec CIDR."
meta_keywords: "CIDR, sous-réseautage cidr, format cidr, masque de sous-réseau, adressage IP, sous-réseau serveur ubuntu, cidr sous-réseau ubuntu, préfixe réseau, réseau Linux"
---

## Lesson Content

Le CIDR (Classless Inter-Domain Routing, ou Routage Inter-Domaines Sans Classe) est une méthode d'allocation des adresses IP et de routage des paquets Internet Protocol. Il offre une manière plus compacte et efficace de représenter un masque de sous-réseau, remplaçant l'ancienne conception de réseau par classes. Comprendre le CIDR est essentiel pour l'administration réseau moderne.

### Le Format CIDR

Vous verrez souvent les réseaux notés en utilisant le **format CIDR**, où une adresse IP est suivie d'une barre oblique et d'un nombre. Par exemple, un sous-réseau comme `10.42.3.0` avec un masque de sous-réseau de `255.255.255.0` s'écrit `10.42.3.0/24`. Cette notation unique inclut à la fois l'adresse réseau et la longueur du préfixe.

Le nombre après la barre oblique indique combien de bits de l'adresse IP sont utilisés pour le préfixe réseau. C'est une tâche courante lors de la configuration du réseau sur un système comme un **serveur Ubuntu**, où vous pourriez définir une interface avec une adresse `ubuntu subnet cidr`.

### Sous-réseautage CIDR et Calcul des Hôtes

Une adresse IPv4 se compose de 4 octets, soit un total de 32 bits. Le préfixe CIDR détermine la séparation entre la partie réseau et la partie hôte de l'adresse. Pour un **cidr subnetting** efficace, vous devez savoir comment calculer le nombre d'hôtes disponibles.

Prenons l'exemple `123.12.24.0/23`. Cela signifie que les 23 premiers bits constituent le préfixe réseau. Pour trouver le nombre d'hôtes disponibles :

1. Soustrayez le préfixe CIDR du nombre total de bits (32) : `32 - 23 = 9`. Il reste donc 9 bits pour la portion hôte.
2. Calculez le nombre total d'adresses dans le sous-réseau : `2^9 = 512`.
3. Soustrayez 2 du total. Une adresse est réservée pour le réseau lui-même, et une pour l'adresse de diffusion (broadcast). Il reste donc `512 - 2 = 510` adresses hôtes utilisables.

Un autre exemple courant est un réseau `/30`, qui fournit `32 - 30 = 2` bits hôtes. Cela donne `2^2 = 4` adresses totales, laissant seulement 2 adresses utilisables, ce qui le rend idéal pour les liaisons point à point.

## Exercise

Pour maîtriser ces concepts, entraînez-vous avec des laboratoires pratiques qui renforcent votre compréhension du CIDR, de l'adressage IP et du **cidr subnetting** :

1. **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, y compris la traduction des masques CIDR et le calcul des hôtes utilisables.
2. **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Apprenez à attribuer des adresses IP statiques et observez comment les sous-réseaux IP régissent la communication réseau directe dans un environnement simulé.
3. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez l'adressage IP et la joignabilité réseau à l'aide de commandes telles que `ping` et `ip a` pour tester divers types d'IP et la connectivité.

Ces laboratoires vous aideront à appliquer les concepts de CIDR et d'adressage IP dans des scénarios réels et à renforcer votre confiance dans la configuration réseau.

## Quiz Question

Combien de bits comporte une adresse IPv4 ?

## Quiz Answer

32
