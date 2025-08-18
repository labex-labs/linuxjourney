---
index: 6
lang: "fr"
title: "NAT"
meta_title: "NAT - Subnetting"
meta_description: "Découvrez le NAT (Network Address Translation) sous Linux, son fonctionnement et son rôle dans la sécurité réseau. Comprenez les adresses IP privées et publiques. Guide de mise en réseau Linux."
meta_keywords: "NAT, Network Address Translation, mise en réseau Linux, IP privée, IP publique, tutoriel Linux, guide du débutant"
---

## Lesson Content

Nous avons déjà évoqué le NAT (Network Address Translation) auparavant, mais sans l'aborder en détail. Lorsque nous travaillons sur notre réseau, cela signifie-t-il que l'internet peut voir notre adresse IP ? Pas tout à fait.

Le NAT fait en sorte qu'un appareil comme notre routeur agisse comme un intermédiaire entre l'internet et un réseau privé. Ainsi, une seule adresse IP unique est nécessaire pour représenter un groupe entier d'ordinateurs.

Considérez le NAT comme une réceptionniste dans un grand bureau. Si quelqu'un veut vous contacter, il ne connaît que le numéro du bureau entier. La réceptionniste devrait alors chercher votre numéro de poste et vous transférer l'appel.

### How does it work?

Un cas simple ressemblerait à ceci :

1. Patty veut se connecter à <www.google.com>, donc sa machine envoie cette requête via le routeur.
2. Le routeur prend cette requête et ouvre sa propre connexion à google.com, puis il envoie la requête de Patty une fois la connexion établie.
3. Le routeur est l'intermédiaire entre Patty et <www.google.com>. Google ne connaît pas Patty ; au lieu de cela, tout ce qu'il peut voir est le routeur.

Le NAT et le routage de paquets en général peuvent devenir assez complexes, mais nous n'entrerons pas dans les détails.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Qu'est-ce qui est utilisé pour représenter une seule adresse privée sur internet ?

## Quiz Answer

NAT
