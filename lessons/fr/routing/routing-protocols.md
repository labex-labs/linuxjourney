---
lesson_id: "routing-protocols"
course_id: "routing"
lang: "fr"
order_index: 4
title: "Protocoles de routage"
description: "Découvrez comment les protocoles de routage dynamique échangent l’accessibilité et convergent vers des chemins d’acheminement utilisables."
meta_title: "Protocoles de routage - Routage"
meta_description: "Explorez les protocoles de routage, les vecteurs de distance, l’état des liens, la convergence et la construction des tables de routage."
meta_keywords: "protocoles routage, convergence réseau, vecteur distance, état liens, réseau Linux, table routage, tutoriel réseau"
---

Les routes statiques sont configurées directement, tandis que les protocoles de routage dynamique échangent des informations d’accessibilité et de topologie pour permettre aux routeurs de s’adapter. L’apprentissage dynamique réduit le travail manuel, mais introduit un état de protocole, des frontières de confiance, des minuteurs et des modes de panne qui doivent être surveillés.

## Plan de contrôle et plan d’acheminement

Un protocole de routage apprend des routes candidates dans sa propre base. Le routeur sélectionne les routes dans une base d’informations de routage et installe des prochains sauts utilisables dans une table d’acheminement. Le matériel ou le noyau achemine ensuite les paquets depuis cette table.

L’établissement d’une adjacence de protocole ne prouve pas que le préfixe voulu a été appris, sélectionné, installé ou autorisé par la politique d’acheminement.

:::single-choice{#routing-protocols-adjacency-limit}
Qu’est-ce qu’une adjacence de routage établie ne prouve pas ?

::option[Que chaque route voulue est installée et achemine correctement.]{#routing-protocols-not-full-proof .correct explanation="L’annonce, la sélection, l’installation, le filtrage et le fonctionnement du plan de données sont des étapes distinctes."}
::option[Que deux participants au protocole ont échangé des messages de contrôle.]{#routing-protocols-no-messages explanation="L’établissement d’une adjacence nécessite normalement une communication de protocole."}
::option[Qu’un plan de contrôle existe.]{#routing-protocols-no-control explanation="L’adjacence constitue elle-même un état du plan de contrôle."}
:::

## Routage intérieur et extérieur

Les protocoles de passerelle intérieure fonctionnent au sein d’un domaine de routage administratif. RIP, OSPF et IS-IS en sont des exemples. BGP échange des informations d’accessibilité contrôlées par des politiques au sein des systèmes autonomes et entre eux ; c’est le protocole de routage extérieur d’Internet.

Les métriques possèdent un sens propre à chaque protocole. Un coût OSPF, un nombre de sauts RIP et un ensemble d’attributs BGP ne peuvent pas être comparés comme s’ils partageaient une échelle numérique universelle. Les implémentations emploient une préférence de route ou une distance administrative pour choisir entre les sources avant ou parallèlement à la sélection propre au protocole.

:::single-choice{#routing-protocols-metric-comparison}
Peut-on comparer directement un nombre de sauts RIP à un coût OSPF ?

::option[Oui, car toutes les métriques de routage emploient les mêmes unités.]{#routing-protocols-universal-metric explanation="Chaque protocole définit sa propre métrique et son propre processus de sélection."}
::option[Oui, mais uniquement lorsque les deux valeurs sont nulles.]{#routing-protocols-zero-metric explanation="Leur sémantique reste différente quelle que soit la valeur affichée."}
::option[Non ; leur signification est propre à chaque protocole.]{#routing-protocols-specific-metric .correct explanation="La sélection entre sources repose sur la politique de l’implémentation plutôt que sur le traitement de métriques différentes comme une seule échelle."}
:::

## Vecteur de distance et état des liens

Les protocoles à vecteur de distance annoncent l’accessibilité et la distance par leurs voisins, puis déduisent les chemins de leurs rapports. Les protocoles à état des liens forment des adjacences, diffusent les informations d’état des liens dans un périmètre, construisent une base de topologie et calculent des arbres de plus courts chemins. Les protocoles modernes comportent des raffinements qui rendent ces catégories simples incomplètes.

:::single-choice{#routing-protocols-link-state-input}
Qu’emploie un routeur à état des liens pour calculer ses chemins ?

::option[Uniquement le nom d’hôte de sa passerelle par défaut.]{#routing-protocols-hostname-only explanation="Un calcul de topologie exige des informations sur les liens et les préfixes."}
::option[Une base synchronisée qui décrit les liens du périmètre de routage.]{#routing-protocols-link-database .correct explanation="Le routeur exécute un algorithme de plus court chemin sur la topologie apprise."}
::option[Les mots de passe applicatifs de chaque hôte.]{#routing-protocols-passwords explanation="L’échange de topologie de routage ne nécessite pas les identifiants des utilisateurs finaux."}
:::

## Convergence

Après un changement de topologie ou de politique, les routeurs le détectent, propagent les informations de contrôle, calculent les chemins et mettent à jour l’état d’acheminement. La convergence est la période et l’issue au cours desquelles le réseau atteint un routage stable et mutuellement utilisable pour les destinations concernées. Elle n’exige pas une table complète identique sur chaque routeur ; les rôles et les politiques peuvent volontairement différer.

Pendant la convergence, des pertes, des boucles ou des trous noirs temporaires peuvent survenir. Mesurez séparément la détection, la propagation, le calcul et l’installation, puis vérifiez avec des sondes du plan de données.

:::single-choice{#routing-protocols-convergence}
Qu’est-ce que la convergence du routage ?

::option[Le processus permettant d’atteindre un routage stable et utilisable après un changement.]{#routing-protocols-stable-routing .correct explanation="Elle comprend la propagation du contrôle et les mises à jour d’acheminement qui en résultent."}
::option[L’obligation pour chaque routeur de conserver une table globale identique.]{#routing-protocols-identical-table explanation="La politique, les zones et les rôles peuvent créer des différences intentionnelles."}
::option[La prévention permanente de toute panne de routage possible.]{#routing-protocols-no-failure explanation="Un réseau convergé peut encore souffrir de problèmes de politique ou de capacité."}
:::

## Résumé

Vous savez maintenant situer les informations de routage dynamique sur le chemin qui va de l’échange de protocole à l’acheminement.

1. Distinguer les routes candidates apprises, les routes sélectionnées et les entrées d’acheminement.
2. Distinguer le routage intérieur des échanges de politiques BGP.
3. Comparer les métriques uniquement dans la sémantique de leur protocole.
4. Vérifier la convergence dans les plans de contrôle et de données.
