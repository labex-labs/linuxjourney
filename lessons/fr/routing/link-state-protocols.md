---
lesson_id: "link-state-protocols"
course_id: "routing"
lang: "fr"
order_index: 6
title: "Protocoles à état des liens"
description: "Découvrez comment les protocoles à état des liens forment des adjacences, diffusent les informations de topologie et calculent les chemins."
meta_title: "Protocoles à état des liens - Routage"
meta_description: "Découvrez les protocoles à état des liens tels qu’OSPF, leur convergence, leur diffusion de topologie et leur mise à jour des routes."
meta_keywords: "protocoles état liens, OSPF, réseau Linux, protocoles routage, topologie réseau, débutant"
---

Les protocoles à état des liens décrivent les liens et préfixes locaux, distribuent ces descriptions dans un périmètre de routage et permettent à chaque routeur de calculer les chemins depuis une base de topologie. OSPF et IS-IS en sont des exemples courants.

## Former des adjacences

Les routeurs découvrent des voisins compatibles et forment des adjacences de protocole selon le type d’interface, la zone, les minuteurs, l’authentification et d’autres paramètres. L’observation de paquets hello ne garantit pas une adjacence complète ; une configuration incompatible peut arrêter plus tôt la machine à états.

:::single-choice{#link-state-hello-limit}
Qu’est-ce que la réception d’un paquet hello OSPF ne prouve pas ?

::option[Que les routeurs ont formé une adjacence entièrement synchronisée.]{#link-state-not-full .correct explanation="La zone, les minuteurs, l’authentification, la MTU et d’autres états peuvent empêcher l’échange complet de la base."}
::option[Que le voisin a envoyé au moins un message de protocole.]{#link-state-hello-sent explanation="La réception du paquet hello prouve directement ce fait limité."}
::option[Qu’une interface peut recevoir une trame.]{#link-state-frame-received explanation="Le paquet reçu prouve qu’une partie du chemin de réception local fonctionne."}
:::

## Diffuser les informations d’état des liens

Chaque routeur produit des annonces sur son état pertinent. Les voisins diffusent de manière fiable les informations plus récentes dans la zone ou le domaine défini au lieu de limiter les mises à jour à la paire de voisins d’origine. Des mécanismes de séquence et de vieillissement distinguent les informations actuelles et retirent les états périmés.

:::single-choice{#link-state-flooding-scope}
Pourquoi les informations d’état des liens sont-elles diffusées au-delà d’un seul voisin ?

::option[Chaque application a besoin d’une copie de tous les mots de passe des routeurs.]{#link-state-password-copy explanation="Les identifiants applicatifs ne constituent pas des annonces de topologie."}
::option[Ethernet ne peut pas envoyer de trames unicast.]{#link-state-no-unicast explanation="Ethernet prend en charge l’unicast ; la diffusion est ici un mécanisme de distribution du protocole de routage."}
::option[Les routeurs du périmètre ont besoin d’une base de topologie cohérente.]{#link-state-consistent-database .correct explanation="Chaque routeur calcule ses chemins depuis l’ensemble partagé des annonces actuelles d’état des liens."}
:::

## Calculer les plus courts chemins

Après avoir construit une base d’état des liens, un routeur exécute un algorithme de plus court chemin d’abord, généralement l’algorithme de Dijkstra, en se prenant comme racine. OSPF additionne les coûts des interfaces ; la politique et les règles de coûts égaux influencent les résultats installés.

« Plus court » signifie le coût de protocole le plus faible, et pas nécessairement le plus petit nombre de routeurs ou la plus faible latence applicative mesurée. La conception des coûts doit refléter l’intention opérationnelle.

:::single-choice{#link-state-shortest-meaning}
Que signifie « plus court » dans le calcul d’un chemin à état des liens ?

::option[La route dont le préfixe comporte le moins de caractères écrits.]{#link-state-shortest-text explanation="La longueur du texte est sans rapport avec le coût de la topologie."}
::option[Le chemin dont la somme des coûts de protocole est la plus faible.]{#link-state-lowest-cost .correct explanation="Le modèle de coût peut correspondre ou non directement au nombre de sauts ou à la latence actuelle."}
::option[Le chemin qui ne connaît jamais aucune perte de paquets.]{#link-state-zero-loss explanation="Une route calculée ne garantit pas les performances de l’application."}
:::

## Zones et convergence

Les zones OSPF limitent la diffusion de la topologie et le périmètre du calcul, la zone 0 servant de dorsale dans une conception interzone normale. La récapitulation et les types de zones peuvent volontairement donner à différents routeurs des niveaux de détail différents dans leur base.

Après un changement de liaison, la détection, la diffusion des annonces, le calcul SPF, l’installation des routes et la reprise de l’acheminement prennent chacun du temps. Une convergence plus rapide qu’avec une conception simple à vecteur de distance est possible, mais pas automatique pour chaque panne ou configuration.

:::single-choice{#link-state-convergence-stages}
Que faut-il mesurer pendant l’analyse d’une convergence OSPF ?

::option[Uniquement l’heure à laquelle un administrateur a ouvert un terminal.]{#link-state-terminal-time explanation="Cela n’isole aucune étape du protocole ou de l’acheminement."}
::option[Uniquement l’ordre alphabétique des noms des routeurs.]{#link-state-router-names explanation="Les noms ne déterminent pas la durée de la convergence."}
::option[La détection, la diffusion, le calcul, l’installation et la reprise de l’acheminement.]{#link-state-all-stages .correct explanation="La séparation des étapes révèle l’endroit où le retard ou l’échec de convergence survient."}
:::

## Résumé

Vous savez maintenant suivre le routage à état des liens de la découverte des voisins aux chemins installés.

1. Distinguer la réception d’un hello d’une adjacence complète.
2. Expliquer la diffusion fiable dans un périmètre de routage.
3. Interpréter le plus court chemin comme le coût de protocole configuré le plus faible.
4. Mesurer chaque étape de convergence des plans de contrôle et de données.
