---
lesson_id: "compose-service-dependencies"
course_id: "docker-compose"
lang: "fr"
order_index: 6
title: "Dépendances entre services"
description: "Apprenez à distinguer l’ordre de démarrage des services de leur capacité à répondre aux requêtes."
meta_title: "Dépendances entre services - Docker Compose"
meta_description: "Apprenez à distinguer l’ordre de démarrage des services de leur capacité à répondre aux requêtes."
meta_keywords: "dépendances entre services, contrôle d’état, ordre de démarrage, Docker Compose, DevOps, Linux Journey"
---

Un outil qui a besoin d’un serveur web peut envoyer sa première requête trop tôt, même si les services démarrent dans le bon ordre. Un **contrôle d’état** est un petit test exécuté par Docker pour vérifier qu’un service remplit une fonction précise, par exemple répondre à une requête HTTP.

## Choisir un test pour savoir si le service est prêt

Dans cet exemple distinct, le contrôle s’exécute à l’intérieur du conteneur web. Il demande la page web locale. Si la requête aboutit, Docker sait que le serveur répond depuis cet emplacement.

```yaml
services:
  web:
    image: nginx:alpine
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1/"]
      interval: 3s
      timeout: 2s
      retries: 5
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
    depends_on:
      web:
        condition: service_healthy
```

Enregistrez l’exemple sous le nom `compose.health.yaml` dans le même dossier d’exercice. Le contrôle se répète à intervalles réguliers, avec un délai maximal pour chaque tentative. Il vérifie une réponse locale à l’intérieur du conteneur web.

:::single-choice{#compose-service-dependencies-check-location} Où la commande wget s’exécute-t-elle pour ce contrôle d’état ?

::option[Dans le conteneur web.]{#compose-service-dependencies-check-location-c .correct explanation="L’adresse de bouclage est utilisée depuis l’intérieur de ce conteneur."}
::option[Dans le navigateur de l’hôte.]{#compose-service-dependencies-check-location-a explanation="Docker exécute la commande indiquée dans la définition du service web."}
::option[Dans le conteneur d’outils.]{#compose-service-dependencies-check-location-b explanation="Le contrôle est défini sous web."}
:::

## Attendre que la dépendance soit prête

Avec la condition `service_healthy`, Compose attend un contrôle d’état réussi avant de démarrer le conteneur d’outils qui en dépend. Un simple ordre de démarrage permet à ce conteneur de démarrer dès que le service web est en cours d’exécution, parfois avant qu’il puisse répondre à sa première requête.

```bash
$ docker compose -p journey-health -f compose.health.yaml up -d
$ docker compose -p journey-health -f compose.health.yaml ps
```

Vérifiez dans la liste que web est indiqué en bon état et que le conteneur d’outils est en cours d’exécution.

:::single-choice{#compose-service-dependencies-ready-condition} Le processus web a démarré, mais la requête locale échoue encore. Quel réglage permet de retarder le démarrage du conteneur d’outils ?

::option[L’ordre de démarrage seul.]{#compose-service-dependencies-ready-condition-b explanation="Même si web démarre en premier, un délai peut s’écouler avant qu’il réponde."}
::option[Le mode arrière-plan.]{#compose-service-dependencies-ready-condition-c explanation="Ce mode change la façon dont le terminal attend. Il ne détermine pas quand le service est prêt."}
::option[La condition service_healthy.]{#compose-service-dependencies-ready-condition-a .correct explanation="Cette condition oblige Compose à attendre le résultat du contrôle."}
:::

![État de Compose avec la dépendance web en bon état et le conteneur d’outils en cours d’exécution](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-dependencies/healthy-dependency.png)

## Réagir à une panne ultérieure

Une condition de démarrage Compose détermine à quel moment un service dépendant démarre. Un service en bon état au début peut ensuite cesser de répondre. Le client doit pouvoir gérer un échec et se reconnecter lorsque le service redevient disponible. Consultez son état et faites une requête directe pour examiner son comportement actuel.

:::single-choice{#compose-service-dependencies-later-failure} Une requête échoue une heure après le démarrage des deux services. Que pouvez-vous vérifier maintenant ?

::option[Uniquement l’ordre initial de démarrage.]{#compose-service-dependencies-later-failure-a explanation="Cet ordre décrit ce qui s’est passé au démarrage."}
::option[Le résultat actuel du contrôle et une requête depuis le service dépendant.]{#compose-service-dependencies-later-failure-b .correct explanation="Ces vérifications renseignent sur l’état actuel du service et sur le chemin utilisé par le client."}
::option[Le nombre d’images dans le cache Docker.]{#compose-service-dependencies-later-failure-c explanation="Les images disponibles ne disent pas grand-chose sur la réponse d’un service en cours d’exécution."}
:::

## Vérifier depuis deux endroits

Un contrôle local réussi montre ce qui est accessible depuis l’intérieur du conteneur web. Le conteneur d’outils a toujours besoin du réseau du projet et d’une adresse qui lui permette de joindre le service. Vérifiez séparément le résultat du contrôle et celui de la requête depuis le conteneur d’outils.

:::single-choice{#compose-service-dependencies-final-application} Le contrôle est au vert, mais une requête du conteneur d’outils échoue. Quelle comparaison aide à situer le problème ?

::option[Regarder uniquement l’heure du démarrage initial.]{#compose-service-dependencies-final-application-b explanation="L’heure de démarrage ne montre pas quels chemins fonctionnent maintenant."}
::option[Considérer que les deux requêtes réussissent puisque le contrôle de web est au vert.]{#compose-service-dependencies-final-application-c explanation="Le contrôle renseigne sur ce qui se passe depuis un seul emplacement."}
::option[Comparer la même requête depuis l’intérieur de web et vers web depuis le conteneur d’outils.]{#compose-service-dependencies-final-application-a .correct explanation="Vous comparez ainsi la disponibilité du service depuis l’intérieur et le chemin réellement emprunté par le service dépendant."}
:::

## Résumé

Vous savez maintenant vous appuyer sur un contrôle pour déterminer si une dépendance est prête.

1. Identifiez ce que le contrôle d’état observe réellement.
2. Attendez que la dépendance soit prête lorsque l’ordre de démarrage seul ne suffit pas.
3. Vérifiez le comportement actuel si le service tombe en panne par la suite.
