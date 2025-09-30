---
index: 6
lang: "fr"
title: "NAT"
meta_title: "NAT - Sous-réseautage"
meta_description: "Découvrez la NAT (Network Address Translation) sous Linux, son fonctionnement et son rôle dans la sécurité réseau. Comprenez les adresses IP privées vs publiques. Guide de mise en réseau Linux."
meta_keywords: "NAT, Network Address Translation, mise en réseau Linux, IP privée, IP publique, tutoriel Linux, guide débutant"
---

## Lesson Content

Nous avons déjà évoqué la NAT (Network Address Translation) auparavant, mais sans l'approfondir. Lorsque nous travaillons sur notre réseau, cela signifie-t-il que l'internet peut voir notre adresse IP ? Pas tout à fait.

La NAT fait en sorte qu'un appareil comme notre routeur agisse comme un intermédiaire entre l'internet et un réseau privé. Ainsi, une seule adresse IP unique est nécessaire pour représenter un groupe entier d'ordinateurs.

Considérez la NAT comme une réceptionniste dans un grand bureau. Si quelqu'un veut vous contacter, il ne connaît que le numéro du bureau entier. La réceptionniste devrait alors chercher votre numéro de poste et vous transférer l'appel.

### Comment ça marche ?

Un cas simple ressemblerait à ceci :

1. Patty veut se connecter à `www.google.com`, donc sa machine envoie cette requête via le routeur.
2. Le routeur prend cette requête et ouvre sa propre connexion à google.com, puis il envoie la requête de Patty une fois la connexion établie.
3. Le routeur est l'intermédiaire entre Patty et `www.google.com`. Google ne connaît pas Patty ; au lieu de cela, tout ce qu'il peut voir est le routeur.

La NAT et le routage de paquets en général peuvent devenir assez complexes, mais nous n'entrerons pas dans les détails.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage réseau et de la connectivité, qui sont fondamentaux pour comprendre des concepts comme la NAT :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IPv4 et IPv6, sur un système Linux.
2. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Apprenez à gérer l'adressage IP en configurant des adresses IP statiques et dynamiques, et en vérifiant la configuration réseau, ce qui aide à comprendre comment les appareils obtiennent leurs adresses.
3. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez différents types d'adresses IP (privées, publiques, multicast) et testez la joignabilité du réseau, offrant un contexte pratique pour la façon dont la NAT distingue les adresses internes et externes.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la configuration et le dépannage réseau sous Linux.

## Quiz Question

Qu'est-ce qui est utilisé pour représenter une seule adresse privée sur Internet ?

## Quiz Answer

NAT
