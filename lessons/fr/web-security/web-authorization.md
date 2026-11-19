---
lesson_id: "web-authorization"
course_id: "web-security"
lang: "fr"
order_index: 6
title: "Autorisation"
description: "Apprenez à comparer la demande d’un utilisateur authentifié aux règles d’accès d’une application."
meta_title: "Autorisation - Sécurité web"
meta_description: "Apprenez à comparer la demande d’un utilisateur authentifié aux règles d’accès d’une application."
meta_keywords: "autorisation, sécurité web, cybersécurité, Linux Journey"
---

Un utilisateur peut être connecté sans avoir le droit d’effectuer une action précise. L’**autorisation** détermine si un compte donné peut effectuer une action sur une ressource.

## Lire une règle d’accès

Un **rôle** est un ensemble de droits auquel on donne un nom. Ces règles d’exercice s’appliquent à un service de prévisualisation.

```text
Role       View published page   Edit draft
Reader    Yes                   No
Editor    Yes                   Yes
```

Lisez la ligne du rôle de l’utilisateur et la colonne de l’opération demandée. Un éditeur peut lire la page publiée et modifier un brouillon. Un lecteur peut lire la page publiée.

:::single-choice{#web-authorization-read-policy} Un lecteur connecté demande à modifier un brouillon. Que dit le tableau ?

::option[L’action est interdite au rôle Reader.]{#web-authorization-read-policy-b .correct explanation="La ligne Reader indique No dans la colonne Edit draft."}
::option[L’action est autorisée pour tout compte connecté.]{#web-authorization-read-policy-a explanation="Le réglage pour cette action dépend du rôle."}
::option[L’utilisateur doit passer à HTTPS pour modifier le brouillon.]{#web-authorization-read-policy-c explanation="La protection du transport n’attribue aucun droit dans l’application."}
:::

## Vérifier la ressource concernée

De nombreux systèmes accordent des droits différents selon la ressource. Un éditeur pourrait modifier les brouillons de son propre projet et seulement consulter les pages d’un autre projet. La vérification doit préciser l’opération et la ressource visée.

:::single-choice{#web-authorization-target-resource} Maya peut modifier Project A. Quel élément permet de savoir si elle peut modifier Project B ?

::option[Le titre de Project A.]{#web-authorization-target-resource-b explanation="Le titre n’indique pas les droits d’accès à un autre projet."}
::option[Le fait que Maya s’est connectée avec succès.]{#web-authorization-target-resource-c explanation="L’authentification identifie le compte de Maya. L’accès à la ressource reste à vérifier."}
::option[Les règles de permissions qui s’appliquent à Maya sur Project B.]{#web-authorization-target-resource-a .correct explanation="Le droit accordé précédemment portait sur une ressource précise."}
:::

## Appliquer les règles dans le service

Une interface peut masquer les commandes de modification aux lecteurs. Le serveur doit tout de même appliquer ses règles à chaque requête reçue. Testez les cas qui doivent réussir et ceux qui doivent être refusés en passant par les opérations normales et approuvées du service d’exercice.

:::single-choice{#web-authorization-decision-location} Une application masque le bouton Edit aux lecteurs. Où la décision d’accès doit-elle aussi être appliquée ?

::option[Uniquement dans le navigateur lorsqu’il choisit quel bouton afficher.]{#web-authorization-decision-location-a explanation="Le navigateur peut adapter l’interface. Le service prend la décision d’accès pour la requête qu’il reçoit."}
::option[Dans le service qui reçoit la demande d’opération.]{#web-authorization-decision-location-c .correct explanation="Le service peut évaluer à chaque fois le compte, l’action et la ressource cible."}
::option[Uniquement sur la page qui liste les rôles.]{#web-authorization-decision-location-b explanation="Afficher le nom du rôle ne suffit pas à restreindre une opération."}
:::

## Résumé

Vous savez maintenant examiner une décision d’accès dans une application.

1. Vérifiez si le rôle du compte autorise l’action demandée.
2. Tenez compte de la ressource précise.
3. Vérifiez que le service applique ses règles aux requêtes.
