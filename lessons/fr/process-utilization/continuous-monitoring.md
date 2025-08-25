---
index: 7
lang: "fr"
title: "Surveillance continue"
meta_title: "Surveillance continue - Utilisation des processus"
meta_description: "Apprenez la surveillance continue du système Linux avec sar. Comprenez l'installation, la collecte de données et comment analyser l'utilisation historique des ressources pour les performances. Commencez dès maintenant !"
meta_keywords: "sar, sysstat, surveillance Linux, performances système, surveillance continue, débutant, tutoriel, guide"
---

## Lesson Content

Ces outils de surveillance sont utiles pour examiner votre machine lorsqu'elle rencontre des problèmes, mais qu'en est-il des machines qui ont des problèmes lorsque vous ne regardez pas ? Pour celles-ci, vous devrez utiliser un outil de surveillance continue, quelque chose qui collectera, rapportera et sauvegardera les informations d'activité de votre système. Dans cette leçon, nous allons passer en revue un excellent outil à utiliser : **sar**.

### Installation de sar

Sar est un outil utilisé pour effectuer une analyse historique de votre système. Tout d'abord, assurez-vous de l'avoir installé en installant le paquet `sysstat` : `sudo apt install sysstat`.

### Configuration de la collecte de données

Habituellement, une fois que vous installez `sysstat`, votre système commencera automatiquement à collecter des données. Si ce n'est pas le cas, vous pouvez l'activer en modifiant le champ `ENABLED` dans `/etc/default/sysstat`.

### Utilisation de sar

```bash
sudo sar -q
```

Cette commande listera les détails depuis le début de la journée.

```bash
sudo sar -r
```

Ceci listera les détails de l'utilisation de la mémoire depuis le début de la journée.

```bash
sudo sar -P
```

Ceci listera les détails de l'utilisation du CPU.

Pour voir une vue d'un jour différent, vous pouvez aller dans `/var/log/sysstat/saXX` où `XX` est le jour que vous souhaitez visualiser.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la surveillance du système et de l'analyse des ressources :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus de premier plan et d'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top` et à les terminer avec `kill`.
2. **[Commande Linux top : Surveillance du système en temps réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Apprenez à utiliser diverses options avec la commande `top` pour trier les processus, ajuster les intervalles de mise à jour, filtrer par utilisateur et vous concentrer sur les processus actifs afin de surveiller efficacement les performances du système.
3. **[Commande Linux df : Rapport d'espace disque](https://labex.io/fr/labs/linux-linux-df-command-disk-space-reporting-219188)** - Ce laboratoire présente la commande `df` sous Linux, un utilitaire qui affiche des informations sur l'utilisation de l'espace disque sur les systèmes de fichiers montés, ce qui est un aspect clé de la surveillance du système.

Ces laboratoires vous aideront à appliquer les concepts de surveillance des ressources système dans des scénarios réels et à renforcer votre confiance dans l'analyse de l'activité du système.

## Quiz Question

Quel est un bon outil à utiliser pour surveiller les ressources système ?

## Quiz Answer

sar
