---
index: 3
lang: "fr"
title: "Le chemin d'un paquet"
meta_title: "Le chemin d'un paquet - Routage"
meta_description: "Apprenez comment un paquet voyage à l'intérieur et à l'extérieur d'un réseau. Comprenez IP, MAC, ARP et les tables de routage pour la communication réseau. Démarrez votre parcours de mise en réseau Linux !"
meta_keywords: "voyage de paquet, communication réseau, ARP, adresse IP, adresse MAC, table de routage, mise en réseau Linux, guide du débutant"
---

## Lesson Content

### Voyons comment un paquet voyage au sein de son réseau local

1. Tout d'abord, la machine locale comparera l'adresse IP de destination pour voir si elle se trouve dans le même sous-réseau en examinant son masque de sous-réseau.
2. Lorsque les paquets sont envoyés, ils doivent avoir une adresse MAC source, une adresse MAC de destination, une adresse IP source et une adresse IP de destination. À ce stade, nous ne connaissons pas l'adresse MAC de destination.
3. Pour atteindre l'hôte de destination, nous utilisons ARP pour diffuser une requête sur le réseau local afin de trouver l'adresse MAC de l'hôte de destination.
4. Maintenant, le paquet peut être envoyé avec succès !

### Voyons comment un paquet voyage en dehors de son réseau

1. Tout d'abord, la machine locale comparera l'adresse IP de destination. Puisqu'elle est en dehors de notre réseau, elle ne voit pas l'adresse MAC de l'hôte de destination. Et nous ne pouvons pas utiliser ARP car la requête ARP est une diffusion vers les hôtes connectés localement.
2. Notre paquet examine donc maintenant la table de routage. Il ne connaît pas l'adresse IP de destination, il l'envoie donc à la passerelle par défaut (un autre routeur). Ainsi, notre paquet contient maintenant notre IP source, notre IP de destination et notre MAC source ; cependant, nous n'avons pas de MAC de destination. Rappelez-vous, les adresses MAC ne sont accessibles qu'à travers le même réseau. Alors que fait-il ? Il envoie une requête ARP pour obtenir l'adresse MAC de la passerelle par défaut.
3. Le routeur examine le paquet et confirme l'adresse MAC de destination, mais ce n'est pas l'adresse IP de destination finale, il continue donc à regarder la table de routage pour transférer le paquet à une autre adresse IP qui peut aider le paquet à atteindre sa destination. Chaque fois que le paquet se déplace, il supprime les anciennes adresses MAC source et de destination et met à jour le paquet avec les nouvelles adresses MAC source et de destination.
4. Une fois que le paquet est transféré vers le même réseau, nous utilisons ARP pour trouver l'adresse MAC de destination finale.
5. Pendant ce processus, notre paquet ne change pas l'adresse IP source ou de destination.

## Exercise

No exercises for this lesson.

## Quiz Question

Comment trouvons-nous l'adresse MAC d'une adresse IP ?

## Quiz Answer

ARP
