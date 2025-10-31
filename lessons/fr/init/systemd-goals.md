---
index: 6
lang: "fr"
title: "Objectifs de Systemd"
meta_title: "Objectifs de Systemd - Init"
meta_description: "Explorez les objectifs de systemd et apprenez à gérer les services Linux avec les commandes systemctl essentielles. Ce guide couvre les bases des fichiers d'unité systemd, comment démarrer, arrêter et activer les services, et visualiser leur état."
meta_keywords: "systemd, systemctl, services Linux, fichiers d'unité, objectifs systemd, gestion des services, unités systemd, débutant, tutoriel, guide, commandes Linux"
---

## Lesson Content

Cette leçon fournit un aperçu fondamental des fichiers d'unité systemd et comment les gérer avec `systemctl`, l'outil principal pour contrôler le système d'initialisation (init). Nous aborderons la structure de base d'un fichier d'unité et les commandes essentielles pour gérer les services Linux.

### Comprendre un Fichier d'Unité Systemd

A un fichier d'unité systemd est un fichier texte simple qui décrit un service, un point de montage, un périphérique ou une autre ressource que systemd peut gérer. Voici un exemple de base d'un fichier d'unité de service nommé `foobar.service` :

```
[Unit]
Description=Mon Service Foobar
After=network.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Ce fichier de service simple est divisé en sections :

- **[Unit]** : Cette section contient les métadonnées et les informations de dépendance. La directive `Description` fournit un nom lisible par l'homme pour l'unité. Des directives comme `After` et `Before` contrôlent l'ordre de démarrage, garantissant que cette unité démarre après que le réseau soit disponible.
- **[Service]** : Cette section définit comment gérer le service. La directive `ExecStart` est cruciale, car elle spécifie la commande à exécuter pour démarrer le service. D'autres directives comme `ExecStop` et `ExecReload` peuvent définir comment arrêter ou recharger le service.
- **[Install]** : Cette section définit le comportement de l'unité lorsqu'elle est activée ou désactivée avec `systemctl`. La directive `WantedBy` indique à systemd de démarrer ce service dans le cadre d'une cible spécifique, telle que `multi-user.target` pour un démarrage standard non graphique.

Ceci n'est qu'un aperçu des fichiers d'unité systemd. Pour des configurations plus avancées, une lecture approfondie sur le sujet est fortement recommandée.

### Commandes Systemctl Essentielles

Explorons maintenant les commandes `systemctl` essentielles que vous utiliserez pour interagir avec les unités systemd et gérer les services Linux.

### Lister les Unités Systemd

Pour voir toutes les unités actives que systemd gère actuellement, utilisez la commande `list-units`.

```bash
systemctl list-units
```

### Vérifier le Statut d'une Unité

Pour afficher l'état détaillé d'une unité spécifique, y compris si elle est active, activée, et ses dernières entrées de journal, utilisez la commande `status`.

```bash
systemctl status networking.service
```

### Gérer les États des Services

Vous pouvez contrôler l'état d'exécution d'un service en utilisant `start`, `stop` et `restart`.

Pour démarrer un service immédiatement :

```bash
sudo systemctl start networking.service
```

Pour arrêter un service en cours d'exécution :

```bash
sudo systemctl stop networking.service
```

Pour arrêter puis redémarrer le service :

```bash
sudo systemctl restart networking.service
```

### Activer et Désactiver les Services

Activer un service crée un lien symbolique qui l'accroche au processus de démarrage, garantissant qu'il démarre automatiquement. Le désactiver supprime ce lien.

Pour activer un service afin qu'il démarre au démarrage :

```bash
sudo systemctl enable networking.service
```

Pour désactiver un service afin qu'il ne démarre pas au démarrage :

```bash
sudo systemctl disable networking.service
```

Ces commandes sont les éléments de base de la gestion des services sur les systèmes Linux modernes. Les maîtriser est une étape clé dans votre parcours Linux.

## Exercise

La pratique est essentielle pour maîtriser de nouvelles compétences. Ce laboratoire pratique vous aidera à renforcer votre compréhension de la gestion des processus, qui sont souvent contrôlés par les services systemd :

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus de premier plan et d'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top`, à ajuster la priorité avec `renice`, et à les terminer avec `kill`. Ce laboratoire vous donnera une expérience pratique des effets d'exécution de la gestion des unités systemd.

Ce laboratoire vous aidera à appliquer ces concepts dans un scénario réel et à renforcer votre confiance dans la gestion des processus sous Linux.

## Quiz Question

What is the command to start a service named peanut.service? Please answer in English. The answer is case-sensitive.

## Quiz Answer

sudo systemctl start peanut.service
