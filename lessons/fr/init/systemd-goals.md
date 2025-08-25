---
index: 6
lang: "fr"
title: "Objectifs de Systemd"
meta_title: "Objectifs de Systemd - Init"
meta_description: "Apprenez les bases des unités systemd et les commandes systemctl essentielles. Comprenez comment gérer les services, afficher les statuts et activer les unités sous Linux. Commencez votre parcours !"
meta_keywords: "systemd, systemctl, services Linux, fichiers d'unité, débutant, tutoriel, guide, commandes Linux"
---

## Lesson Content

Nous n'entrerons pas dans les détails de l'écriture des fichiers d'unité systemd. Cependant, nous allons passer en revue un bref aperçu d'un fichier d'unité et comment contrôler manuellement les unités.

Voici un fichier d'unité de service de base : foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Ceci est une cible de service simple. Au début du fichier, nous voyons une section pour `[Unit]`. Cela nous permet de donner une description à notre fichier d'unité ainsi que de contrôler l'ordre d'activation de l'unité. La partie suivante est la section `[Service]` ; ici, nous pouvons démarrer, arrêter ou recharger un service. Et la section `[Install]` est utilisée pour les dépendances. Ce n'est que la pointe de l'iceberg pour l'écriture de fichiers systemd, je vous implore donc de vous renseigner sur le sujet si vous voulez en savoir plus.

Maintenant, passons à quelques commandes que vous pouvez utiliser avec les unités systemd :

### Lister les unités

```bash
systemctl list-units
```

### Afficher le statut d'une unité

```bash
systemctl status networking.service
```

### Démarrer un service

```bash
sudo systemctl start networking.service
```

### Arrêter un service

```bash
sudo systemctl stop networking.service
```

### Redémarrer un service

```bash
sudo systemctl restart networking.service
```

### Activer une unité

```bash
sudo systemctl enable networking.service
```

### Désactiver une unité

```bash
sudo systemctl disable networking.service
```

Encore une fois, vous n'avez pas encore vu la profondeur de systemd, alors renseignez-vous si vous voulez en savoir plus.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus, qui sont souvent contrôlés par les services systemd :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus de premier plan et d'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top`, à ajuster la priorité avec `renice` et à les terminer avec `kill`. Ce laboratoire vous donnera une expérience pratique des effets d'exécution de la gestion des unités systemd.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des processus sous Linux.

## Quiz Question

Quelle est la commande pour démarrer un service nommé peanut.service ?

## Quiz Answer

sudo systemctl start peanut.service
