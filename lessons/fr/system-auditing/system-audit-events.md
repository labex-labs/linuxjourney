---
lesson_id: "system-audit-events"
course_id: "system-auditing"
lang: "fr"
order_index: 1
title: "Événements d’audit"
description: "Apprenez à choisir les événements à auditer pour répondre à une question sur un fichier protégé."
meta_title: "Événements d’audit - Audit système"
meta_description: "Apprenez à choisir les événements à auditer pour répondre à une question sur un fichier protégé."
meta_keywords: "événements d’audit, audit système, cybersécurité, Linux Journey"
---

Un journal de service peut signaler qu’une page a été chargée. Une **entrée d’audit** peut décrire une action que votre système est configuré pour observer, comme une écriture dans un fichier de configuration. Déterminez d’abord l’action qui vous intéresse et les renseignements nécessaires à son examen.

## Définir la question d’audit

Supposons que la configuration du service web fixe qui peut ouvrir une prévisualisation. Vous voulez examiner les modifications de ce fichier. Une entrée utile indiquerait la cible, l’opération, l’heure, le contexte du compte et le résultat. Chaque champ aide à reconstituer un aspect de l’action.

:::single-choice{#system-audit-events-choose-object} Quel élément l’entrée d’audit doit-elle identifier pour cet examen ?

::option[Uniquement le nombre de requêtes web de la journée.]{#system-audit-events-choose-object-b explanation="Le volume de requêtes décrit une autre activité."}
::option[Le fichier de configuration ciblé.]{#system-audit-events-choose-object-a .correct explanation="La cible permet de distinguer cette modification des écritures dans d’autres fichiers."}
::option[Uniquement le type d’opération, par exemple une écriture.]{#system-audit-events-choose-object-c explanation="L’opération indique ce qui a été tenté. Le fichier cible permet de juger si la tentative est pertinente."}
:::

## Lire le résultat

Une entrée peut décrire une écriture réussie ou une tentative infructueuse. Tenez compte de l’opération et de son résultat. Un refus d’écriture peut constituer une preuve utile d’une tentative. Il conduit à une conclusion différente d’une écriture réussie.

:::single-choice{#system-audit-events-operation-result} Une entrée indique une écriture dans la configuration et un résultat de refus. Que montre-t-elle ?

::option[La tentative d’écriture enregistrée a été refusée.]{#system-audit-events-operation-result-b .correct explanation="L’opération et le résultat décrivent ensemble l’action observée."}
::option[Le fichier a forcément été remplacé.]{#system-audit-events-operation-result-a explanation="Un refus n’établit pas qu’une modification a réussi."}
::option[La page attendue a renvoyé HTTP 200.]{#system-audit-events-operation-result-c explanation="L’entrée ne décrit aucune requête de page."}
:::

## Vérifier la couverture de l’audit

Le système d’audit consigne seulement les événements que ses mécanismes et ses règles lui permettent d’observer. Avant de vous appuyer sur une recherche vide, vérifiez que la politique couvrait le bon chemin, les bonnes opérations et la bonne période. Notez quelle source vous avez examinée.

:::single-choice{#system-audit-events-empty-audit} Vous ne trouvez aucune écriture dans le journal sélectionné. Que vérifier avant de conclure qu’aucune écriture n’a eu lieu ?

::option[Compter les éditeurs installés.]{#system-audit-events-empty-audit-a explanation="Les logiciels installés n’indiquent pas la couverture de l’audit."}
::option[Rechercher la même période uniquement sous un deuxième nom de compte.]{#system-audit-events-empty-audit-b explanation="Une recherche supplémentaire peut aider si la collecte fonctionne. Vérifiez d’abord si les événements recherchés pouvaient être enregistrés."}
::option[Vérifier la politique et la période disponible.]{#system-audit-events-empty-audit-c .correct explanation="Un défaut de couverture peut laisser la recherche vide même si une action a eu lieu."}
:::

## Résumé

Vous savez maintenant sélectionner les éléments d’audit utiles pour une ressource protégée.

1. Identifiez l’opération et la cible que vous voulez examiner.
2. Lisez le résultat enregistré avec l’action demandée.
3. Vérifiez la couverture avant d’utiliser une recherche vide comme élément de preuve.
