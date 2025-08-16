---
title: "Protocoles de Routage"
description: "Découvrez les protocoles de routage comme le vecteur de distance et l'état de lien. Comprenez la convergence du réseau et comment les routeurs s'adaptent aux changements. Commencez votre parcours de mise en réseau Linux !"
keywords: "protocoles de routage, convergence réseau, vecteur de distance, état de lien, mise en réseau Linux, guide du débutant, tutoriel réseau"
---

## Lesson Content

Il serait fastidieux de devoir configurer manuellement les routes sur une table de routage pour chaque appareil de votre réseau. Au lieu de cela, nous utilisons ce que l'on appelle des protocoles de routage. Les protocoles de routage aident notre système à s'adapter aux changements du réseau ; ils apprennent différentes routes, les intègrent dans la table de routage, puis acheminent nos paquets de cette manière. Il existe deux types principaux de protocoles de routage : les protocoles à vecteur de distance et les protocoles à état de lien.

### Convergence

Avant de parler des protocoles, nous devrions aborder un terme utilisé en routage connu sous le nom de convergence. Lors de l'utilisation de protocoles de routage, les routeurs communiquent avec d'autres routeurs pour collecter et échanger des informations sur le réseau. Lorsqu'ils s'accordent sur l'apparence d'un réseau, chaque table de routage cartographie la topologie complète du réseau, ainsi "convergeant". Lorsqu'un événement se produit dans la topologie du réseau, la convergence sera temporairement rompue jusqu'à ce que tous les routeurs soient conscients de ce changement.

## Exercise

No exercises for this lesson.

## Quiz Question

Quel est le terme utilisé lorsque toutes les tables de routage connaissent la topologie du réseau ?

## Quiz Answer

Convergence
