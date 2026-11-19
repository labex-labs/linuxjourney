---
lesson_id: "deployment-health-checks"
course_id: "deployment"
lang: "fr"
order_index: 4
title: "Contrôles d’état"
description: "Apprenez à vérifier le processus, à interroger le service et à envoyer une requête depuis un client après le déploiement."
meta_title: "Contrôles d’état - Déploiement"
meta_description: "Apprenez à vérifier le processus, à interroger le service et à envoyer une requête depuis un client après le déploiement."
meta_keywords: "contrôles d’état, point d’accès, déploiement, DevOps, Linux Journey"
---

Un programme qui vient de démarrer peut être en cours d’exécution avant d’être prêt. Vérifiez le service par étapes pour savoir ce que démontre chaque résultat positif.

## Vérifier le processus

La liste des conteneurs peut vous indiquer si le programme principal tourne. Cela répond à une première question importante après un déploiement. Pour savoir s’il a terminé son initialisation ou si le navigateur peut l’atteindre, il faut d’autres vérifications.

:::single-choice{#deployment-health-checks-process-scope} Le nouveau conteneur affiche Up. Que pouvez-vous en conclure ?

::option[Les visiteurs reçoivent forcément la nouvelle page.]{#deployment-health-checks-process-scope-a explanation="L’état du conteneur ne décrit pas la réponse à une requête de visiteur."}
::option[Le programme principal du conteneur tourne au moment de la vérification.]{#deployment-health-checks-process-scope-b .correct explanation="Up indique l’état du processus."}
::option[Toutes les dépendances ont passé une vérification.]{#deployment-health-checks-process-scope-c explanation="Aucun résultat concernant les dépendances n’est affiché."}
:::

## Interroger un point d’accès du service

Un **point d’accès** est une adresse accompagnée d’un chemin que le service prend en charge. Choisissez un chemin qui permette de vérifier le comportement qui vous intéresse. Pour un essai local, utilisez un dossier d’exercice vide. La redirection écrit le fichier de version. Laissez le serveur Python tourner sur l’adresse de bouclage dans ce terminal et arrêtez-le avec Ctrl+C après l’exercice.

```bash
$ mkdir site
$ printf '%s\n' 2 > site/version.txt
$ python3 -m http.server 8091 --bind 127.0.0.1 --directory site
```

Dans un deuxième terminal, demandez le fichier de version. L’option `-f` de curl traite les réponses HTTP d’erreur comme des échecs. L’option `-sS` masque les messages de progression tout en affichant les erreurs.

```bash
$ curl -fsS http://127.0.0.1:8091/version.txt
```

Dans cet exercice, vous devriez obtenir `2`. Une requête réussie vers le fichier de version ne couvre qu’une petite partie des vérifications du site.

:::single-choice{#deployment-health-checks-endpoint-mismatch} La requête réussit et affiche 1. Quel point devez-vous examiner ?

::option[La version qui répond à cette adresse.]{#deployment-health-checks-endpoint-mismatch-a .correct explanation="La connexion a fonctionné, mais la version observée diffère de celle qui était prévue."}
::option[Pourquoi curl ne parvient pas à se connecter.]{#deployment-health-checks-endpoint-mismatch-b explanation="La valeur reçue montre que la connexion a abouti et qu’une réponse est arrivée."}
::option[Si le nom du service contient un chiffre.]{#deployment-health-checks-endpoint-mismatch-c explanation="Le nom du service ne permet pas de déterminer la version renvoyée."}
:::

![Point d’accès de bouclage renvoyant la version 2 depuis le serveur d’exercice LabEx](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-health-checks/version-response.png)

## Vérifier depuis l’emplacement du client

Si une requête fonctionne depuis l’hôte du service, répétez une vérification sans risque depuis l’endroit où les utilisateurs se connectent normalement. Un répartiteur de charge, un proxy ou une règle réseau peut modifier leur trajet. Notez l’adresse vérifiée et la réponse obtenue. Si le résultat ne correspond pas à la release, poursuivez l’examen du déploiement.

:::single-choice{#deployment-health-checks-user-path} Une requête locale renvoie 2, mais l’adresse de test publique renvoie 1. Que faut-il vérifier ensuite ?

::option[Compter les lignes affichées par la requête locale.]{#deployment-health-checks-user-path-a explanation="Le nombre de lignes n’indique pas quel service répond à l’adresse publique."}
::option[Répéter uniquement la même vérification locale.]{#deployment-health-checks-user-path-b explanation="L’accès local a déjà renvoyé la version 2."}
::option[Vérifier quelle version du service répond via le chemin public.]{#deployment-health-checks-user-path-c .correct explanation="Les deux chemins ont abouti à des réponses différentes."}
:::

## Résumé

Vous savez maintenant ce que vérifie chaque contrôle après un déploiement.

1. Vérifiez que le programme principal est en cours d’exécution.
2. Interrogez un point d’accès qui indique la version attendue.
3. Vérifiez séparément le chemin d’accès des utilisateurs.
