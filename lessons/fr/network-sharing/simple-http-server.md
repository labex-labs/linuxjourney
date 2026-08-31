---
lesson_id: "simple-http-server"
course_id: "network-sharing"
lang: "fr"
order_index: 3
title: "Serveur HTTP simple"
description: "Découvrez comment exposer temporairement un répertoire contrôlé avec le serveur HTTP de Python."
meta_title: "Serveur HTTP simple - Partage réseau"
meta_description: "Découvrez comment lancer rapidement un serveur HTTP simple sous Linux avec le module http.server de Python pour partager temporairement des fichiers."
meta_keywords: "serveur HTTP simple Linux, serveur web simple Linux, Python http.server, SimpleHTTPServer Python, partage de fichiers, serveur réseau"
---

Le module `http.server` de Python peut servir des fichiers statiques pour un test de courte durée ou un transfert de confiance. Ce n’est pas un serveur web de production : il ne fournit ni authentification, ni autorisation, ni TLS, ni limitation du débit, ni traitement renforcé face à du trafic hostile.

## Préparer un répertoire de partage

Créez un répertoire dédié qui contient uniquement les fichiers destinés à être exposés. Examinez les fichiers cachés, les liens symboliques, les permissions et les métadonnées sensibles avant de démarrer. Évitez de servir un répertoire personnel, la racine d’un dépôt, un répertoire d’identifiants secrets ou un chemin système.

Employez `--directory` afin d’indiquer explicitement la racine partagée :

```bash
$ python3 -m http.server 8000 --directory /srv/temporary-share
```

En l’absence de fichier d’index, le module génère normalement une liste du répertoire. Toute personne pouvant atteindre le socket en écoute peut être en mesure d’énumérer et de télécharger le contenu servi.

:::single-choice{#http-server-directory-option}
Pourquoi utiliser `--directory /srv/temporary-share` ?

::option[Cette option chiffre automatiquement chaque réponse HTTP.]{#http-server-directory-tls explanation="L’option de répertoire n’ajoute pas TLS."}
::option[Elle crée un compte pour chaque personne qui télécharge.]{#http-server-directory-accounts explanation="Le module de base ne fournit pas d’authentification des utilisateurs."}
::option[Elle rend explicite la racine documentaire voulue.]{#http-server-explicit-root .correct explanation="Une racine explicite et vérifiée réduit le risque d’exposer des fichiers depuis un répertoire de travail choisi par erreur."}
:::

## Contrôler l’adresse d’écoute

Liez le serveur à l’adresse de boucle locale lorsque seul le même hôte doit s’y connecter :

```bash
$ python3 -m http.server 8000 --bind 127.0.0.1 --directory /srv/temporary-share
```

Pour un partage sur un réseau de confiance, liez-le délibérément à l’adresse d’interface appropriée et vérifiez la politique du pare-feu. Une exécution sans liaison restrictive écoute généralement sur toutes les interfaces disponibles, ce qui peut exposer le répertoire au-delà du réseau prévu.

:::single-choice{#http-server-loopback-bind}
Qui peut normalement atteindre un serveur lié à `127.0.0.1` ?

::option[Les clients du même hôte.]{#http-server-local-clients .correct explanation="La liaison à la boucle locale convient aux tests locaux ou à une utilisation derrière un tunnel configuré délibérément."}
::option[N’importe quel hôte de l’Internet public.]{#http-server-public explanation="La boucle locale appartient au même espace de noms réseau et n’est pas une interface publique."}
::option[Uniquement les périphériques connectés en Bluetooth.]{#http-server-bluetooth explanation="Cette adresse est sans rapport avec le transport Bluetooth."}
:::

## Tester l’accès

Depuis l’hôte qui sert les fichiers, demandez un fichier connu et examinez la réponse :

```bash
$ curl -f http://127.0.0.1:8000/example.txt
```

Pour un test distant autorisé, employez l’adresse d’interface choisie plutôt que la boucle locale. Confirmez à la fois que le fichier prévu est accessible et qu’un fichier situé hors de la racine documentaire ne l’est pas. La réussite dans un navigateur ne prouve pas à elle seule que l’exposition est appropriée ou confidentielle.

:::single-choice{#http-server-default-port-command}
Quel port est explicitement sélectionné dans `python3 -m http.server 8000` ?

::option[22]{#http-server-port-22 explanation="Le port 22 est généralement associé à SSH et n’est pas sélectionné ici."}
::option[8000]{#http-server-port-8000 .correct explanation="L’opérande positionnel du port indique au module où écouter."}
::option[443]{#http-server-port-443 explanation="La commande ne configure pas HTTPS sur le port 443."}
:::

## Arrêter et nettoyer

Exécutez le service temporaire dans un terminal supervisé et arrêtez-le avec `Ctrl-C` une fois le transfert terminé. Vérifiez que le socket n’est plus en écoute :

```bash
$ ss -ltn 'sport = :8000'
```

Supprimez les copies temporaires conformément à la politique de gestion des données et annulez toute règle temporaire du pare-feu. Pour une distribution persistante, authentifiée ou exposée à Internet, employez un serveur maintenu et configuré avec un contrôle d’accès et TLS.

:::single-choice{#http-server-completion-check}
Que faut-il faire après la fin du transfert temporaire ?

::option[Arrêter le serveur et vérifier que le port n’est plus en écoute.]{#http-server-stop-verify .correct explanation="Cette vérification confirme que le service réseau temporaire est réellement arrêté."}
::option[Laisser le socket en écoute au cas où quelqu’un en aurait besoin plus tard.]{#http-server-leave-running explanation="Une exposition inutile doit être supprimée lorsque l’usage autorisé prend fin."}
::option[Copier d’autres fichiers privés dans la racine documentaire.]{#http-server-add-private explanation="Seul le contenu intentionnellement partagé doit figurer dans le répertoire servi."}
:::

## Résumé

Vous savez maintenant exécuter un serveur HTTP Python temporaire dont l’exposition est limitée.

1. Servir uniquement un répertoire dédié et vérifié.
2. Lier le serveur à l’adresse appropriée la plus restrictive.
3. Tester l’accès prévu et les limites qui ne doivent pas être franchies.
4. Arrêter le socket en écoute et nettoyer l’accès temporaire après utilisation.
