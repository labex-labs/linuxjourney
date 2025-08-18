---
lang: "fr"
title: "Objectifs de Systemd"
meta_title: "Objectifs de Systemd - Init"
meta_description: "Apprenez les bases des unités systemd et les commandes systemctl essentielles. Comprenez comment gérer les services, afficher les statuts et activer les unités sous Linux. Commencez votre parcours !"
meta_keywords: "systemd, systemctl, services Linux, fichiers d'unité, débutant, tutoriel, guide, commandes Linux"
---

## Lesson Content

Nous n'entrerons pas dans les détails de l'écriture des fichiers d'unité systemd. Nous allons cependant passer en revue un bref aperçu d'un fichier d'unité et comment contrôler manuellement les unités.

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

Ceci est une cible de service simple. Au début du fichier, nous voyons une section pour `[Unit]`. Cela nous permet de donner une description à notre fichier d'unité et de contrôler l'ordre d'activation de l'unité. La partie suivante est la section `[Service]` ; ici, nous pouvons démarrer, arrêter ou recharger un service. Et la section `[Install]` est utilisée pour les dépendances. Ce n'est que la pointe de l'iceberg pour l'écriture de fichiers systemd, je vous implore donc de vous renseigner sur le sujet si vous voulez en savoir plus.

Maintenant, passons à quelques commandes que vous pouvez utiliser avec les unités systemd :

### List units

```bash
systemctl list-units
```

### View status of unit

```bash
systemctl status networking.service
```

### Start a service

```bash
sudo systemctl start networking.service
```

### Stop a service

```bash
sudo systemctl stop networking.service
```

### Restart a service

```bash
sudo systemctl restart networking.service
```

### Enable a unit

```bash
sudo systemctl enable networking.service
```

### Disable a unit

```bash
sudo systemctl disable networking.service
```

Encore une fois, vous n'avez pas encore vu à quel point systemd est approfondi, alors renseignez-vous si vous voulez en savoir plus.

## Exercise

Visualisez les statuts des unités et démarrez et arrêtez quelques services. Qu'observez-vous ?

## Quiz Question

Quelle est la commande pour démarrer un service nommé peanut.service ?

## Quiz Answer

sudo systemctl start peanut.service
