---
lesson_id: "subnetting-cheats"
course_id: "subnetting"
lang: "fr"
order_index: 4
title: "Astuces pour les sous-réseaux"
description: "Découvrez des méthodes binaires et de taille de blocs compactes pour vérifier les calculs des sous-réseaux IPv4."
meta_title: "Astuces pour les sous-réseaux - Sous-réseaux"
meta_description: "Maîtrisez les conversions binaires avec 128+64+32+16+8+4+2+1 pour vérifier rapidement les calculs d’adresses et de sous-réseaux."
meta_keywords: "sous-réseaux, conversion binaire, adresse IP, réseau Linux, 128+64+32+16+8+4+2+1, décimal binaire, calcul sous-réseaux"
---

Les calculateurs de sous-réseaux sont utiles, mais quelques motifs binaires facilitent la vérification de leurs résultats. Ces méthodes sont des contrôles, et non des substituts à la confirmation de l’attribution et de la politique de routage réelles.

## Valeurs des bits d’un octet

Un octet IPv4 emploie les valeurs de position suivantes :

```text
bit :     1   1   1   1   1  1  1  1
valeur : 128  64  32  16   8  4  2  1
```

L’addition des huit valeurs donne 255. Le nombre décimal 192 vaut `128 + 64` ; sa représentation binaire est donc `11000000`.

:::single-choice{#subnet-cheats-binary-192} Quelle est la représentation binaire sur huit bits du nombre décimal 192 ?

::option[`11000000`]{#subnet-cheats-192-correct .correct explanation="Les positions 128 et 64 sont à un et les autres à zéro."}
::option[`10101000`]{#subnet-cheats-168 explanation="Ce motif vaut 168."}
::option[`11111111`]{#subnet-cheats-255 explanation="Les huit positions à un donnent 255."}
:::

## Masques courants dans un octet partiel

Des bits de préfixe contigus produisent une courte séquence de masques :

```text
bits à un : 0    1    2    3    4    5    6    7    8
décimal :   0  128  192  224  240  248  252  254  255
```

Par exemple, `/19` contient 16 bits de préfixe complets et trois bits supplémentaires dans le troisième octet ; son masque est donc `255.255.224.0`.

:::single-choice{#subnet-cheats-prefix-19} Quel masque correspond au préfixe IPv4 `/19` ?

::option[`255.255.224.0`]{#subnet-cheats-mask-19 .correct explanation="Seize bits complets et trois supplémentaires donnent 255, 255 et 224."}
::option[`255.255.19.0`]{#subnet-cheats-literal-19 explanation="Une longueur de préfixe est un nombre de bits, et non un octet décimal du masque."}
::option[`255.255.255.19`]{#subnet-cheats-tail-19 explanation="Ce masque ne possède pas 19 bits contigus."}
:::

## Tailles des blocs

Dans le premier octet du masque différent de 255, soustrayez sa valeur de 256 pour obtenir l’incrément du sous-réseau. Un masque `/27` se termine par 224, ce qui donne une taille de bloc de `256 - 224 = 32`. Les limites du dernier octet sont donc 0, 32, 64, 96, 128, 160, 192 et 224.

L’adresse `198.51.100.77/27` se trouve dans le bloc allant de 64 à 95.

:::single-choice{#subnet-cheats-77-network} Quelle est l’adresse réseau de `198.51.100.77/27` ?

::option[`198.51.100.32`]{#subnet-cheats-network-32 explanation="Ce bloc couvre les valeurs du dernier octet allant de 32 à 63."}
::option[`198.51.100.77`]{#subnet-cheats-network-77 explanation="Cette adresse contient des bits d’hôte et ne constitue pas la limite du bloc."}
::option[`198.51.100.64`]{#subnet-cheats-network-64 .correct explanation="Le bloc `/27` qui commence à 64 couvre 64 à 95."}
:::

## Convertir un octet quelconque

Pour convertir le nombre décimal 123, sélectionnez successivement les plus grandes valeurs restantes sans le dépasser :

```text
123 = 64 + 32 + 16 + 8 + 2 + 1
    = 01111011
```

Pour revenir au décimal, additionnez uniquement les valeurs de position dont les bits valent un. Conservez toujours les huit positions lorsque vous travaillez dans un octet IPv4.

:::single-choice{#subnet-cheats-binary-123} Quelle valeur sur huit bits correspond au nombre décimal 123 ?

::option[`1111011`]{#subnet-cheats-123-seven-bit explanation="La valeur numérique est semblable, mais la représentation d’un octet doit conserver huit positions."}
::option[`01111011`]{#subnet-cheats-123-correct .correct explanation="Les positions à un donnent 64 + 32 + 16 + 8 + 2 + 1."}
::option[`01111100`]{#subnet-cheats-124 explanation="Ce motif emploie la position 4 au lieu de 2 et 1, ce qui donne 124."}
:::

## Résumé

Vous savez maintenant vérifier les calculs IPv4 courants avec des motifs binaires compacts.

1. Employer les huit valeurs de position d’un octet, de 128 à 1.
2. Mémoriser la séquence des masques contigus dans un octet partiel.
3. Déduire la taille du bloc en soustrayant le masque partiel de 256.
4. Conserver huit bits lors de la conversion d’un octet.
