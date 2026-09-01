---
lesson_id: "process-permissions"
course_id: "permissions"
lang: "fr"
order_index: 7
title: "Permissions des processus"
description: "Découvrez comment les identifiants utilisateur réel, effectif et sauvegardé aident les processus Linux à suivre les appelants et à gérer les privilèges."
meta_title: "Permissions des processus - Permissions"
meta_description: "Découvrez les permissions des processus Linux, notamment les UID réel, effectif et sauvegardé, et leur rôle dans la sécurité et l’exécution des commandes."
meta_keywords: "permissions processus Linux, UID réel, UID effectif, UID sauvegardé, sécurité Linux, commande passwd, tutoriel Linux, Linux débutant"
---

Les contrôles d’autorisation de Linux agissent sur les identifiants des processus plutôt que directement sur un nom d’utilisateur saisi. Un processus possède plusieurs identifiants utilisateur et groupe liés, chacun remplissant un rôle différent. La plupart des programmes ordinaires démarrent avec des identités identiques, tandis que les programmes privilégiés peuvent délibérément employer des valeurs distinctes.

## Identifiant utilisateur réel

L’identifiant utilisateur réel désigne le compte qui a démarré le processus ou sa session de connexion ancêtre. Les programmes peuvent le consulter pour distinguer l’appelant d’une identité effective élevée.

Pour une commande ordinaire lancée par Bob, l’identifiant utilisateur réel correspond normalement à l’UID de Bob. La création d’un autre processus ne crée pas un nouveau compte et ne modifie pas à elle seule cette identité.

:::single-choice{#process-permissions-real-uid} Qu’est-ce que l’identifiant utilisateur réel d’un processus désigne normalement ?

::option[Le propriétaire du fichier ouvert le plus récemment.]{#process-permissions-real-opened-file explanation="L’ouverture d’un fichier ne remplace pas l’UID réel du processus par le propriétaire de ce fichier."}
::option[Le compte associé à l’appelant d’origine du processus.]{#process-permissions-real-caller .correct explanation="L’UID réel enregistre l’identité de l’utilisateur appelant héritée lors du lancement du processus."}
::option[Le groupe sélectionné pour chaque contrôle d’accès.]{#process-permissions-real-group explanation="Un UID est une identité utilisateur ; les contrôles de groupe emploient des identifiants de groupe distincts."}
:::

## Identifiant utilisateur effectif

L’identifiant utilisateur effectif est l’identifiant employé pour de nombreux contrôles de privilèges et du système de fichiers. Il correspond normalement à l’UID réel. L’exécution d’un programme setuid honoré peut au contraire l’initialiser à partir du propriétaire de l’exécutable.

Par exemple, un utilitaire de mot de passe soigneusement conçu peut s’exécuter avec un UID effectif élevé afin de mettre à jour des données d’authentification protégées. Il doit néanmoins faire respecter la politique selon l’appelant, le compte demandé, les résultats de PAM et d’autres éléments de contexte. La possession d’un UID effectif ne rend pas automatiquement légitime chaque opération demandée.

:::single-choice{#process-permissions-effective-uid} Quel identifiant utilisateur sert à de nombreuses décisions de contrôle d’accès prises pour un processus ?

::option[L’identifiant utilisateur effectif.]{#process-permissions-effective-active .correct explanation="L’UID effectif est l’identifiant utilisateur actif consulté pour de nombreux contrôles d’autorisation."}
::option[Uniquement l’identifiant utilisateur sauvegardé.]{#process-permissions-effective-saved-only explanation="L’identifiant sauvegardé permet des transitions d’identifiants, mais n’est généralement pas l’identité active des contrôles d’accès."}
::option[L’UID enregistré sur le répertoire actuel.]{#process-permissions-effective-directory explanation="La propriété du système de fichiers est une métadonnée de l’objet, et non l’identifiant utilisateur actif du processus."}
:::

## Identifiant set-user-ID sauvegardé

L’identifiant set-user-ID sauvegardé permet à un programme de conserver une identité qu’il pourra restaurer ultérieurement, sous réserve des règles des appels système. Un programme privilégié peut temporairement attribuer à son UID effectif une valeur moins privilégiée, accomplir un travail ordinaire avec des droits réduits, puis ne restaurer l’identité sauvegardée que pour une opération précisément limitée.

Cette approche est plus sûre que le maintien d’une autorité élevée pendant toute l’exécution, mais seulement si elle est correctement mise en œuvre. Les programmes doivent abandonner définitivement les privilèges lorsqu’ils ne sont plus nécessaires et contrôler l’échec de chaque appel qui modifie les identifiants.

:::single-choice{#process-permissions-saved-uid} Pourquoi un programme privilégié peut-il conserver un identifiant set-user-ID sauvegardé ?

::option[Pour changer son identité effective pendant des phases privilégiées et non privilégiées contrôlées.]{#process-permissions-saved-switch .correct explanation="L’identité sauvegardée peut permettre une réduction temporaire des privilèges et une restauration ultérieure autorisée."}
::option[Pour attribuer automatiquement cet UID à chaque fichier qu’il lit.]{#process-permissions-saved-file-owner explanation="La lecture d’un fichier ne lui attribue pas l’UID sauvegardé du processus."}
::option[Pour remplacer la base des comptes système au sein du processus.]{#process-permissions-saved-database explanation="Les identifiants du processus ne remplacent ni les enregistrements de comptes ni les données des services de noms."}
:::

## Les identifiants utilisateur ne sont qu’une partie des identifiants du processus

Les processus possèdent aussi des identifiants de groupe réels, effectifs, sauvegardés et supplémentaires. Les identifiants du système de fichiers, les capacités, les espaces de noms, les modules de sécurité, les ACL, les options de montage et les politiques des services peuvent encore influencer l’autorisation. Ainsi, « l’UID l’autorise » ne constitue souvent qu’une partie de l’explication complète.

Employez des outils tels que `ps` et `/proc/PROCESS/status` pour examiner les identifiants sous Linux. La disponibilité des champs et leur format d’affichage varient ; consultez donc la documentation locale et ne modifiez pas les identifiants simplement pour expérimenter sur un système partagé.

:::single-choice{#process-permissions-ordinary-identities} Pour la plupart des commandes ordinaires sans transition de privilèges, comment les UID réel et effectif se comparent-ils ?

::option[L’UID effectif vaut toujours zéro.]{#process-permissions-effective-root explanation="Les commandes ordinaires ne reçoivent pas automatiquement l’UID de root."}
::option[L’UID réel correspond toujours au propriétaire du fichier exécutable.]{#process-permissions-real-file-owner explanation="Le propriétaire de l’exécutable affecte le comportement setuid, et non l’UID réel ordinaire."}
::option[Ils correspondent normalement à l’UID de l’utilisateur appelant.]{#process-permissions-uids-match .correct explanation="Sans setuid ni changement explicite des identifiants, les processus ordinaires s’exécutent généralement avec des identités réelle et effective identiques."}
:::

## Résumé

Vous savez maintenant expliquer pourquoi un processus Linux peut porter plusieurs identités utilisateur.

1. Employer l’UID réel pour identifier l’appelant d’origine.
2. Relier l’UID effectif aux contrôles d’autorisation actifs.
3. Employer l’identité sauvegardée pour comprendre les transitions de privilèges contrôlées.
4. Considérer les identifiants de groupe et les mécanismes de sécurité supplémentaires dans la décision complète.
