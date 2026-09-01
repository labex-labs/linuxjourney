---
lesson_id: "umask"
course_id: "permissions"
lang: "fr"
order_index: 4
title: "Umask"
description: "Découvrez comment l’umask d’un processus limite les bits de permissions demandés pour les nouveaux fichiers et répertoires."
meta_title: "Umask - Permissions"
meta_description: "Apprenez à employer la commande umask pour contrôler les permissions initiales des nouveaux fichiers et répertoires sous Linux."
meta_keywords: "umask, permissions Linux, permissions des fichiers, commandes Linux, Linux débutant, tutoriel Linux, permissions par défaut"
---

Le masque de création de fichiers d’un processus, ou umask, empêche certains bits de permissions d’être définis lorsque ce processus crée un objet du système de fichiers. Il s’agit d’un masque, et non d’un mode par défaut complet : l’application demande d’abord un mode, puis le noyau retire les bits interdits par l’umask.

Conceptuellement :

```text
mode obtenu = mode demandé ET NON umask
```

Les listes de contrôle d’accès et le comportement de l’application peuvent ajouter d’autres subtilités ; examinez donc le résultat lorsque les permissions exactes importent.

## Afficher et définir l’umask

Exécutez `umask` sans opérande pour afficher le masque du shell actuel, souvent sous forme octale :

```bash
$ umask
0022
```

Définissez-le pour le shell actuel et les processus que celui-ci démarrera ensuite :

```bash
$ umask 027
```

Chaque position octale correspond au propriétaire, au groupe et aux autres. Un bit du masque retire la permission demandée correspondante : `2` masque l’écriture, `4` la lecture et `1` l’exécution.

:::single-choice{#umask-command-purpose} Que modifie `umask 027` dans le shell actuel ?

::option[Les permissions de chaque fichier qui existe déjà.]{#umask-existing-files explanation="Un umask affecte les demandes de création ; il n’exécute pas rétroactivement `chmod` sur les objets existants."}
::option[Le masque hérité par les commandes lancées ensuite depuis ce shell.]{#umask-current-shell-mask .correct explanation="Le shell définit l’umask de son processus, et les processus enfants héritent normalement de cette valeur."}
::option[Les noms du propriétaire et du groupe enregistrés sur les nouveaux fichiers.]{#umask-owner-group explanation="Le masque filtre les bits de permissions et ne sélectionne pas les identités de propriété."}
:::

## Calculer les modes des nouveaux fichiers et répertoires

De nombreux programmes ordinaires demandent `0666` pour les nouveaux fichiers ordinaires, car créer par défaut des fichiers exécutables serait dangereux. Ils demandent couramment `0777` pour les nouveaux répertoires, où la permission d’exécution est nécessaire à la traversée.

Avec l’umask `0022` :

```text
fichier ordinaire : 0666 masqué par 0022 -> 0644 (rw-r--r--)
répertoire :        0777 masqué par 0022 -> 0755 (rwxr-xr-x)
```

L’umask ne fait que retirer les bits demandés. Il ne peut pas ajouter la permission d’exécution si l’application ne l’a pas demandée. Une application peut également demander un mode initial plus restrictif, ce qui produit un résultat lui aussi plus restrictif.

:::single-choice{#umask-file-mode-022} Si un programme demande le mode `0666` pour un fichier ordinaire et que l’umask vaut `0022`, quel mode obtient-on ?

::option[`0666`]{#umask-file-0666 explanation="Les bits d’écriture demandés pour le groupe et les autres par `0666` sont retirés par le masque `0022`."}
::option[`0755`]{#umask-file-0755 explanation="Aucun bit d’exécution n’a été demandé pour le fichier ordinaire ; l’umask ne peut donc pas en ajouter."}
::option[`0644`]{#umask-file-0644 .correct explanation="Le retrait de l’écriture pour le groupe et les autres de `0666` laisse la lecture et l’écriture au propriétaire et la lecture seule au groupe et aux autres."}
:::

:::single-choice{#umask-directory-mode-027} Si un programme demande `0777` pour un répertoire et que l’umask vaut `0027`, quel mode obtient-on ?

::option[`0777`]{#umask-directory-0777 explanation="La demande d’écriture du groupe et toutes les permissions des autres sont filtrées par le masque non nul."}
::option[`0640`]{#umask-directory-0640 explanation="Ce résultat retire également des bits d’exécution que le masque `0027` ne retire ni au propriétaire ni au groupe."}
::option[`0750`]{#umask-directory-0750 .correct explanation="Le masque retire l’écriture du groupe et toutes les permissions des autres, ce qui laisse `rwxr-x---`."}
:::

## Portée et persistance

La modification de l’umask dans un shell n’affecte ni son processus parent ni les sessions sans rapport. La valeur s’applique aux créations futures de ce shell et de ses descendants ; les fichiers existants conservent leurs modes.

Pour rendre une valeur persistante, configurez-la dans les paramètres de connexion, du shell, de PAM, du gestionnaire de services ou de l’application appropriés à votre environnement. Le bon emplacement varie, et les services peuvent définir leur propre umask. Ne supposez pas que la modification d’un fichier de shell interactif gouverne tous les processus du système.

:::single-choice{#umask-existing-file-effect} Que devient un fichier existant lorsque vous définissez un nouvel umask ?

::option[Son mode actuel reste inchangé.]{#umask-existing-unchanged .correct explanation="Un nouvel umask filtre les demandes de création ultérieures et ne modifie pas les modes déjà enregistrés sur les objets du système de fichiers."}
::option[Son mode est recalculé à partir de `0666`.]{#umask-existing-recalculated explanation="Les objets existants ne sont pas recréés ni automatiquement soumis au nouveau masque."}
::option[Son propriétaire perd immédiatement les permissions masquées.]{#umask-existing-owner-loss explanation="La modification de l’umask d’un processus n’agit pas sur les métadonnées des fichiers existants."}
:::

Pour vous exercer, créez des fichiers et des répertoires sous différents masques dans un environnement isolé, puis comparez leurs modes avec `ls -ld`. L’atelier [Groupes d’utilisateurs Linux et permissions des fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002) fournit un espace approprié.

## Résumé

Vous savez maintenant prévoir comment un umask limite les permissions nouvellement demandées.

1. Afficher ou définir le masque du shell actuel avec `umask`.
2. Retirer les bits masqués du mode demandé par une application.
3. Distinguer les demandes courantes `0666` des fichiers et `0777` des répertoires.
4. Considérer la portée et la persistance de l’umask comme propres au processus et à l’environnement.
