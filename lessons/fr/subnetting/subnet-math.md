---
lesson_id: "subnet-math"
course_id: "subnetting"
lang: "fr"
order_index: 3
title: "Calcul des sous-réseaux"
description: "Découvrez comment calculer le réseau IPv4, la diffusion, la plage et le nombre d’adresses à partir d’un préfixe."
meta_title: "Calcul des sous-réseaux - Sous-réseaux"
meta_description: "Maîtrisez le calcul des masques de sous-réseaux, du nombre d’hôtes et des limites de préfixes IPv4."
meta_keywords: "calcul sous-réseaux, calcul masque sous-réseau, adresse IP, masque sous-réseau, hôtes réseau, binaire, réseau Linux"
---

Le calcul des sous-réseaux applique une longueur de préfixe aux 32 bits d’une adresse IPv4. Le raisonnement binaire évite les erreurs aux limites de préfixes qui ne coïncident pas avec les octets décimaux.

## Trouver l’adresse réseau

Utilisons l’adresse `192.168.1.165/24` :

```text
adresse  11000000.10101000.00000001.10100101
masque   11111111.11111111.11111111.00000000
réseau   11000000.10101000.00000001.00000000
```

Un ET bit à bit conserve les bits de l’adresse lorsque le masque vaut un et efface les bits d’hôte. Le résultat est `192.168.1.0/24`.

:::single-choice{#subnet-math-network-operation} Quelle opération trouve une adresse réseau IPv4 à partir d’une adresse et d’un masque ?

::option[La concaténation de chaînes décimales.]{#subnet-math-concatenation explanation="La jonction des octets affichés n’applique pas les bits du préfixe."}
::option[La soustraction des ports de transport.]{#subnet-math-port-subtraction explanation="Les ports sont sans rapport avec le préfixe réseau."}
::option[Le ET bit à bit.]{#subnet-math-bitwise-and .correct explanation="Les bits réseau restent, tandis que les positions d’hôtes masquées par des zéros sont effacées."}
:::

## Compter les adresses

Pour le préfixe `/p`, la partie hôte comporte `32 - p` bits. Le nombre total d’adresses est :

```text
2^(32 - p)
```

Un `/24` contient donc `2^8 = 256` adresses. Dans un sous-réseau de diffusion traditionnel, la valeur d’hôte entièrement nulle est l’adresse réseau et la valeur entièrement à un est la diffusion dirigée, ce qui laisse 254 adresses d’hôtes unicast ordinaires.

:::single-choice{#subnet-math-24-total} Combien d’adresses au total contient un `/24` IPv4 ?

::option[24]{#subnet-math-total-24 explanation="La longueur du préfixe compte les bits réseau, et non les adresses."}
::option[256]{#subnet-math-total-256 .correct explanation="Huit bits d’hôte produisent 2^8 valeurs d’adresses distinctes."}
::option[254]{#subnet-math-total-254 explanation="Il s’agit du nombre traditionnel d’hôtes utilisables après le retrait de deux adresses spéciales, et non du total."}
:::

## Trouver la limite d’un bloc

Pour `/26`, le masque est `255.255.255.192`. La taille du bloc dans le dernier octet vaut `256 - 192 = 64` ; les limites des sous-réseaux sont donc 0, 64, 128 et 192. L’adresse `192.168.1.165/26` se trouve dans :

```text
réseau :     192.168.1.128
diffusion :  192.168.1.191
plage :      192.168.1.129 à 192.168.1.190
```

:::single-choice{#subnet-math-165-network} Quelle est l’adresse réseau de `192.168.1.165/26` ?

::option[`192.168.1.0`]{#subnet-math-network-zero explanation="Il s’agit du premier bloc `/26`, qui couvre 0 à 63."}
::option[`192.168.1.165`]{#subnet-math-network-self explanation="L’adresse fournie possède des bits d’hôte non nuls dans le `/26`."}
::option[`192.168.1.128`]{#subnet-math-network-128 .correct explanation="La valeur 165 se trouve dans le bloc allant de 128 à 191."}
:::

## Tenir compte des exceptions de préfixes

Le raccourci `2^bits_hôte - 2` n’est pas universel. Les préfixes IPv4 `/31` sont définis pour les liaisons point à point, où les deux adresses peuvent servir de terminaux et où aucune diffusion dirigée n’est nécessaire. Un `/32` identifie une route d’hôte ou une adresse d’interface unique. La technologie réseau et l’usage du protocole déterminent les adresses attribuables.

:::single-choice{#subnet-math-31-exception} Pourquoi ne faut-il pas soustraire deux adresses de chaque préfixe IPv4 ?

::option[Les adresses IPv4 ne possèdent aucun bit d’hôte, quel que soit le préfixe.]{#subnet-math-no-host-bits explanation="La plupart des préfixes laissent un ou plusieurs bits d’hôte."}
::option[Les liaisons point à point `/31` peuvent employer les deux adresses comme terminaux.]{#subnet-math-31-both .correct explanation="Le modèle point à point n’a pas besoin des réservations traditionnelles d’adresse réseau et de diffusion dirigée."}
::option[Tous les réseaux IPv4 emploient la multidiffusion plutôt que l’unicast.]{#subnet-math-all-multicast explanation="L’adressage unicast ordinaire reste fondamental."}
:::

## Vérifier les calculs

Employez un outil ou une bibliothèque indépendante pour contrôler le travail manuel, puis comparez avec la configuration réelle des interfaces et des routes. Un préfixe mathématiquement valide peut toujours chevaucher un autre sous-réseau ou enfreindre un plan d’attribution.

:::single-choice{#subnet-math-valid-not-safe} Qu’est-ce qu’un calcul de sous-réseau correct ne prouve pas ?

::option[Que le plan d’adressage ne possède aucun chevauchement ni conflit de politique.]{#subnet-math-no-conflict .correct explanation="Des indices sur l’attribution opérationnelle et le routage restent nécessaires."}
::option[Que les adresses IPv4 contiennent 32 bits.]{#subnet-math-proves-size explanation="Le calcul repose sur cette taille fixe."}
::option[Que les puissances de deux déterminent le nombre de blocs.]{#subnet-math-powers explanation="Les combinaisons d’adresses binaires emploient intrinsèquement des puissances de deux."}
:::

## Résumé

Vous savez maintenant calculer les limites des sous-réseaux IPv4 et reconnaître les exceptions courantes.

1. Trouver une adresse réseau avec un ET bit à bit.
2. Compter le nombre total d’adresses à partir des bits d’hôte.
3. Employer la taille des blocs pour trouver les limites du réseau et de la diffusion.
4. Traiter `/31` et `/32` selon leur usage prévu.
5. Vérifier les résultats mathématiques par rapport au plan d’adressage réel.
